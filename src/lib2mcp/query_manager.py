"""
Tool Query Manager

工具查询管理器，提供工具索引、搜索、分类等功能。
"""

from typing import Dict, List, Any, Optional, Set
import logging
import json
from pathlib import Path

from .exceptions import QueryError
from .config import Config

logger = logging.getLogger(__name__)


class ToolQueryManager:
    """工具查询管理器"""
    
    def __init__(self, tools: Optional[Dict[str, Any]] = None, config: Optional[Config] = None):
        self.config = config or Config()
        self.tools = tools or {}
        self._index = {}
        
        if self.tools:
            self._build_index()
    
    def _build_index(self) -> None:
        """构建工具索引"""
        self._index = {
            'by_name': {},
            'by_module': {},
            'by_category': {},
            'by_tags': {},
            'keywords': set()
        }
        
        for tool_id, tool in self.tools.items():
            name = tool.get('name', '')
            metadata = tool.get('metadata', {})
            module = metadata.get('module', '')
            description = tool.get('description', '')
            
            # 按名称索引
            self._index['by_name'][name] = tool_id
            
            # 按模块索引
            if module:
                if module not in self._index['by_module']:
                    self._index['by_module'][module] = []
                self._index['by_module'][module].append(tool_id)
            
            # 提取关键词
            words = self._extract_keywords(name + ' ' + description)
            self._index['keywords'].update(words)
    
    def _extract_keywords(self, text: str) -> Set[str]:
        """提取关键词"""
        import re
        # 简单的关键词提取
        words = re.findall(r'\w+', text.lower())
        return set(word for word in words if len(word) > 2)
    
    def search_tools(self, query: str, limit: int = 20) -> List[Dict[str, Any]]:
        """搜索工具"""
        query_lower = query.lower()
        results = []
        
        for tool_id, tool in self.tools.items():
            score = self._calculate_relevance_score(tool, query_lower)
            if score > 0:
                results.append({
                    'tool_id': tool_id,
                    'tool': tool,
                    'score': score
                })
        
        # 按分数排序
        results.sort(key=lambda x: x['score'], reverse=True)
        
        return results[:limit]
    
    def _calculate_relevance_score(self, tool: Dict[str, Any], query: str) -> float:
        """计算相关性分数"""
        score = 0.0
        
        name = tool.get('name', '').lower()
        description = tool.get('description', '').lower()
        
        # 名称匹配
        if query in name:
            score += 10.0
        
        # 描述匹配
        if query in description:
            score += 5.0
        
        # 关键词匹配
        query_words = query.split()
        text = name + ' ' + description
        for word in query_words:
            if word in text:
                score += 1.0
        
        return score
    
    def filter_by_module(self, module_name: str) -> List[Dict[str, Any]]:
        """按模块过滤工具"""
        if module_name not in self._index['by_module']:
            return []
        
        tool_ids = self._index['by_module'][module_name]
        return [{'tool_id': tid, 'tool': self.tools[tid]} for tid in tool_ids]
    
    def list_all_tools(self, page: int = 1, size: int = 20) -> Dict[str, Any]:
        """列出所有工具（分页）"""
        total = len(self.tools)
        start_idx = (page - 1) * size
        end_idx = start_idx + size
        
        tool_items = list(self.tools.items())
        page_items = tool_items[start_idx:end_idx]
        
        return {
            'tools': [{'tool_id': tid, 'tool': tool} for tid, tool in page_items],
            'pagination': {
                'page': page,
                'size': size,
                'total': total,
                'pages': (total + size - 1) // size
            }
        }
    
    def get_tool_detail(self, tool_id: str) -> Optional[Dict[str, Any]]:
        """获取工具详情"""
        return self.tools.get(tool_id)
    
    def get_statistics(self) -> Dict[str, Any]:
        """获取统计信息"""
        stats = {
            'total_tools': len(self.tools),
            'modules': list(self._index['by_module'].keys()),
            'module_count': len(self._index['by_module']),
            'keyword_count': len(self._index['keywords'])
        }
        
        return stats