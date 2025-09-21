"""
Main Library Converter

主要的库转换器，协调各个组件完成转换工作。
"""

from typing import Dict, List, Any, Optional, Union
from pathlib import Path
import logging

from .exceptions import ConversionError
from .config import Config
from .core import (
    LibraryAnalyzer, APIExtractor, TypeInferenceEngine, 
    DescriptionConverter, MCPToolGenerator, ToolValidator
)
from .models import LibraryMetadata, APIFunction

logger = logging.getLogger(__name__)


class LibraryConverter:
    """
    主库转换器 - 协调整个转换流程
    
    转换流程：
    1. 分析库结构
    2. 提取API信息
    3. 推断类型信息
    4. 转换描述信息
    5. 生成MCP工具
    6. 验证工具定义
    """
    
    def __init__(self, config: Optional[Config] = None):
        self.config = config or Config()
        
        # 初始化各个组件
        self.analyzer = LibraryAnalyzer(self.config)
        self.api_extractor = APIExtractor(self.config)
        self.type_engine = TypeInferenceEngine(self.config)
        self.desc_converter = DescriptionConverter(self.config)
        self.mcp_generator = MCPToolGenerator(self.config)
        self.validator = ToolValidator(self.config)
        
    def convert_library(self, library_name: str, 
                       output_path: Optional[Union[str, Path]] = None) -> Dict[str, Any]:
        """
        转换指定的Python库
        
        Args:
            library_name: 库名称
            output_path: 输出路径（可选）
            
        Returns:
            Dict[str, Any]: 转换结果，包含工具定义和统计信息
        """
        try:
            logger.info(f"开始转换库: {library_name}")
            
            # 1. 分析库结构
            logger.info("步骤1: 分析库结构")
            library_metadata = self.analyzer.analyze_library(library_name)
            
            # 2. 提取API信息
            logger.info("步骤2: 提取API信息")
            apis = self.api_extractor.extract_apis(library_metadata)
            
            # 3. 生成工具定义
            logger.info("步骤3: 生成MCP工具")
            tools = {}
            for api_key, api_func in apis.items():
                try:
                    tool = self._convert_api_to_tool(api_func)
                    tools[api_key] = tool
                except Exception as e:
                    logger.warning(f"转换API {api_key} 失败: {e}")
                    continue
            
            # 4. 验证工具
            logger.info("步骤4: 验证工具定义")
            validated_tools = {}
            validation_results = []
            
            for tool_key, tool in tools.items():
                validation_result = self.validator.validate_tool(tool)
                validation_results.append(validation_result)
                
                if validation_result.get('valid', False):
                    validated_tools[tool_key] = tool
                else:
                    logger.warning(f"工具 {tool_key} 验证失败: {validation_result.get('errors', [])}")
            
            # 5. 生成输出
            result = {
                'library_name': library_name,
                'library_metadata': library_metadata,
                'tools': validated_tools,
                'statistics': {
                    'total_apis': len(apis),
                    'converted_tools': len(tools),
                    'validated_tools': len(validated_tools),
                    'validation_failures': len(tools) - len(validated_tools)
                },
                'validation_results': validation_results
            }
            
            # 6. 保存到文件（如果指定了输出路径）
            if output_path:
                self._save_result(result, output_path)
            
            logger.info(f"库转换完成: {library_name}, 生成工具数: {len(validated_tools)}")
            return result
            
        except Exception as e:
            raise ConversionError(f"转换库 {library_name} 失败: {str(e)}")
    
    def _convert_api_to_tool(self, api_func: APIFunction) -> Dict[str, Any]:
        """将API函数转换为MCP工具"""
        # 推断类型信息
        parameter_types = self.type_engine.infer_parameter_types(api_func)
        return_type = self.type_engine.infer_return_type(api_func)
        
        # 转换描述信息
        description_data = self.desc_converter.convert_function_description(api_func)
        
        # 生成MCP工具定义
        tool = self.mcp_generator.generate_tool(
            api_func, parameter_types, return_type, description_data
        )
        
        return tool
    
    def _save_result(self, result: Dict[str, Any], output_path: Union[str, Path]) -> None:
        """保存转换结果"""
        output_dir = Path(output_path)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        library_name = result['library_name']
        
        # 保存工具定义
        tools_file = output_dir / f"{library_name}_tools.json"
        self._save_json(result['tools'], tools_file)
        
        # 保存统计信息
        stats_file = output_dir / f"{library_name}_stats.json"
        self._save_json(result['statistics'], stats_file)
        
        # 保存清单文件
        manifest = {
            'library_name': library_name,
            'tools_file': str(tools_file),
            'statistics_file': str(stats_file),
            'tool_count': len(result['tools']),
            'generated_at': self._get_timestamp()
        }
        manifest_file = output_dir / f"{library_name}_manifest.json"
        self._save_json(manifest, manifest_file)
        
        logger.info(f"转换结果已保存到: {output_dir}")
    
    def _save_json(self, data: Any, file_path: Path) -> None:
        """保存JSON文件"""
        import json
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False, default=str)
    
    def _get_timestamp(self) -> str:
        """获取时间戳"""
        from datetime import datetime
        return datetime.now().isoformat()
    
    def convert_multiple_libraries(self, library_names: List[str], 
                                 output_path: Optional[Union[str, Path]] = None) -> Dict[str, Any]:
        """批量转换多个库"""
        results = {}
        errors = {}
        
        for library_name in library_names:
            try:
                result = self.convert_library(library_name, output_path)
                results[library_name] = result
            except Exception as e:
                logger.error(f"转换库 {library_name} 失败: {e}")
                errors[library_name] = str(e)
        
        return {
            'successful_conversions': results,
            'failed_conversions': errors,
            'summary': {
                'total_libraries': len(library_names),
                'successful_count': len(results),
                'failed_count': len(errors),
                'total_tools': sum(len(r['tools']) for r in results.values())
            }
        }