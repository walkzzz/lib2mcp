"""
Tool Validator

工具验证器，验证生成的MCP工具定义。
"""

from typing import Dict, List, Any, Optional
import logging

from ..exceptions import ValidationError
from ..config import Config

logger = logging.getLogger(__name__)


class ToolValidator:
    """工具验证器"""
    
    def __init__(self, config: Optional[Config] = None):
        self.config = config or Config()
    
    def validate_tool(self, tool: Dict[str, Any]) -> Dict[str, Any]:
        """验证单个工具"""
        result = {
            'valid': True,
            'errors': [],
            'warnings': []
        }
        
        # 检查必需字段
        required_fields = ['name', 'description', 'inputSchema']
        for field in required_fields:
            if field not in tool:
                result['errors'].append(f"缺少必需字段: {field}")
                result['valid'] = False
        
        # 检查名称格式
        if 'name' in tool:
            name = tool['name']
            if not isinstance(name, str) or not name.strip():
                result['errors'].append("工具名称不能为空")
                result['valid'] = False
            elif len(name) > 100:
                result['warnings'].append("工具名称过长")
        
        # 检查输入schema
        if 'inputSchema' in tool:
            schema_validation = self._validate_json_schema(tool['inputSchema'])
            if not schema_validation['valid']:
                result['errors'].extend(schema_validation['errors'])
                result['valid'] = False
            result['warnings'].extend(schema_validation['warnings'])
        
        return result
    
    def _validate_json_schema(self, schema: Dict[str, Any]) -> Dict[str, Any]:
        """验证JSON Schema"""
        result = {
            'valid': True,
            'errors': [],
            'warnings': []
        }
        
        if not isinstance(schema, dict):
            result['errors'].append("Schema必须是字典类型")
            result['valid'] = False
            return result
        
        # 检查type字段
        if 'type' not in schema:
            result['warnings'].append("Schema缺少type字段")
        
        return result