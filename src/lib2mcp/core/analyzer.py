"""
Library Analyzer

负责分析Python库的结构，包括AST解析、模块发现、API识别等核心功能。
"""

import ast
import importlib
import inspect
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional, Set, Tuple, Union
import logging

from ..exceptions import AnalysisError
from ..models import LibraryMetadata, ModuleInfo, APIFunction, ClassInfo
from ..config import Config

logger = logging.getLogger(__name__)


class LibraryAnalyzer:
    """
    库分析器 - 分析Python库结构和API信息
    
    功能包括：
    - AST解析和源代码分析
    - 模块发现和依赖分析
    - API识别和分类
    - 运行时信息提取
    """
    
    def __init__(self, config: Optional[Config] = None):
        self.config = config or Config()
        self._module_cache: Dict[str, ModuleInfo] = {}
        self._analyzed_modules: Set[str] = set()
        
    def analyze_library(self, library_name: str) -> LibraryMetadata:
        """
        分析指定的Python库
        
        Args:
            library_name: 库名称，如 'requests', 'pandas' 等
            
        Returns:
            LibraryMetadata: 包含库的完整元数据信息
            
        Raises:
            AnalysisError: 当分析失败时抛出
        """
        try:
            logger.info(f"开始分析库: {library_name}")
            
            # 导入库
            library_module = self._import_library(library_name)

            # 获取库基本信息
            library_info = self._extract_library_info(library_module)
            
            # 发现所有模块
            modules = self._discover_modules(library_module)
            
            # 分析每个模块
            analyzed_modules = {}
            for module_name, module_obj in modules.items():
                if self._should_analyze_module(module_name):
                    try:
                        module_info = self._analyze_module(module_obj, module_name)
                        analyzed_modules[module_name] = module_info
                    except Exception as e:
                        logger.warning(f"分析模块 {module_name} 失败: {e}")
                        continue
            
            # 创建库元数据
            metadata = LibraryMetadata(
                name=library_name,
                version=library_info.get('version', 'unknown'),
                description=library_info.get('description', ''),
                author=library_info.get('author', ''),
                modules=analyzed_modules,
                dependencies=self._analyze_dependencies(library_module),
                total_functions=sum(len(m.functions) for m in analyzed_modules.values()),
                total_classes=sum(len(m.classes) for m in analyzed_modules.values())
            )
            
            logger.info(f"库分析完成: {library_name}, "
                       f"模块数: {len(analyzed_modules)}, "
                       f"函数数: {metadata.total_functions}, "
                       f"类数: {metadata.total_classes}")
            
            return metadata
            
        except AnalysisError:
            # 直接重新抛出AnalysisError，不进行任何其他处理
            raise
        except Exception as e:
            raise AnalysisError(f"分析库 {library_name} 失败: {str(e)}")
    
    def _import_library(self, library_name: str) -> Any:
        """导入指定的库"""
        try:
            return importlib.import_module(library_name)
        except ImportError as e:
            raise AnalysisError(f"无法导入库 {library_name}: {str(e)}")
    
    def _extract_library_info(self, library_module: Any) -> Dict[str, str]:
        """提取库的基本信息"""
        info = {}
        
        # 获取版本信息
        for version_attr in ['__version__', 'VERSION', 'version']:
            if hasattr(library_module, version_attr):
                info['version'] = str(getattr(library_module, version_attr))
                break
        
        # 获取描述信息
        if hasattr(library_module, '__doc__') and library_module.__doc__:
            info['description'] = library_module.__doc__.strip()
        
        # 获取作者信息
        for author_attr in ['__author__', 'AUTHOR', 'author']:
            if hasattr(library_module, author_attr):
                info['author'] = str(getattr(library_module, author_attr))
                break
                
        return info
    
    def _discover_modules(self, library_module: Any) -> Dict[str, Any]:
        """发现库中的所有模块"""
        modules = {}
        
        # 添加主模块
        modules[library_module.__name__] = library_module
        
        # 如果是包，递归发现子模块
        if hasattr(library_module, '__path__'):
            package_path = library_module.__path__[0]
            self._discover_submodules(
                package_path, 
                library_module.__name__, 
                modules, 
                depth=0
            )
        
        return modules
    
    def _discover_submodules(self, package_path: str, package_name: str, 
                           modules: Dict[str, Any], depth: int = 0) -> None:
        """递归发现子模块"""
        if depth >= self.config.max_depth:
            return
            
        try:
            package_dir = Path(package_path)
            
            for item in package_dir.iterdir():
                if item.is_file() and item.suffix == '.py' and item.name != '__init__.py':
                    # Python文件
                    module_name = f"{package_name}.{item.stem}"
                    if self._should_include_module(module_name):
                        try:
                            module_obj = importlib.import_module(module_name)
                            modules[module_name] = module_obj
                        except Exception as e:
                            logger.debug(f"无法导入模块 {module_name}: {e}")
                            
                elif item.is_dir() and not item.name.startswith('.'):
                    # 子包
                    if (item / '__init__.py').exists():
                        subpackage_name = f"{package_name}.{item.name}"
                        if self._should_include_module(subpackage_name):
                            try:
                                submodule = importlib.import_module(subpackage_name)
                                modules[subpackage_name] = submodule
                                # 递归处理子包
                                self._discover_submodules(
                                    str(item), 
                                    subpackage_name, 
                                    modules, 
                                    depth + 1
                                )
                            except Exception as e:
                                logger.debug(f"无法导入子包 {subpackage_name}: {e}")
                                
        except Exception as e:
            logger.debug(f"扫描包路径 {package_path} 失败: {e}")
    
    def _should_include_module(self, module_name: str) -> bool:
        """检查是否应该包含指定模块"""
        # 检查包含模式
        include_patterns = self.config.include_patterns
        if include_patterns and not any(
            self._match_pattern(module_name, pattern) for pattern in include_patterns
        ):
            return False
        
        # 检查排除模式
        exclude_patterns = self.config.exclude_patterns
        if exclude_patterns and any(
            self._match_pattern(module_name, pattern) for pattern in exclude_patterns
        ):
            return False
            
        return True
    
    def _should_analyze_module(self, module_name: str) -> bool:
        """检查是否应该分析指定模块"""
        if module_name in self._analyzed_modules:
            return False
            
        return self._should_include_module(module_name)
    
    def _match_pattern(self, text: str, pattern: str) -> bool:
        """简单的模式匹配，支持通配符*"""
        import fnmatch
        return fnmatch.fnmatch(text, pattern)
    
    def _analyze_module(self, module_obj: Any, module_name: str) -> ModuleInfo:
        """分析单个模块"""
        if module_name in self._module_cache:
            return self._module_cache[module_name]
        
        logger.debug(f"分析模块: {module_name}")
        
        module_info = ModuleInfo(
            name=module_name,
            docstring=getattr(module_obj, '__doc__', None),
            file_path=getattr(module_obj, '__file__', None),
            functions={},
            classes={},
            constants={},
            imports=[]
        )
        
        # 分析模块成员
        for name, obj in inspect.getmembers(module_obj):
            if name.startswith('_') and not self.config.include_private:
                continue
                
            try:
                if inspect.isfunction(obj):
                    # 函数
                    if self._is_module_member(obj, module_obj):
                        func_info = self._analyze_function(obj, name, module_name)
                        module_info.functions[name] = func_info
                        
                elif inspect.isclass(obj):
                    # 类
                    if self._is_module_member(obj, module_obj):
                        class_info = self._analyze_class(obj, name, module_name)
                        module_info.classes[name] = class_info
                        
                elif not inspect.ismodule(obj) and not inspect.isbuiltin(obj):
                    # 常量
                    if not callable(obj):
                        module_info.constants[name] = {
                            'value': obj,
                            'type': type(obj).__name__
                        }
                        
            except Exception as e:
                logger.debug(f"分析模块成员 {name} 失败: {e}")
                continue
        
        # 如果有源代码，进行AST分析
        if module_info.file_path:
            try:
                ast_info = self._analyze_ast(module_info.file_path)
                module_info.imports = ast_info.get('imports', [])
            except Exception as e:
                logger.debug(f"AST分析失败: {e}")
        
        self._module_cache[module_name] = module_info
        self._analyzed_modules.add(module_name)
        
        return module_info
    
    def _is_module_member(self, obj: Any, module_obj: Any) -> bool:
        """检查对象是否属于指定模块"""
        return getattr(obj, '__module__', None) == module_obj.__name__
    
    def _analyze_function(self, func: Any, name: str, module_name: str) -> APIFunction:
        """分析单个函数"""
        try:
            signature = inspect.signature(func)
            
            return APIFunction(
                name=name,
                module=module_name,
                signature=str(signature),
                docstring=getattr(func, '__doc__', None),
                parameters=self._extract_parameters(signature),
                return_annotation=signature.return_annotation if signature.return_annotation != signature.empty else None,
                is_async=inspect.iscoroutinefunction(func),
                is_generator=inspect.isgeneratorfunction(func),
                decorators=self._extract_decorators(func),
                source_file=getattr(func, '__code__', None) and getattr(func.__code__, 'co_filename', None),
                line_number=getattr(func, '__code__', None) and getattr(func.__code__, 'co_firstlineno', None)
            )
        except Exception as e:
            logger.debug(f"分析函数 {name} 失败: {e}")
            return APIFunction(
                name=name,
                module=module_name,
                signature="(...)",
                docstring=getattr(func, '__doc__', None),
                parameters={},
                return_annotation=None,
                is_async=False,
                is_generator=False,
                decorators=[],
                source_file=None,
                line_number=None
            )
    
    def _analyze_class(self, cls: Any, name: str, module_name: str) -> ClassInfo:
        """分析单个类"""
        class_info = ClassInfo(
            name=name,
            module=module_name,
            docstring=getattr(cls, '__doc__', None),
            methods={},
            properties={},
            base_classes=[base.__name__ for base in cls.__bases__ if base != object],
            is_abstract=inspect.isabstract(cls),
        )
        
        # 分析类方法
        for method_name, method_obj in inspect.getmembers(cls, inspect.isfunction):
            if method_name.startswith('_') and not self.config.include_private:
                continue
                
            try:
                method_info = self._analyze_function(method_obj, method_name, module_name)
                method_info.class_name = name
                method_info.is_classmethod = isinstance(inspect.getattr_static(cls, method_name), classmethod)
                method_info.is_staticmethod = isinstance(inspect.getattr_static(cls, method_name), staticmethod)
                class_info.methods[method_name] = method_info
            except Exception as e:
                logger.debug(f"分析类方法 {method_name} 失败: {e}")
        
        # 分析属性
        for prop_name, prop_obj in inspect.getmembers(cls, lambda x: isinstance(x, property)):
            class_info.properties[prop_name] = {
                'docstring': getattr(prop_obj, '__doc__', None),
                'has_getter': prop_obj.fget is not None,
                'has_setter': prop_obj.fset is not None,
                'has_deleter': prop_obj.fdel is not None
            }
        
        return class_info
    
    def _extract_parameters(self, signature: inspect.Signature) -> Dict[str, Dict[str, Any]]:
        """提取函数参数信息"""
        parameters = {}
        
        for param_name, param in signature.parameters.items():
            param_info = {
                'annotation': param.annotation if param.annotation != param.empty else None,
                'default': param.default if param.default != param.empty else None,
                'kind': param.kind.name,
                'has_default': param.default != param.empty
            }
            parameters[param_name] = param_info
            
        return parameters
    
    def _extract_decorators(self, func: Any) -> List[str]:
        """提取函数装饰器信息"""
        decorators = []
        
        # 这里可以通过AST分析获取更准确的装饰器信息
        # 目前只提供基础实现
        if hasattr(func, '__wrapped__'):
            decorators.append('wrapped')
            
        return decorators
    
    def _analyze_ast(self, file_path: str) -> Dict[str, Any]:
        """分析源代码的AST"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                source = f.read()
            
            tree = ast.parse(source)
            
            ast_info = {
                'imports': [],
                'functions': [],
                'classes': []
            }
            
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        ast_info['imports'].append({
                            'module': alias.name,
                            'alias': alias.asname,
                            'type': 'import'
                        })
                elif isinstance(node, ast.ImportFrom):
                    for alias in node.names:
                        ast_info['imports'].append({
                            'module': node.module,
                            'name': alias.name,
                            'alias': alias.asname,
                            'type': 'from_import'
                        })
                elif isinstance(node, ast.FunctionDef):
                    ast_info['functions'].append({
                        'name': node.name,
                        'line_number': node.lineno,
                        'decorators': [d.id if isinstance(d, ast.Name) else str(d) for d in node.decorator_list]
                    })
                elif isinstance(node, ast.ClassDef):
                    ast_info['classes'].append({
                        'name': node.name,
                        'line_number': node.lineno,
                        'base_classes': [base.id if isinstance(base, ast.Name) else str(base) for base in node.bases]
                    })
            
            return ast_info
            
        except Exception as e:
            logger.debug(f"AST分析失败: {e}")
            return {}
    
    def _analyze_dependencies(self, library_module: Any) -> List[str]:
        """分析库的依赖关系"""
        dependencies = []
        
        # 这里可以通过分析setup.py、requirements.txt等文件获取依赖信息
        # 目前提供基础实现
        if hasattr(library_module, '__file__'):
            try:
                module_dir = Path(library_module.__file__).parent
                requirements_files = [
                    'requirements.txt',
                    'requirements-dev.txt', 
                    'setup.py',
                    'pyproject.toml'
                ]
                
                for req_file in requirements_files:
                    req_path = module_dir / req_file
                    if req_path.exists():
                        # 简单的依赖提取，实际应该使用专门的解析器
                        logger.debug(f"发现依赖文件: {req_path}")
                        
            except Exception as e:
                logger.debug(f"分析依赖失败: {e}")
        
        return dependencies