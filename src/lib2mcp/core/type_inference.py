"""
Type Inference Engine

类型推断器，负责处理Type Hints、默认值类型推断等功能。
"""

import inspect
import sys
from typing import (
    Dict, List, Any, Optional, Union, Tuple, Set, 
    get_type_hints, get_origin, get_args
)
import logging

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    try:
        from typing_extensions import Literal
    except ImportError:
        Literal = None

from ..exceptions import TypeInferenceError
from ..models import APIFunction
from ..config import Config

logger = logging.getLogger(__name__)


class TypeInferenceEngine:
    """
    类型推断器 - 推断和转换Python类型为JSON Schema
    
    功能包括：
    - Type Hints解析和转换
    - 默认值类型推断
    - 复杂类型处理
    - JSON Schema生成
    """
    
    def __init__(self, config: Optional[Config] = None):
        self.config = config or Config()
        self._type_cache: Dict[str, Dict[str, Any]] = {}
        
    def infer_parameter_types(self, func_info: APIFunction) -> Dict[str, Dict[str, Any]]:
        """
        推断函数参数的类型信息
        
        Args:
            func_info: API函数信息
            
        Returns:
            Dict[str, Dict[str, Any]]: 参数类型信息，包含JSON Schema
        """
        cache_key = f"{func_info.module}.{func_info.name}"
        if cache_key in self._type_cache:
            return self._type_cache[cache_key]
        
        parameter_types = {}
        
        for param_name, param_info in func_info.parameters.items():
            try:
                type_info = self._infer_parameter_type(param_name, param_info, func_info)
                parameter_types[param_name] = type_info
            except Exception as e:
                logger.debug(f"推断参数 {param_name} 类型失败: {e}")
                # 使用默认类型
                parameter_types[param_name] = self._get_default_type_info(param_info)
        
        self._type_cache[cache_key] = parameter_types
        return parameter_types
    
    def _infer_parameter_type(self, param_name: str, param_info: Dict[str, Any], 
                            func_info: APIFunction) -> Dict[str, Any]:
        """推断单个参数的类型"""
        type_info = {
            'name': param_name,
            'python_type': None,
            'json_schema': {},
            'description': '',
            'required': not param_info.get('has_default', False),
            'default': param_info.get('default')
        }
        
        # 1. 尝试从Type Hint获取类型
        annotation = param_info.get('annotation')
        if annotation and annotation != inspect.Parameter.empty:
            try:
                schema = self._convert_annotation_to_schema(annotation)
                type_info['python_type'] = annotation
                type_info['json_schema'] = schema
                type_info['description'] = self._generate_type_description(annotation)
                return type_info
            except Exception as e:
                logger.debug(f"转换类型注解失败 {annotation}: {e}")
        
        # 2. 尝试从默认值推断类型
        default_value = param_info.get('default')
        if default_value is not None and default_value != inspect.Parameter.empty:
            try:
                schema = self._infer_type_from_default(default_value)
                type_info['python_type'] = type(default_value)
                type_info['json_schema'] = schema
                type_info['description'] = f"类型从默认值推断: {type(default_value).__name__}"
                return type_info
            except Exception as e:
                logger.debug(f"从默认值推断类型失败: {e}")
        
        # 3. 尝试从参数名推断类型
        try:
            schema = self._infer_type_from_name(param_name)
            if schema:
                type_info['json_schema'] = schema
                type_info['description'] = f"类型从参数名推断: {param_name}"
                return type_info
        except Exception as e:
            logger.debug(f"从参数名推断类型失败: {e}")
        
        # 4. 使用通用类型
        type_info['json_schema'] = {'type': 'string', 'description': '通用字符串类型'}
        type_info['description'] = '未知类型，默认为字符串'
        
        return type_info
    
    def _convert_annotation_to_schema(self, annotation: Any) -> Dict[str, Any]:
        """将Python类型注解转换为JSON Schema"""
        
        # 处理基本类型
        if annotation == str:
            return {'type': 'string'}
        elif annotation == int:
            return {'type': 'integer'}
        elif annotation == float:
            return {'type': 'number'}
        elif annotation == bool:
            return {'type': 'boolean'}
        elif annotation == list:
            return {'type': 'array'}
        elif annotation == dict:
            return {'type': 'object'}
        elif annotation is None or annotation == type(None):
            return {'type': 'null'}
        
        # 处理泛型类型
        origin = get_origin(annotation)
        args = get_args(annotation)
        
        if origin is Union:
            return self._handle_union_type(args)
        elif origin is list or origin is List:
            return self._handle_list_type(args)
        elif origin is dict or origin is Dict:
            return self._handle_dict_type(args)
        elif origin is tuple or origin is Tuple:
            return self._handle_tuple_type(args)
        elif origin is set or origin is Set:
            return self._handle_set_type(args)
        elif Literal and origin is Literal:
            return self._handle_literal_type(args)
        
        # 处理Optional类型
        if self._is_optional_type(annotation):
            inner_type = self._get_optional_inner_type(annotation)
            inner_schema = self._convert_annotation_to_schema(inner_type)
            return {**inner_schema, 'nullable': True}
        
        # 处理自定义类
        if inspect.isclass(annotation):
            return self._handle_custom_class(annotation)
        
        # 处理其他复杂类型
        return self._handle_complex_type(annotation)
    
    def _handle_union_type(self, args: Tuple) -> Dict[str, Any]:
        """处理Union类型"""
        # 检查是否为Optional (Union[T, None])
        if len(args) == 2 and type(None) in args:
            non_none_type = args[0] if args[1] is type(None) else args[1]
            schema = self._convert_annotation_to_schema(non_none_type)
            schema['nullable'] = True
            return schema
        
        # 一般的Union类型
        schemas = []
        for arg in args:
            try:
                schema = self._convert_annotation_to_schema(arg)
                schemas.append(schema)
            except Exception:
                continue
        
        if len(schemas) == 1:
            return schemas[0]
        elif len(schemas) > 1:
            return {'oneOf': schemas}
        else:
            return {'type': 'string', 'description': 'Union类型，默认为字符串'}
    
    def _handle_list_type(self, args: Tuple) -> Dict[str, Any]:
        """处理List类型"""
        schema: Dict[str, Any] = {'type': 'array'}
        
        if args:
            try:
                item_schema = self._convert_annotation_to_schema(args[0])
                schema['items'] = item_schema
            except Exception:
                schema['items'] = {'type': 'string'}
        
        return schema
    
    def _handle_dict_type(self, args: Tuple) -> Dict[str, Any]:
        """处理Dict类型"""
        schema: Dict[str, Any] = {'type': 'object'}
        
        if len(args) >= 2:
            try:
                # 键类型（通常是字符串）
                key_type = args[0]
                value_type = args[1]
                
                # JSON只支持字符串键
                if key_type != str:
                    logger.debug(f"字典键类型 {key_type} 不是字符串，将转换为字符串")
                
                value_schema = self._convert_annotation_to_schema(value_type)
                schema['additionalProperties'] = value_schema
                
            except Exception:
                schema['additionalProperties'] = {'type': 'string'}
        
        return schema
    
    def _handle_tuple_type(self, args: Tuple) -> Dict[str, Any]:
        """处理Tuple类型"""
        # 元组在JSON中表示为数组
        schema: Dict[str, Any] = {'type': 'array'}
        
        if args:
            if len(args) == 2 and args[1] is ...:
                # Tuple[T, ...] - 可变长度元组
                item_schema = self._convert_annotation_to_schema(args[0])
                schema['items'] = item_schema
            else:
                # 固定长度元组
                items = []
                for arg in args:
                    try:
                        item_schema = self._convert_annotation_to_schema(arg)
                        items.append(item_schema)
                    except Exception:
                        items.append({'type': 'string'})
                
                schema['items'] = items
                schema['minItems'] = len(items)
                schema['maxItems'] = len(items)
        
        return schema
    
    def _handle_set_type(self, args: Tuple) -> Dict[str, Any]:
        """处理Set类型"""
        # 集合在JSON中表示为数组，但要求唯一
        schema: Dict[str, Any] = {'type': 'array', 'uniqueItems': True}
        
        if args:
            try:
                item_schema = self._convert_annotation_to_schema(args[0])
                schema['items'] = item_schema
            except Exception:
                schema['items'] = {'type': 'string'}
        
        return schema
    
    def _handle_literal_type(self, args: Tuple) -> Dict[str, Any]:
        """处理Literal类型"""
        if not args:
            return {'type': 'string'}
        
        # 获取所有可能的值
        values = list(args)
        
        # 确定基础类型
        if all(isinstance(v, str) for v in values):
            return {'type': 'string', 'enum': values}
        elif all(isinstance(v, int) for v in values):
            return {'type': 'integer', 'enum': values}
        elif all(isinstance(v, (int, float)) for v in values):
            return {'type': 'number', 'enum': values}
        else:
            # 混合类型
            return {'enum': values}
    
    def _handle_custom_class(self, cls: type) -> Dict[str, Any]:
        """处理自定义类"""
        # 对于自定义类，我们生成一个对象schema
        schema: Dict[str, Any] = {
            'type': 'object',
            'description': f'自定义类型: {cls.__name__}'
        }
        
        # 如果类有文档字符串，添加到描述中
        if cls.__doc__:
            schema['description'] += f' - {cls.__doc__.strip()}'
        
        # 尝试分析类的属性
        try:
            properties: Dict[str, Any] = {}
            annotations = getattr(cls, '__annotations__', {})
            
            for attr_name, attr_type in annotations.items():
                if not attr_name.startswith('_'):
                    try:
                        prop_schema = self._convert_annotation_to_schema(attr_type)
                        properties[attr_name] = prop_schema
                    except Exception:
                        properties[attr_name] = {'type': 'string'}
            
            if properties:
                schema['properties'] = properties
        
        except Exception as e:
            logger.debug(f"分析自定义类 {cls.__name__} 失败: {e}")
        
        return schema
    
    def _handle_complex_type(self, annotation: Any) -> Dict[str, Any]:
        """处理其他复杂类型"""
        # 对于无法识别的复杂类型，提供基本的fallback
        type_name = getattr(annotation, '__name__', str(annotation))
        
        return {
            'type': 'string',
            'description': f'复杂类型: {type_name}，请提供字符串表示'
        }
    
    def _is_optional_type(self, annotation: Any) -> bool:
        """检查是否为Optional类型"""
        origin = get_origin(annotation)
        if origin is Union:
            args = get_args(annotation)
            return len(args) == 2 and type(None) in args
        return False
    
    def _get_optional_inner_type(self, annotation: Any) -> Any:
        """获取Optional类型的内部类型"""
        args = get_args(annotation)
        return args[0] if args[1] is type(None) else args[1]
    
    def _infer_type_from_default(self, default_value: Any) -> Dict[str, Any]:
        """从默认值推断类型"""
        if isinstance(default_value, str):
            return {'type': 'string', 'default': default_value}
        elif isinstance(default_value, int):
            return {'type': 'integer', 'default': default_value}
        elif isinstance(default_value, float):
            return {'type': 'number', 'default': default_value}
        elif isinstance(default_value, bool):
            return {'type': 'boolean', 'default': default_value}
        elif isinstance(default_value, list):
            # 尝试推断数组项类型
            if default_value:
                first_item = default_value[0]
                item_schema = self._infer_type_from_default(first_item)
                return {
                    'type': 'array',
                    'items': item_schema,
                    'default': default_value
                }
            else:
                return {'type': 'array', 'default': []}
        elif isinstance(default_value, dict):
            return {'type': 'object', 'default': default_value}
        elif default_value is None:
            return {'type': 'null', 'default': None}
        else:
            # 其他类型转换为字符串
            return {
                'type': 'string',
                'default': str(default_value),
                'description': f'从 {type(default_value).__name__} 类型转换'
            }
    
    def _infer_type_from_name(self, param_name: str) -> Optional[Dict[str, Any]]:
        """从参数名推断类型"""
        name_lower = param_name.lower()
        
        # 常见的命名模式
        if any(keyword in name_lower for keyword in ['id', 'index', 'count', 'size', 'length']):
            return {'type': 'integer', 'description': f'整数类型（从参数名 {param_name} 推断）'}
        
        elif any(keyword in name_lower for keyword in ['name', 'title', 'description', 'text', 'str']):
            return {'type': 'string', 'description': f'字符串类型（从参数名 {param_name} 推断）'}
        
        elif any(keyword in name_lower for keyword in ['is_', 'has_', 'can_', 'should_', 'enable', 'disable']):
            return {'type': 'boolean', 'description': f'布尔类型（从参数名 {param_name} 推断）'}
        
        elif any(keyword in name_lower for keyword in ['list', 'items', 'values', 'array']):
            return {'type': 'array', 'description': f'数组类型（从参数名 {param_name} 推断）'}
        
        elif any(keyword in name_lower for keyword in ['data', 'config', 'options', 'params', 'kwargs']):
            return {'type': 'object', 'description': f'对象类型（从参数名 {param_name} 推断）'}
        
        elif any(keyword in name_lower for keyword in ['price', 'cost', 'amount', 'rate', 'percent']):
            return {'type': 'number', 'description': f'数值类型（从参数名 {param_name} 推断）'}
        
        return None
    
    def _generate_type_description(self, annotation: Any) -> str:
        """生成类型描述"""
        if annotation == str:
            return "字符串类型"
        elif annotation == int:
            return "整数类型"
        elif annotation == float:
            return "浮点数类型"
        elif annotation == bool:
            return "布尔类型"
        elif annotation == list:
            return "列表类型"
        elif annotation == dict:
            return "字典类型"
        
        # 处理泛型类型
        origin = get_origin(annotation)
        if origin:
            origin_name = getattr(origin, '__name__', str(origin))
            args = get_args(annotation)
            if args:
                args_desc = ', '.join(self._generate_type_description(arg) for arg in args)
                return f"{origin_name}[{args_desc}]"
            else:
                return origin_name
        
        # 处理类类型
        if inspect.isclass(annotation):
            return f"{annotation.__name__} 类型"
        
        return str(annotation)
    
    def _get_default_type_info(self, param_info: Dict[str, Any]) -> Dict[str, Any]:
        """获取默认类型信息"""
        return {
            'name': 'unknown',
            'python_type': None,
            'json_schema': {'type': 'string', 'description': '未知类型，默认为字符串'},
            'description': '类型推断失败，使用默认字符串类型',
            'required': not param_info.get('has_default', False),
            'default': param_info.get('default')
        }
    
    def infer_return_type(self, func_info: APIFunction) -> Optional[Dict[str, Any]]:
        """推断函数返回类型"""
        return_annotation = func_info.return_annotation
        
        if return_annotation and return_annotation != inspect.Parameter.empty:
            try:
                schema = self._convert_annotation_to_schema(return_annotation)
                return {
                    'python_type': return_annotation,
                    'json_schema': schema,
                    'description': self._generate_type_description(return_annotation)
                }
            except Exception as e:
                logger.debug(f"推断返回类型失败: {e}")
        
        # 从函数名推断返回类型
        func_name = func_info.name.lower()
        if func_name.startswith('is_') or func_name.startswith('has_'):
            return {
                'python_type': bool,
                'json_schema': {'type': 'boolean'},
                'description': '布尔类型（从函数名推断）'
            }
        elif func_name.startswith('get_') and 'count' in func_name:
            return {
                'python_type': int,
                'json_schema': {'type': 'integer'},
                'description': '整数类型（从函数名推断）'
            }
        elif func_name.startswith('list_') or func_name.endswith('_list'):
            return {
                'python_type': list,
                'json_schema': {'type': 'array'},
                'description': '数组类型（从函数名推断）'
            }
        
        return None
    
    def validate_type_conversion(self, func_info: APIFunction) -> List[str]:
        """验证类型转换的问题"""
        warnings = []
        
        parameter_types = self.infer_parameter_types(func_info)
        
        for param_name, type_info in parameter_types.items():
            schema = type_info.get('json_schema', {})
            
            # 检查复杂类型
            if 'oneOf' in schema:
                warnings.append(f"参数 {param_name} 使用联合类型，可能导致类型不明确")
            
            # 检查缺失的类型信息
            if schema.get('type') == 'string' and '推断' in type_info.get('description', ''):
                warnings.append(f"参数 {param_name} 的类型是推断的，建议添加类型注解")
            
            # 检查必需参数但没有描述
            if type_info.get('required') and not type_info.get('description'):
                warnings.append(f"必需参数 {param_name} 缺少描述信息")
        
        return warnings