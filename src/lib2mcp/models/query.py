"""
Query data models

定义查询相关的数据模型。
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
from .tool import SearchFilter, QueryResult, ToolIndex

# 重新导出，保持向后兼容
__all__ = [
    "SearchFilter",
    "QueryResult", 
    "ToolIndex",
]