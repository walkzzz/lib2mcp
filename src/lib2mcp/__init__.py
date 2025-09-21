"""
Lib2MCP - Python Library to MCP Tool Converter

A powerful tool that automatically converts Python library APIs into MCP (Model Context Protocol) 
tool specifications, enabling AI models to directly call Python library functions.
"""

__version__ = "1.0.0"
__author__ = "Lib2MCP Team"
__email__ = "dev@lib2mcp.com"

from .converter import LibraryConverter
from .query_manager import ToolQueryManager
from .config import Config
from .exceptions import Lib2MCPError, ConversionError, ValidationError

__all__ = [
    "LibraryConverter",
    "ToolQueryManager", 
    "Config",
    "Lib2MCPError",
    "ConversionError",
    "ValidationError",
]