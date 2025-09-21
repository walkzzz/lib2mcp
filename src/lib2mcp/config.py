"""
Configuration management system

配置管理系统，支持各种转换配置选项。
"""

import os
from pathlib import Path
from typing import Dict, List, Any, Optional, Union
from dataclasses import dataclass, field

try:
    import yaml  # type: ignore
    HAS_YAML = True
except ImportError:
    HAS_YAML = False
    yaml = None  # type: ignore

from .exceptions import ConfigurationError


@dataclass
class ConversionConfig:
    """转换配置"""
    include_patterns: List[str] = field(default_factory=lambda: ["*"])
    exclude_patterns: List[str] = field(default_factory=lambda: ["test_*", "*._*", "*.tests.*"])
    max_depth: int = 10
    enable_type_checking: bool = True
    preserve_docstrings: bool = True
    handle_exceptions: bool = True
    include_private: bool = False
    include_magic_methods: bool = False
    
    
@dataclass
class DescriptionConfig:
    """描述转换配置"""
    language: str = "auto"  # auto, zh, en
    docstring_style: str = "auto"  # auto, google, numpy, sphinx
    enhance_descriptions: bool = True
    generate_examples: bool = True
    max_description_length: int = 500
    include_type_hints: bool = True
    extract_parameter_docs: bool = True
    include_exceptions: bool = True
    translate_descriptions: bool = False
    
    
@dataclass  
class QueryConfig:
    """查询配置"""
    enable_tool_index: bool = True
    index_update_mode: str = "auto"  # auto, manual
    search_engine: str = "simple"  # simple, elasticsearch
    enable_semantic_search: bool = False
    default_page_size: int = 20
    max_search_results: int = 100
    enable_autocomplete: bool = True
    cache_query_results: bool = True
    cache_ttl: int = 3600  # seconds
    
    
@dataclass
class OutputConfig:
    """输出配置"""
    format: str = "json"  # json, yaml
    tool_prefix: str = ""
    group_by_module: bool = True
    generate_manifest: bool = True
    output_directory: str = "./output"
    create_subdirs: bool = True
    overwrite_existing: bool = False
    
    
@dataclass
class LoggingConfig:
    """日志配置"""
    level: str = "INFO"
    format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    file_path: Optional[str] = None
    max_file_size: int = 10 * 1024 * 1024  # 10MB
    backup_count: int = 5
    
    
@dataclass
class PerformanceConfig:
    """性能配置"""
    enable_caching: bool = True
    cache_directory: str = "./cache"
    max_cache_size: int = 100 * 1024 * 1024  # 100MB
    parallel_processing: bool = True
    max_workers: int = 4
    batch_size: int = 10
    memory_limit: int = 512 * 1024 * 1024  # 512MB


class Config:
    """主配置类"""
    
    def __init__(self, config_file: Optional[Union[str, Path]] = None, **kwargs):
        # 设置默认配置
        self.conversion = ConversionConfig()
        self.description = DescriptionConfig()
        self.query = QueryConfig()
        self.output = OutputConfig()
        self.logging = LoggingConfig()
        self.performance = PerformanceConfig()
        
        # 从配置文件加载
        if config_file:
            self.load_from_file(config_file)
            
        # 从环境变量加载
        self.load_from_env()
        
        # 应用传入的参数
        self.update(**kwargs)
    
    def load_from_file(self, config_file: Union[str, Path]) -> None:
        """从配置文件加载配置"""
        config_path = Path(config_file)
        
        if not config_path.exists():
            raise ConfigurationError(f"配置文件不存在: {config_path}")
            
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                if config_path.suffix.lower() in ['.yaml', '.yml']:
                    if not HAS_YAML:
                        raise ConfigurationError("YAML 支持需要安装 PyYAML: pip install PyYAML")
                    data = yaml.safe_load(f)  # type: ignore
                elif config_path.suffix.lower() == '.json':
                    import json
                    data = json.load(f)
                else:
                    raise ConfigurationError(f"不支持的配置文件格式: {config_path.suffix}")
            
            self._update_from_dict(data)
            
        except Exception as e:
            raise ConfigurationError(f"加载配置文件失败: {e}")
    
    def load_from_env(self) -> None:
        """从环境变量加载配置"""
        env_mapping = {
            # 转换配置
            'LIB2MCP_MAX_DEPTH': ('conversion', 'max_depth', int),
            'LIB2MCP_INCLUDE_PRIVATE': ('conversion', 'include_private', bool),
            'LIB2MCP_ENABLE_TYPE_CHECKING': ('conversion', 'enable_type_checking', bool),
            
            # 描述配置
            'LIB2MCP_DESCRIPTION_LANGUAGE': ('description', 'language', str),
            'LIB2MCP_ENHANCE_DESCRIPTIONS': ('description', 'enhance_descriptions', bool),
            'LIB2MCP_MAX_DESCRIPTION_LENGTH': ('description', 'max_description_length', int),
            
            # 查询配置
            'LIB2MCP_ENABLE_TOOL_INDEX': ('query', 'enable_tool_index', bool),
            'LIB2MCP_DEFAULT_PAGE_SIZE': ('query', 'default_page_size', int),
            'LIB2MCP_ENABLE_SEMANTIC_SEARCH': ('query', 'enable_semantic_search', bool),
            
            # 输出配置
            'LIB2MCP_OUTPUT_FORMAT': ('output', 'format', str),
            'LIB2MCP_OUTPUT_DIRECTORY': ('output', 'output_directory', str),
            'LIB2MCP_GROUP_BY_MODULE': ('output', 'group_by_module', bool),
            
            # 日志配置
            'LIB2MCP_LOG_LEVEL': ('logging', 'level', str),
            'LIB2MCP_LOG_FILE': ('logging', 'file_path', str),
            
            # 性能配置
            'LIB2MCP_ENABLE_CACHING': ('performance', 'enable_caching', bool),
            'LIB2MCP_MAX_WORKERS': ('performance', 'max_workers', int),
            'LIB2MCP_PARALLEL_PROCESSING': ('performance', 'parallel_processing', bool),
        }
        
        for env_var, (section, key, type_func) in env_mapping.items():
            value = os.getenv(env_var)
            if value is not None:
                try:
                    if type_func == bool:
                        # 处理布尔值
                        typed_value = value.lower() in ('true', '1', 'yes', 'on')
                    else:
                        typed_value = type_func(value)
                    
                    # 设置配置值
                    section_obj = getattr(self, section)
                    setattr(section_obj, key, typed_value)
                    
                except (ValueError, TypeError) as e:
                    raise ConfigurationError(f"环境变量 {env_var} 的值无效: {e}")
    
    def _update_from_dict(self, data: Dict[str, Any]) -> None:
        """从字典更新配置"""
        for section_name, section_data in data.items():
            if hasattr(self, section_name) and isinstance(section_data, dict):
                section_obj = getattr(self, section_name)
                for key, value in section_data.items():
                    if hasattr(section_obj, key):
                        setattr(section_obj, key, value)
    
    def update(self, **kwargs) -> None:
        """更新配置"""
        for key, value in kwargs.items():
            if '.' in key:
                # 支持嵌套键，如 'conversion.max_depth'
                section_name, attr_name = key.split('.', 1)
                if hasattr(self, section_name):
                    section_obj = getattr(self, section_name)
                    if hasattr(section_obj, attr_name):
                        setattr(section_obj, attr_name, value)
            else:
                # 直接设置属性
                if hasattr(self, key):
                    setattr(self, key, value)
    
    def to_dict(self) -> Dict[str, Any]:
        """转换为字典"""
        return {
            'conversion': self._dataclass_to_dict(self.conversion),
            'description': self._dataclass_to_dict(self.description),
            'query': self._dataclass_to_dict(self.query),
            'output': self._dataclass_to_dict(self.output),
            'logging': self._dataclass_to_dict(self.logging),
            'performance': self._dataclass_to_dict(self.performance),
        }
    
    def _dataclass_to_dict(self, obj) -> Dict[str, Any]:
        """将dataclass转换为字典"""
        result = {}
        for field_name in obj.__dataclass_fields__:
            result[field_name] = getattr(obj, field_name)
        return result
    
    def save_to_file(self, config_file: Union[str, Path]) -> None:
        """保存配置到文件"""
        config_path = Path(config_file)
        config_path.parent.mkdir(parents=True, exist_ok=True)
        
        data = self.to_dict()
        
        try:
            with open(config_path, 'w', encoding='utf-8') as f:
                if config_path.suffix.lower() in ['.yaml', '.yml']:
                    if not HAS_YAML:
                        raise ConfigurationError("YAML 支持需要安装 PyYAML: pip install PyYAML")
                    yaml.dump(data, f, default_flow_style=False, allow_unicode=True)  # type: ignore
                elif config_path.suffix.lower() == '.json':
                    import json
                    json.dump(data, f, indent=2, ensure_ascii=False)
                else:
                    raise ConfigurationError(f"不支持的配置文件格式: {config_path.suffix}")
                    
        except Exception as e:
            raise ConfigurationError(f"保存配置文件失败: {e}")
    
    def validate(self) -> None:
        """验证配置"""
        errors = []
        
        # 验证转换配置
        if self.conversion.max_depth < 1:
            errors.append("conversion.max_depth 必须大于 0")
            
        if not self.conversion.include_patterns:
            errors.append("conversion.include_patterns 不能为空")
        
        # 验证描述配置
        if self.description.language not in ['auto', 'zh', 'en']:
            errors.append("description.language 必须是 'auto', 'zh' 或 'en'")
            
        if self.description.max_description_length < 10:
            errors.append("description.max_description_length 必须大于等于 10")
        
        # 验证查询配置
        if self.query.default_page_size < 1:
            errors.append("query.default_page_size 必须大于 0")
            
        if self.query.max_search_results < 1:
            errors.append("query.max_search_results 必须大于 0")
        
        # 验证输出配置
        if self.output.format not in ['json', 'yaml']:
            errors.append("output.format 必须是 'json' 或 'yaml'")
        
        # 验证性能配置
        if self.performance.max_workers < 1:
            errors.append("performance.max_workers 必须大于 0")
            
        if self.performance.batch_size < 1:
            errors.append("performance.batch_size 必须大于 0")
        
        if errors:
            raise ConfigurationError("配置验证失败:\n" + "\n".join(f"- {error}" for error in errors))
    
    def get_cache_dir(self) -> Path:
        """获取缓存目录"""
        cache_dir = Path(self.performance.cache_directory)
        cache_dir.mkdir(parents=True, exist_ok=True)
        return cache_dir
    
    def get_output_dir(self) -> Path:
        """获取输出目录"""
        output_dir = Path(self.output.output_directory)
        if self.output.create_subdirs:
            output_dir.mkdir(parents=True, exist_ok=True)
        return output_dir
    
    def setup_logging(self) -> None:
        """设置日志配置"""
        import logging
        import logging.handlers
        
        # 设置日志级别
        level = getattr(logging, self.logging.level.upper(), logging.INFO)
        logging.basicConfig(level=level, format=self.logging.format)
        
        # 设置文件日志
        if self.logging.file_path:
            log_file = Path(self.logging.file_path)
            log_file.parent.mkdir(parents=True, exist_ok=True)
            
            handler = logging.handlers.RotatingFileHandler(
                log_file,
                maxBytes=self.logging.max_file_size,
                backupCount=self.logging.backup_count,
                encoding='utf-8'
            )
            handler.setFormatter(logging.Formatter(self.logging.format))
            logging.getLogger().addHandler(handler)
    
    # 便利属性，用于向后兼容
    @property
    def include_patterns(self) -> List[str]:
        return self.conversion.include_patterns
    
    @property 
    def exclude_patterns(self) -> List[str]:
        return self.conversion.exclude_patterns
    
    @property
    def max_depth(self) -> int:
        return self.conversion.max_depth
    
    @property
    def enable_type_checking(self) -> bool:
        return self.conversion.enable_type_checking
    
    @property
    def include_private(self) -> bool:
        return self.conversion.include_private


def load_config(config_file: Optional[Union[str, Path]] = None, **kwargs) -> Config:
    """加载配置的便利函数"""
    return Config(config_file, **kwargs)


def create_default_config_file(output_path: Union[str, Path]) -> None:
    """创建默认配置文件"""
    config = Config()
    config.save_to_file(output_path)