"""
MCP Tool Generator

MCP工具生成器，负责生成MCP工具定义和执行逻辑。
"""

from typing import Dict, List, Any, Optional
import logging

from ..exceptions import GenerationError
from ..models import APIFunction
from ..config import Config

logger = logging.getLogger(__name__)


class MCPToolGenerator:
    """MCP工具生成器"""
    
    def __init__(self, config: Optional[Config] = None):
        self.config = config or Config()
    
    def generate_tool(self, api_func: APIFunction, 
                     parameter_types: Dict[str, Any],
                     return_type: Optional[Dict[str, Any]],
                     description_data: Dict[str, Any]) -> Dict[str, Any]:
        """生成MCP工具定义"""
        
        tool_name = self._generate_tool_name(api_func)
        
        tool = {
            'name': tool_name,
            'description': description_data.get('description', ''),
            'inputSchema': {
                'type': 'object',
                'properties': self._generate_properties(parameter_types),
                'required': self._get_required_parameters(parameter_types)
            },
            'metadata': {
                'source_function': api_func.full_name,
                'module': api_func.module,
                'class_name': api_func.class_name,
                'is_async': api_func.is_async,
                'is_static': api_func.is_staticmethod,
                'is_classmethod': api_func.is_classmethod
            }
        }
        
        if return_type:
            tool['outputSchema'] = return_type.get('json_schema', {})
        
        return tool
    
    def _generate_tool_name(self, api_func: APIFunction) -> str:
        """生成工具名称"""
        prefix = self.config.output.tool_prefix
        if api_func.class_name:
            name = f"{api_func.module}_{api_func.class_name}_{api_func.name}"
        else:
            name = f"{api_func.module}_{api_func.name}"
        
        # 替换特殊字符
        name = name.replace('.', '_').replace('-', '_')
        
        return f"{prefix}{name}" if prefix else name
    
    def _generate_properties(self, parameter_types: Dict[str, Any]) -> Dict[str, Any]:
        """生成参数属性"""
        properties = {}
        
        for param_name, type_info in parameter_types.items():
            if param_name == 'self':
                continue
                
            schema = type_info.get('json_schema', {})
            description = type_info.get('description', '')
            
            prop = schema.copy()
            if description:
                prop['description'] = description
            
            properties[param_name] = prop
        
        return properties
    
    def _get_required_parameters(self, parameter_types: Dict[str, Any]) -> List[str]:
        """获取必需参数列表"""
        required = []
        
        for param_name, type_info in parameter_types.items():
            if param_name == 'self':
                continue
                
            if type_info.get('required', False):
                required.append(param_name)
        
        return required