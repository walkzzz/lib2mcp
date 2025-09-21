"""
API Extractor

API提取器，负责从库元数据中提取和分类API信息。
"""

import inspect
from typing import Dict, List, Any, Optional, Set, Tuple, Iterator
import logging

from ..exceptions import AnalysisError
from ..models import LibraryMetadata, ModuleInfo, APIFunction, ClassInfo
from ..config import Config

logger = logging.getLogger(__name__)


class APIExtractor:
    """
    API提取器 - 从库元数据中提取可转换的API
    
    功能包括：
    - 提取模块级函数
    - 提取类方法、静态方法、实例方法
    - API分类和过滤
    - API权重和优先级计算
    """
    
    def __init__(self, config: Optional[Config] = None):
        self.config = config or Config()
        self._extracted_apis: Dict[str, APIFunction] = {}
        
    def extract_apis(self, library_metadata: LibraryMetadata) -> Dict[str, APIFunction]:
        """
        从库元数据中提取所有API
        
        Args:
            library_metadata: 库元数据
            
        Returns:
            Dict[str, APIFunction]: API字典，key为API的完整名称
        """
        logger.info(f"开始提取库 {library_metadata.name} 的API")
        
        extracted_apis = {}
        
        for module_name, module_info in library_metadata.modules.items():
            try:
                module_apis = self._extract_module_apis(module_info)
                extracted_apis.update(module_apis)
            except Exception as e:
                logger.warning(f"提取模块 {module_name} 的API失败: {e}")
                continue
        
        # 过滤和排序API
        filtered_apis = self._filter_apis(extracted_apis)
        
        logger.info(f"API提取完成，总数: {len(extracted_apis)}, 过滤后: {len(filtered_apis)}")
        
        self._extracted_apis = filtered_apis
        return filtered_apis
    
    def _extract_module_apis(self, module_info: ModuleInfo) -> Dict[str, APIFunction]:
        """提取单个模块的API"""
        apis = {}
        
        # 1. 提取模块级函数
        for func_name, func_info in module_info.functions.items():
            if self._should_include_function(func_info):
                api_key = self._generate_api_key(func_info)
                apis[api_key] = func_info
        
        # 2. 提取类相关的API
        for class_name, class_info in module_info.classes.items():
            if self._should_include_class(class_info):
                class_apis = self._extract_class_apis(class_info)
                apis.update(class_apis)
        
        return apis
    
    def _extract_class_apis(self, class_info: ClassInfo) -> Dict[str, APIFunction]:
        """提取类相关的API"""
        apis = {}
        
        # 提取实例方法、类方法、静态方法
        for method_name, method_info in class_info.methods.items():
            if self._should_include_method(method_info, class_info):
                api_key = self._generate_api_key(method_info)
                
                # 设置方法类型标记
                method_info.class_name = class_info.name
                
                apis[api_key] = method_info
        
        # 如果类有构造函数，也考虑提取
        if '__init__' in class_info.methods:
            init_method = class_info.methods['__init__']
            if self._should_include_constructor(init_method, class_info):
                # 创建一个特殊的构造器API
                constructor_api = self._create_constructor_api(init_method, class_info)
                api_key = self._generate_api_key(constructor_api)
                apis[api_key] = constructor_api
        
        return apis
    
    def _create_constructor_api(self, init_method: APIFunction, class_info: ClassInfo) -> APIFunction:
        """为类构造函数创建API"""
        constructor = APIFunction(
            name=f"create_{class_info.name.lower()}",
            module=class_info.module,
            signature=init_method.signature,
            docstring=class_info.docstring or init_method.docstring,
            parameters=init_method.parameters.copy(),
            return_annotation=class_info.name,
            is_async=False,
            is_generator=False,
            is_classmethod=False,
            is_staticmethod=False,
            decorators=init_method.decorators.copy(),
            source_file=init_method.source_file,
            line_number=init_method.line_number,
            class_name=class_info.name
        )
        
        # 移除self参数
        if 'self' in constructor.parameters:
            del constructor.parameters['self']
        
        return constructor
    
    def _should_include_function(self, func_info: APIFunction) -> bool:
        """判断是否应该包含函数"""
        # 跳过私有函数
        if func_info.name.startswith('_') and not self.config.conversion.include_private:
            return False
        
        # 跳过魔术方法
        if (func_info.name.startswith('__') and func_info.name.endswith('__') 
            and not self.config.conversion.include_magic_methods):
            return False
        
        # 检查函数签名是否可用
        if not self._is_callable_signature(func_info):
            return False
        
        return True
    
    def _should_include_class(self, class_info: ClassInfo) -> bool:
        """判断是否应该包含类"""
        # 跳过私有类
        if class_info.name.startswith('_') and not self.config.conversion.include_private:
            return False
        
        # 跳过抽象类（可配置）
        if class_info.is_abstract and not getattr(self.config.conversion, 'include_abstract_classes', False):
            return False
        
        # 检查是否有可用的方法
        public_methods = [m for m in class_info.methods.values() if not m.name.startswith('_')]
        if not public_methods:
            return False
        
        return True
    
    def _should_include_method(self, method_info: APIFunction, class_info: ClassInfo) -> bool:
        """判断是否应该包含方法"""
        # 跳过私有方法
        if method_info.name.startswith('_') and not self.config.conversion.include_private:
            # 但是保留构造函数
            if method_info.name != '__init__':
                return False
        
        # 跳过魔术方法
        if (method_info.name.startswith('__') and method_info.name.endswith('__') 
            and not self.config.conversion.include_magic_methods):
            # 保留一些重要的魔术方法
            important_magic = ['__init__', '__call__', '__str__', '__repr__']
            if method_info.name not in important_magic:
                return False
        
        # 检查方法签名是否可用
        if not self._is_callable_signature(method_info):
            return False
        
        return True
    
    def _should_include_constructor(self, init_method: APIFunction, class_info: ClassInfo) -> bool:
        """判断是否应该包含构造函数"""
        # 检查构造函数是否有有用的参数
        params = init_method.get_parameter_names()
        # 移除self参数
        if 'self' in params:
            params.remove('self')
        
        # 如果没有参数，可能不太有用
        if not params and not getattr(self.config.conversion, 'include_parameterless_constructors', True):
            return False
        
        return True
    
    def _is_callable_signature(self, func_info: APIFunction) -> bool:
        """检查函数签名是否可调用"""
        try:
            # 检查是否有过于复杂的参数类型
            for param_name, param_info in func_info.parameters.items():
                annotation = param_info.get('annotation')
                if annotation and self._is_complex_type(annotation):
                    logger.debug(f"函数 {func_info.name} 包含复杂类型参数 {param_name}: {annotation}")
                    # 暂时不排除，后续由类型推断器处理
            
            return True
        except Exception as e:
            logger.debug(f"检查函数 {func_info.name} 签名失败: {e}")
            return False
    
    def _is_complex_type(self, type_annotation: Any) -> bool:
        """检查是否为复杂类型"""
        # 这里可以实现更复杂的类型检查逻辑
        # 目前返回False，表示暂时接受所有类型
        return False
    
    def _generate_api_key(self, func_info: APIFunction) -> str:
        """生成API的唯一键"""
        if func_info.class_name:
            return f"{func_info.module}.{func_info.class_name}.{func_info.name}"
        else:
            return f"{func_info.module}.{func_info.name}"
    
    def _filter_apis(self, apis: Dict[str, APIFunction]) -> Dict[str, APIFunction]:
        """过滤和排序API"""
        filtered = {}
        
        for api_key, api_func in apis.items():
            # 应用自定义过滤规则
            if self._apply_custom_filters(api_func):
                filtered[api_key] = api_func
        
        return filtered
    
    def _apply_custom_filters(self, func_info: APIFunction) -> bool:
        """应用自定义过滤规则"""
        # 可以在这里实现更复杂的过滤逻辑
        
        # 例如：根据函数名模式过滤
        excluded_patterns = getattr(self.config.conversion, 'excluded_function_patterns', [])
        for pattern in excluded_patterns:
            if self._match_pattern(func_info.name, pattern):
                return False
        
        # 例如：根据参数数量过滤
        max_params = getattr(self.config.conversion, 'max_parameters', 20)
        if len(func_info.parameters) > max_params:
            logger.debug(f"函数 {func_info.name} 参数过多 ({len(func_info.parameters)} > {max_params})")
            return False
        
        return True
    
    def _match_pattern(self, text: str, pattern: str) -> bool:
        """模式匹配"""
        import fnmatch
        return fnmatch.fnmatch(text, pattern)
    
    def get_apis_by_category(self) -> Dict[str, List[APIFunction]]:
        """按分类获取API"""
        categories = {
            'functions': [],
            'methods': [],
            'static_methods': [],
            'class_methods': [],
            'constructors': []
        }
        
        for api_func in self._extracted_apis.values():
            if api_func.class_name:
                if api_func.name.startswith('create_'):
                    categories['constructors'].append(api_func)
                elif api_func.is_staticmethod:
                    categories['static_methods'].append(api_func)
                elif api_func.is_classmethod:
                    categories['class_methods'].append(api_func)
                else:
                    categories['methods'].append(api_func)
            else:
                categories['functions'].append(api_func)
        
        return categories
    
    def get_apis_by_module(self) -> Dict[str, List[APIFunction]]:
        """按模块获取API"""
        modules = {}
        
        for api_func in self._extracted_apis.values():
            module_name = api_func.module
            if module_name not in modules:
                modules[module_name] = []
            modules[module_name].append(api_func)
        
        return modules
    
    def get_high_priority_apis(self, limit: int = 50) -> List[APIFunction]:
        """获取高优先级API"""
        # 按优先级排序API
        scored_apis = []
        
        for api_func in self._extracted_apis.values():
            score = self._calculate_api_priority(api_func)
            scored_apis.append((score, api_func))
        
        # 按分数降序排序
        scored_apis.sort(key=lambda x: x[0], reverse=True)
        
        return [api_func for _, api_func in scored_apis[:limit]]
    
    def _calculate_api_priority(self, func_info: APIFunction) -> float:
        """计算API优先级分数"""
        score = 0.0
        
        # 1. 有文档的API优先级更高
        if func_info.docstring and func_info.docstring.strip():
            score += 2.0
        
        # 2. 公共API优先级更高
        if not func_info.name.startswith('_'):
            score += 3.0
        
        # 3. 模块级函数优先级较高
        if not func_info.class_name:
            score += 1.0
        
        # 4. 静态方法和类方法优先级较高
        if func_info.is_staticmethod or func_info.is_classmethod:
            score += 1.5
        
        # 5. 参数适中的函数优先级更高
        param_count = len(func_info.parameters)
        if 1 <= param_count <= 5:
            score += 1.0
        elif param_count == 0:
            score += 0.5
        elif param_count > 10:
            score -= 1.0
        
        # 6. 有类型注解的函数优先级更高
        has_annotations = any(
            info.get('annotation') is not None 
            for info in func_info.parameters.values()
        )
        if has_annotations:
            score += 1.0
        
        # 7. 根据函数名判断重要性
        important_keywords = ['get', 'set', 'create', 'delete', 'update', 'list', 'find', 'search']
        if any(keyword in func_info.name.lower() for keyword in important_keywords):
            score += 0.5
        
        return score
    
    def get_api_statistics(self) -> Dict[str, Any]:
        """获取API统计信息"""
        categories = self.get_apis_by_category()
        modules = self.get_apis_by_module()
        
        stats = {
            'total_apis': len(self._extracted_apis),
            'by_category': {k: len(v) for k, v in categories.items()},
            'by_module': {k: len(v) for k, v in modules.items()},
            'with_docstring': sum(
                1 for api in self._extracted_apis.values() 
                if api.docstring and api.docstring.strip()
            ),
            'with_type_annotations': sum(
                1 for api in self._extracted_apis.values()
                if any(info.get('annotation') for info in api.parameters.values())
            ),
            'async_functions': sum(
                1 for api in self._extracted_apis.values() if api.is_async
            ),
            'generator_functions': sum(
                1 for api in self._extracted_apis.values() if api.is_generator
            ),
        }
        
        return stats
    
    def export_api_list(self, format: str = 'json') -> str:
        """导出API列表"""
        api_list = []
        
        for api_key, api_func in self._extracted_apis.items():
            api_data = {
                'key': api_key,
                'name': api_func.name,
                'module': api_func.module,
                'class_name': api_func.class_name,
                'signature': api_func.signature,
                'docstring': api_func.docstring,
                'is_async': api_func.is_async,
                'is_generator': api_func.is_generator,
                'is_staticmethod': api_func.is_staticmethod,
                'is_classmethod': api_func.is_classmethod,
                'parameter_count': len(api_func.parameters),
                'has_docstring': bool(api_func.docstring and api_func.docstring.strip()),
            }
            api_list.append(api_data)
        
        if format == 'json':
            import json
            return json.dumps(api_list, indent=2, ensure_ascii=False)
        elif format == 'yaml':
            try:
                import yaml  # type: ignore
                return yaml.dump(api_list, default_flow_style=False, allow_unicode=True)
            except ImportError:
                raise ValueError("YAML 支持需要安装 PyYAML: pip install PyYAML")
        else:
            raise ValueError(f"不支持的导出格式: {format}")