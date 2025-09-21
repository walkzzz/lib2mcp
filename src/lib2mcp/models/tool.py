"""
Tool data models

定义MCP工具相关的数据模型。
"""

from typing import Dict, List, Any, Optional
from datetime import datetime
from dataclasses import dataclass, field


@dataclass
class ToolParameter:
    """工具参数定义"""
    name: str
    type: str
    description: str = ""
    required: bool = True
    default: Optional[Any] = None
    schema: Dict[str, Any] = field(default_factory=dict)


@dataclass
class MCPTool:
    """MCP工具定义"""
    name: str
    description: str
    input_schema: Dict[str, Any]
    output_schema: Optional[Dict[str, Any]] = None
    parameters: List[ToolParameter] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    created_at: datetime = field(default_factory=datetime.now)


@dataclass
class ToolMetadata:
    """工具元数据"""
    tool_id: str
    source_module: str
    source_function: str
    category: str = "general"
    tags: List[str] = field(default_factory=list)
    version: str = "1.0.0"
    author: str = ""
    
    
@dataclass
class SearchFilter:
    """搜索过滤器"""
    query: Optional[str] = None
    category: Optional[str] = None
    module: Optional[str] = None
    tags: List[str] = field(default_factory=list)
    limit: int = 20
    offset: int = 0


@dataclass
class QueryResult:
    """查询结果"""
    tools: List[Dict[str, Any]]
    total: int
    page: int
    size: int
    query_time: float = 0.0


@dataclass
class ToolIndex:
    """工具索引"""
    tools: Dict[str, MCPTool] = field(default_factory=dict)
    by_category: Dict[str, List[str]] = field(default_factory=dict)
    by_module: Dict[str, List[str]] = field(default_factory=dict)
    by_tags: Dict[str, List[str]] = field(default_factory=dict)
    keywords: Dict[str, List[str]] = field(default_factory=dict)