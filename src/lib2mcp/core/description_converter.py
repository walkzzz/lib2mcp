"""
Description Converter

描述转换器，负责解析docstring、生成工具描述等功能。
"""

import re
from typing import Dict, List, Any, Optional, Tuple
import logging

from ..exceptions import ConversionError
from ..models import APIFunction
from ..config import Config

logger = logging.getLogger(__name__)


class DescriptionConverter:
    """
    描述转换器 - 解析docstring并生成工具描述
    
    功能包括：
    - 多格式docstring解析（Google、NumPy、Sphinx）
    - 参数描述提取
    - 返回值描述生成
    - 使用示例提取
    """
    
    def __init__(self, config: Optional[Config] = None):
        self.config = config or Config()
        
    def convert_function_description(self, func_info: APIFunction) -> Dict[str, Any]:
        """
        转换函数描述
        
        Args:
            func_info: API函数信息
            
        Returns:
            Dict[str, Any]: 包含工具描述的字典
        """
        description_data = {
            'title': self._generate_title(func_info),
            'description': self._generate_description(func_info),
            'parameters_description': {},
            'return_description': '',
            'examples': [],
            'notes': [],
            'warnings': []
        }
        
        # 解析docstring
        if func_info.docstring:
            parsed = self._parse_docstring(func_info.docstring)
            description_data.update(parsed)
        
        # 如果描述为空，生成基础描述
        if not description_data['description']:
            description_data['description'] = self._generate_fallback_description(func_info)
        
        # 处理参数描述
        if not description_data['parameters_description']:
            description_data['parameters_description'] = self._generate_parameter_descriptions(func_info)
        
        return description_data
    
    def _generate_title(self, func_info: APIFunction) -> str:
        """生成工具标题"""
        if func_info.class_name:
            return f"{func_info.class_name}.{func_info.name}"
        else:
            return f"{func_info.module.split('.')[-1]}.{func_info.name}"
    
    def _generate_description(self, func_info: APIFunction) -> str:
        """生成基础描述"""
        # 从函数名生成描述
        name_desc = self._describe_function_name(func_info.name)
        
        if func_info.class_name:
            return f"{name_desc}（{func_info.class_name}类的方法）"
        else:
            return f"{name_desc}（{func_info.module}模块的函数）"
    
    def _describe_function_name(self, func_name: str) -> str:
        """从函数名生成描述"""
        # 简单的函数名描述映射
        name_mappings = {
            'get': '获取',
            'set': '设置', 
            'create': '创建',
            'delete': '删除',
            'update': '更新',
            'list': '列出',
            'find': '查找',
            'search': '搜索',
            'add': '添加',
            'remove': '移除',
            'load': '加载',
            'save': '保存',
            'open': '打开',
            'close': '关闭',
            'read': '读取',
            'write': '写入',
            'parse': '解析',
            'format': '格式化',
            'validate': '验证',
            'convert': '转换',
            'transform': '变换',
            'calculate': '计算',
            'process': '处理'
        }
        
        for keyword, description in name_mappings.items():
            if func_name.lower().startswith(keyword):
                return f"{description}数据"
        
        return f"执行{func_name}操作"
    
    def _parse_docstring(self, docstring: str) -> Dict[str, Any]:
        """解析docstring"""
        docstring = docstring.strip()
        if not docstring:
            return {}
        
        # 尝试识别docstring格式
        if self._is_google_style(docstring):
            return self._parse_google_docstring(docstring)
        elif self._is_numpy_style(docstring):
            return self._parse_numpy_docstring(docstring)
        elif self._is_sphinx_style(docstring):
            return self._parse_sphinx_docstring(docstring)
        else:
            return self._parse_plain_docstring(docstring)
    
    def _is_google_style(self, docstring: str) -> bool:
        """检查是否为Google风格docstring"""
        google_sections = ['Args:', 'Arguments:', 'Returns:', 'Return:', 'Yields:', 'Raises:', 'Examples:', 'Note:', 'Notes:']
        return any(section in docstring for section in google_sections)
    
    def _is_numpy_style(self, docstring: str) -> bool:
        """检查是否为NumPy风格docstring"""
        numpy_sections = ['Parameters\n----------', 'Returns\n-------', 'Yields\n------']
        return any(section in docstring for section in numpy_sections)
    
    def _is_sphinx_style(self, docstring: str) -> bool:
        """检查是否为Sphinx风格docstring"""
        sphinx_patterns = [':param ', ':type ', ':return:', ':rtype:', ':raises:']
        return any(pattern in docstring for pattern in sphinx_patterns)
    
    def _parse_google_docstring(self, docstring: str) -> Dict[str, Any]:
        """解析Google风格docstring"""
        result = {
            'description': '',
            'parameters_description': {},
            'return_description': '',
            'examples': [],
            'notes': [],
            'warnings': []
        }
        
        lines = docstring.split('\n')
        current_section = 'description'
        current_content = []
        
        for line in lines:
            line = line.strip()
            
            if line in ['Args:', 'Arguments:']:
                if current_content and current_section == 'description':
                    result['description'] = '\n'.join(current_content).strip()
                current_section = 'args'
                current_content = []
            elif line in ['Returns:', 'Return:']:
                if current_section == 'args':
                    result['parameters_description'] = self._parse_args_section(current_content)
                current_section = 'returns'
                current_content = []
            elif line == 'Examples:':
                if current_section == 'returns':
                    result['return_description'] = '\n'.join(current_content).strip()
                current_section = 'examples'
                current_content = []
            elif line in ['Note:', 'Notes:']:
                current_section = 'notes'
                current_content = []
            else:
                current_content.append(line)
        
        # 处理最后一个section
        if current_section == 'description' and current_content:
            result['description'] = '\n'.join(current_content).strip()
        elif current_section == 'args' and current_content:
            result['parameters_description'] = self._parse_args_section(current_content)
        elif current_section == 'returns' and current_content:
            result['return_description'] = '\n'.join(current_content).strip()
        elif current_section == 'examples' and current_content:
            result['examples'] = ['\n'.join(current_content).strip()]
        elif current_section == 'notes' and current_content:
            result['notes'] = ['\n'.join(current_content).strip()]
        
        return result
    
    def _parse_numpy_docstring(self, docstring: str) -> Dict[str, Any]:
        """解析NumPy风格docstring"""
        # 简化实现
        return self._parse_plain_docstring(docstring)
    
    def _parse_sphinx_docstring(self, docstring: str) -> Dict[str, Any]:
        """解析Sphinx风格docstring"""
        result = {
            'description': '',
            'parameters_description': {},
            'return_description': '',
            'examples': [],
            'notes': [],
            'warnings': []
        }
        
        lines = docstring.split('\n')
        description_lines = []
        
        for line in lines:
            line = line.strip()
            
            if line.startswith(':param '):
                # :param name: description
                match = re.match(r':param\s+(\w+):\s*(.+)', line)
                if match:
                    param_name, param_desc = match.groups()
                    result['parameters_description'][param_name] = param_desc
            elif line.startswith(':return:'):
                # :return: description
                result['return_description'] = line[8:].strip()
            elif not line.startswith(':'):
                description_lines.append(line)
        
        result['description'] = '\n'.join(description_lines).strip()
        return result
    
    def _parse_plain_docstring(self, docstring: str) -> Dict[str, Any]:
        """解析普通docstring"""
        lines = docstring.split('\n')
        description = []
        
        for line in lines:
            line = line.strip()
            if line:
                description.append(line)
        
        return {
            'description': '\n'.join(description),
            'parameters_description': {},
            'return_description': '',
            'examples': [],
            'notes': [],
            'warnings': []
        }
    
    def _parse_args_section(self, lines: List[str]) -> Dict[str, str]:
        """解析参数section"""
        params = {}
        current_param = None
        current_desc = []
        
        for line in lines:
            if not line:
                continue
                
            # 检查是否为新参数
            if ':' in line and not line.startswith(' '):
                # 保存上一个参数
                if current_param and current_desc:
                    params[current_param] = ' '.join(current_desc).strip()
                
                # 解析新参数
                parts = line.split(':', 1)
                if len(parts) == 2:
                    current_param = parts[0].strip()
                    current_desc = [parts[1].strip()] if parts[1].strip() else []
            else:
                # 继续描述
                if current_param:
                    current_desc.append(line.strip())
        
        # 保存最后一个参数
        if current_param and current_desc:
            params[current_param] = ' '.join(current_desc).strip()
        
        return params
    
    def _generate_fallback_description(self, func_info: APIFunction) -> str:
        """生成备用描述"""
        desc_parts = []
        
        # 基础描述
        desc_parts.append(self._describe_function_name(func_info.name))
        
        # 添加模块信息
        if func_info.module:
            desc_parts.append(f"来自{func_info.module}模块")
        
        # 添加类信息
        if func_info.class_name:
            desc_parts.append(f"属于{func_info.class_name}类")
        
        # 添加方法类型信息
        if func_info.is_staticmethod:
            desc_parts.append("静态方法")
        elif func_info.is_classmethod:
            desc_parts.append("类方法")
        elif func_info.class_name:
            desc_parts.append("实例方法")
        
        # 添加异步信息
        if func_info.is_async:
            desc_parts.append("异步函数")
        
        return "，".join(desc_parts)
    
    def _generate_parameter_descriptions(self, func_info: APIFunction) -> Dict[str, str]:
        """生成参数描述"""
        descriptions = {}
        
        for param_name, param_info in func_info.parameters.items():
            # 跳过self参数
            if param_name == 'self':
                continue
                
            desc_parts = []
            
            # 基于参数名生成描述
            if 'id' in param_name.lower():
                desc_parts.append("标识符")
            elif 'name' in param_name.lower():
                desc_parts.append("名称")
            elif 'path' in param_name.lower():
                desc_parts.append("路径")
            elif 'url' in param_name.lower():
                desc_parts.append("URL地址")
            elif 'data' in param_name.lower():
                desc_parts.append("数据")
            elif 'config' in param_name.lower():
                desc_parts.append("配置")
            else:
                desc_parts.append(f"{param_name}参数")
            
            # 添加类型信息
            annotation = param_info.get('annotation')
            if annotation:
                type_name = getattr(annotation, '__name__', str(annotation))
                desc_parts.append(f"类型：{type_name}")
            
            # 添加默认值信息
            default = param_info.get('default')
            if default is not None:
                desc_parts.append(f"默认值：{default}")
            
            descriptions[param_name] = "，".join(desc_parts)
        
        return descriptions
    
    def enhance_description(self, description_data: Dict[str, Any], 
                          func_info: APIFunction) -> Dict[str, Any]:
        """增强描述信息"""
        if not self.config.description.enhance_descriptions:
            return description_data
        
        enhanced = description_data.copy()
        
        # 添加使用建议
        if not enhanced.get('notes'):
            enhanced['notes'] = []
        
        # 添加参数数量信息
        param_count = len(func_info.parameters)
        if 'self' in func_info.parameters:
            param_count -= 1
            
        if param_count > 5:
            enhanced['notes'].append(f"此函数有{param_count}个参数，请仔细检查参数要求")
        
        # 添加异步函数提醒
        if func_info.is_async:
            enhanced['notes'].append("这是一个异步函数，需要在异步环境中调用")
        
        # 添加类方法提醒
        if func_info.is_staticmethod:
            enhanced['notes'].append("这是一个静态方法，可以直接通过类调用")
        elif func_info.is_classmethod:
            enhanced['notes'].append("这是一个类方法，会自动传入类作为第一个参数")
        
        return enhanced