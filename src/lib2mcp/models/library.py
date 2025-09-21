"""
Library data models

定义库分析相关的数据模型。
"""

from typing import Dict, List, Any, Optional, Union
from datetime import datetime
from dataclasses import dataclass, field
from enum import Enum


class ParameterKind(Enum):
    """参数类型枚举"""
    POSITIONAL_ONLY = "POSITIONAL_ONLY"
    POSITIONAL_OR_KEYWORD = "POSITIONAL_OR_KEYWORD"
    VAR_POSITIONAL = "VAR_POSITIONAL"
    KEYWORD_ONLY = "KEYWORD_ONLY" 
    VAR_KEYWORD = "VAR_KEYWORD"


@dataclass
class APIFunction:
    """API函数信息"""
    name: str
    module: str
    signature: str
    docstring: Optional[str] = None
    parameters: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    return_annotation: Optional[Any] = None
    is_async: bool = False
    is_generator: bool = False
    is_classmethod: bool = False
    is_staticmethod: bool = False
    decorators: List[str] = field(default_factory=list)
    source_file: Optional[str] = None
    line_number: Optional[int] = None
    class_name: Optional[str] = None
    
    @property
    def full_name(self) -> str:
        """获取完整的函数名称"""
        if self.class_name:
            return f"{self.module}.{self.class_name}.{self.name}"
        return f"{self.module}.{self.name}"
    
    @property
    def is_method(self) -> bool:
        """是否为类方法"""
        return self.class_name is not None
    
    def get_parameter_names(self) -> List[str]:
        """获取参数名列表"""
        return list(self.parameters.keys())
    
    def get_required_parameters(self) -> List[str]:
        """获取必需参数列表"""
        return [
            name for name, info in self.parameters.items()
            if not info.get('has_default', False)
        ]


@dataclass 
class ClassInfo:
    """类信息"""
    name: str
    module: str
    docstring: Optional[str] = None
    methods: Dict[str, APIFunction] = field(default_factory=dict)
    properties: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    base_classes: List[str] = field(default_factory=list)
    is_abstract: bool = False
    source_file: Optional[str] = None
    line_number: Optional[int] = None
    
    @property
    def full_name(self) -> str:
        """获取完整的类名称"""
        return f"{self.module}.{self.name}"
    
    def get_public_methods(self) -> Dict[str, APIFunction]:
        """获取公共方法"""
        return {
            name: method for name, method in self.methods.items()
            if not name.startswith('_')
        }
    
    def get_static_methods(self) -> Dict[str, APIFunction]:
        """获取静态方法"""
        return {
            name: method for name, method in self.methods.items()
            if method.is_staticmethod
        }
    
    def get_class_methods(self) -> Dict[str, APIFunction]:
        """获取类方法"""
        return {
            name: method for name, method in self.methods.items()
            if method.is_classmethod
        }


@dataclass
class ModuleInfo:
    """模块信息"""
    name: str
    docstring: Optional[str] = None
    file_path: Optional[str] = None
    functions: Dict[str, APIFunction] = field(default_factory=dict)
    classes: Dict[str, ClassInfo] = field(default_factory=dict)
    constants: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    imports: List[Dict[str, Any]] = field(default_factory=list)
    
    @property
    def total_apis(self) -> int:
        """获取API总数"""
        total = len(self.functions)
        for class_info in self.classes.values():
            total += len(class_info.methods)
        return total
    
    def get_all_functions(self) -> Dict[str, APIFunction]:
        """获取所有函数（包括类方法）"""
        all_functions = self.functions.copy()
        
        for class_info in self.classes.values():
            for method_name, method in class_info.methods.items():
                # 使用类的全名作为key
                key = f"{class_info.name}.{method_name}"
                all_functions[key] = method
                
        return all_functions
    
    def get_public_apis(self) -> Dict[str, APIFunction]:
        """获取公共API"""
        public_apis = {}
        
        # 公共函数
        for name, func in self.functions.items():
            if not name.startswith('_'):
                public_apis[name] = func
        
        # 公共类和方法
        for class_name, class_info in self.classes.items():
            if not class_name.startswith('_'):
                for method_name, method in class_info.get_public_methods().items():
                    key = f"{class_name}.{method_name}"
                    public_apis[key] = method
                    
        return public_apis


@dataclass
class LibraryMetadata:
    """库元数据"""
    name: str
    version: str = "unknown"
    description: str = ""
    author: str = ""
    modules: Dict[str, ModuleInfo] = field(default_factory=dict)
    dependencies: List[str] = field(default_factory=list)
    total_functions: int = 0
    total_classes: int = 0
    analyzed_at: datetime = field(default_factory=datetime.now)
    
    @property
    def module_count(self) -> int:
        """模块数量"""
        return len(self.modules)
    
    @property 
    def total_apis(self) -> int:
        """总API数量"""
        return sum(module.total_apis for module in self.modules.values())
    
    def get_all_functions(self) -> Dict[str, APIFunction]:
        """获取所有函数"""
        all_functions = {}
        
        for module_name, module_info in self.modules.items():
            module_functions = module_info.get_all_functions()
            for func_name, func in module_functions.items():
                # 确保函数名唯一
                if '.' in func_name:
                    # 已经包含类名
                    full_name = f"{module_name}.{func_name}"
                else:
                    # 模块级函数
                    full_name = f"{module_name}.{func_name}"
                all_functions[full_name] = func
                
        return all_functions
    
    def get_public_apis(self) -> Dict[str, APIFunction]:
        """获取所有公共API"""
        public_apis = {}
        
        for module_name, module_info in self.modules.items():
            module_apis = module_info.get_public_apis()
            for api_name, api_func in module_apis.items():
                # 确保API名唯一
                if '.' in api_name:
                    # 已经包含类名
                    full_name = f"{module_name}.{api_name}"
                else:
                    # 模块级函数
                    full_name = f"{module_name}.{api_name}"
                public_apis[full_name] = api_func
                
        return public_apis
    
    def get_modules_by_pattern(self, pattern: str) -> Dict[str, ModuleInfo]:
        """根据模式获取模块"""
        import fnmatch
        return {
            name: module for name, module in self.modules.items()
            if fnmatch.fnmatch(name, pattern)
        }
    
    def get_statistics(self) -> Dict[str, Any]:
        """获取统计信息"""
        stats = {
            'total_modules': self.module_count,
            'total_functions': self.total_functions,
            'total_classes': self.total_classes,
            'total_apis': self.total_apis,
            'modules_with_docs': sum(
                1 for m in self.modules.values() 
                if m.docstring and m.docstring.strip()
            ),
            'functions_with_docs': sum(
                1 for m in self.modules.values()
                for f in m.get_all_functions().values()
                if f.docstring and f.docstring.strip()
            ),
            'async_functions': sum(
                1 for m in self.modules.values()
                for f in m.get_all_functions().values()
                if f.is_async
            ),
            'generator_functions': sum(
                1 for m in self.modules.values()
                for f in m.get_all_functions().values()
                if f.is_generator
            ),
        }
        return stats