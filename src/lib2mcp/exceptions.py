"""
Lib2MCP exceptions module

定义系统中使用的所有异常类。
"""

from typing import Optional, Any


class Lib2MCPError(Exception):
    """Base exception for all Lib2MCP errors."""
    
    def __init__(self, message: str, details: Optional[dict] = None):
        super().__init__(message)
        self.message = message
        self.details = details or {}


class ConversionError(Lib2MCPError):
    """Raised when library conversion fails."""
    pass


class ValidationError(Lib2MCPError):
    """Raised when tool validation fails."""
    pass


class AnalysisError(Lib2MCPError):
    """Raised when library analysis fails."""
    pass


class TypeInferenceError(Lib2MCPError):
    """Raised when type inference fails."""
    pass


class ConfigurationError(Lib2MCPError):
    """Raised when configuration is invalid."""
    pass


class QueryError(Lib2MCPError):
    """Raised when tool query operations fail."""
    pass


class GenerationError(Lib2MCPError):
    """Raised when MCP tool generation fails."""
    pass