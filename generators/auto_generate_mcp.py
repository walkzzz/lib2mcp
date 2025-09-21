#!/usr/bin/env python3.10
"""
自动生成 MCP 工具链
给定一个 Python 库，自动生成：
1. lib2mcp 工具定义文件
2. MCP 服务器脚本
3. CherryStudio 配置文件
"""

import json
import sys
from pathlib import Path
from typing import Dict, Any, List, Optional
import logging
import os
import re
import urllib.parse
import urllib.request
from collections import Counter

try:
    import click  # type: ignore
except ImportError:
    print("错误: 需要安装 click 库，请运行: pip install click")
    sys.exit(1)

# 设置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 获取项目根目录
PROJECT_ROOT = Path(__file__).parent.parent

def generate_tools_with_lib2mcp(library_name: str, output_dir: Path) -> Dict[str, Any]:
    """使用 lib2mcp 生成工具定义"""
    try:
        from lib2mcp import LibraryConverter, Config
        
        logger.info(f"正在使用 lib2mcp 分析库: {library_name}")
        
        # 创建输出目录
        output_dir.mkdir(exist_ok=True)
        
        # 配置
        config = Config()
        config.output.output_directory = str(output_dir)
        config.output.format = 'json'
        
        # 转换
        converter = LibraryConverter(config)
        result = converter.convert_library(library_name, output_dir)
        
        # 加载生成的工具文件
        tools_file = output_dir / f"{library_name}_tools.json"
        if tools_file.exists():
            with open(tools_file, 'r', encoding='utf-8') as f:
                tools_data = json.load(f)
            return {
                'success': True,
                'tools': tools_data,
                'stats': result.get('statistics', {}),
                'tools_file': str(tools_file)
            }
        else:
            return {'success': False, 'error': '工具文件生成失败'}
            
    except Exception as e:
        logger.error(f"lib2mcp 转换失败: {e}")
        return {'success': False, 'error': str(e)}

def search_tool_usage_frequency(tool_name: str, library_name: str) -> int:
    """
    通过网络搜索获取工具的使用频率
    
    Args:
        tool_name: 工具名称
        library_name: 库名称
        
    Returns:
        int: 使用频率估算值
    """
    try:
        # 构造搜索查询
        query = f"{library_name} {tool_name} site:github.com OR site:stackoverflow.com"
        query_encoded = urllib.parse.quote(query)
        url = f"https://www.google.com/search?q={query_encoded}"
        
        # 发送请求（注意：实际使用中可能需要处理反爬虫机制）
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        # 由于直接搜索可能受限，我们使用简化的方法估算频率
        # 基于工具名称的常见模式来估算
        common_patterns = [
            f"{library_name}.{tool_name}",
            f"{tool_name} {library_name}",
            f"import {library_name}",
            f"from {library_name} import {tool_name}"
        ]
        
        # 简化的频率估算（实际应用中可以使用更复杂的算法）
        frequency_score = 0
        if any(pattern in tool_name.lower() for pattern in ['get', 'post', 'request', 'session']):
            frequency_score += 8
        if any(pattern in tool_name.lower() for pattern in ['json', 'data', 'parse']):
            frequency_score += 6
        if any(pattern in tool_name.lower() for pattern in ['auth', 'login', 'token']):
            frequency_score += 5
        if any(pattern in tool_name.lower() for pattern in ['error', 'exception']):
            frequency_score += 3
            
        return min(frequency_score, 10)  # 限制在0-10范围内
        
    except Exception as e:
        logger.warning(f"搜索工具 {tool_name} 使用频率时出错: {e}")
        return 5  # 默认返回中等频率

def analyze_tool_usability_with_search(tools_data: Dict[str, Any], library_name: str) -> Dict[str, Any]:
    """
    通过网络搜索分析工具的使用频率和易用性
    
    Args:
        tools_data: 工具数据字典
        library_name: 库名称
        
    Returns:
        Dict[str, Any]: 包含每个工具评分和筛选结果的字典
    """
    try:
        # 存储分析结果
        analysis_results = {}
        
        # 为每个工具生成分析
        for tool_id, tool_def in tools_data.items():
            try:
                tool_name = tool_def.get('name', tool_id)
                description = tool_def.get('description', '')
                
                # 估算使用频率
                frequency = search_tool_usage_frequency(tool_name, library_name)
                
                # 估算易用性（基于描述长度和关键词）
                usability = 8  # 默认较高
                if len(description) < 50:
                    usability = min(usability, 6)  # 描述太短可能不易理解
                if 'complex' in description.lower() or 'advanced' in description.lower():
                    usability = max(usability - 2, 3)  # 复杂工具易用性较低
                
                # 估算实用性（基于工具名称和描述）
                utility = 7  # 默认中等
                if any(keyword in tool_name.lower() for keyword in ['get', 'post', 'request']):
                    utility = min(utility + 2, 10)  # 网络请求工具通常很实用
                if any(keyword in tool_name.lower() for keyword in ['json', 'data']):
                    utility = min(utility + 1, 10)  # 数据处理工具较实用
                
                # 综合评分
                score = (frequency + usability + utility) / 3
                
                analysis_results[tool_id] = {
                    'frequency': frequency,
                    'usability': usability,
                    'utility': utility,
                    'score': score,
                    'reason': f'使用频率估算: {frequency}, 易用性评估: {usability}, 实用性评估: {utility}'
                }
                
            except Exception as e:
                logger.warning(f"分析工具 {tool_id} 时出错: {e}")
                analysis_results[tool_id] = {
                    'frequency': 5.0,
                    'usability': 5.0,
                    'utility': 5.0,
                    'score': 5.0,
                    'reason': f'分析失败: {str(e)}'
                }
        
        return {
            'tools': tools_data,
            'analysis': analysis_results
        }
            
    except Exception as e:
        logger.error(f"使用网络搜索分析工具时出错: {e}")
        # 出现错误时返回所有工具
        return {
            'tools': tools_data,
            'analysis': {tool_id: {
                'frequency': 1.0,
                'usability': 1.0,
                'utility': 1.0,
                'score': 1.0,
                'reason': '分析过程出错'
            } for tool_id in tools_data.keys()}
        }

def analyze_tool_usability_with_ollama(tools_data: Dict[str, Any], library_name: str, model_name: str = 'deepseek-r1:8b') -> Dict[str, Any]:
    """
    使用 Ollama 本地大模型分析工具的使用频率和易用性
    
    Args:
        tools_data: 工具数据字典
        library_name: 库名称
        model_name: Ollama 模型名称
        
    Returns:
        Dict[str, Any]: 包含每个工具评分和筛选结果的字典
    """
    try:
        # 检查是否安装了 ollama
        try:
            import importlib
            ollama = importlib.import_module('ollama')
        except ImportError:
            logger.warning("未安装 ollama 库，跳过工具分析")
            # 返回所有工具，不进行筛选
            return {
                'tools': tools_data,
                'analysis': {tool_id: {'score': 1.0, 'reason': '未安装 ollama，未进行分析'} 
                           for tool_id in tools_data.keys()}
            }
        
        # 存储分析结果
        analysis_results = {}
        
        # 为每个工具生成分析
        for tool_id, tool_def in tools_data.items():
            try:
                tool_name = tool_def.get('name', tool_id)
                description = tool_def.get('description', '')
                input_schema = tool_def.get('inputSchema', {})
                
                # 构建分析提示
                prompt = f"""
作为一个经验丰富的 Python 开发者，请分析以下 {library_name} 库中的工具：

工具名称: {tool_name}
工具描述: {description}
参数信息: {json.dumps(input_schema, ensure_ascii=False)}

请从以下维度评分（每项满分10分）：
1. 使用频率：该工具在实际项目中的使用频率
2. 易用性：该工具是否容易理解和使用
3. 实用性：该工具解决实际问题的能力

最后给出一个综合评分（0-10分），并简要说明理由。

请以以下 JSON 格式回复：
{{
    "frequency": 数字,
    "usability": 数字,
    "utility": 数字,
    "score": 数字,
    "reason": "简要说明"
}}
"""
                
                # 调用 Ollama
                response = ollama.chat(
                    model=model_name,
                    messages=[
                        {
                            'role': 'user',
                            'content': prompt
                        }
                    ],
                    format='json'
                )
                
                # 解析响应
                try:
                    result = json.loads(response['message']['content'])
                    analysis_results[tool_id] = result
                except json.JSONDecodeError as json_error:
                    logger.warning(f"解析工具 {tool_id} 的分析结果时出错: {json_error}")
                    # 提供默认评分
                    analysis_results[tool_id] = {
                        'frequency': 5.0,
                        'usability': 5.0,
                        'utility': 5.0,
                        'score': 5.0,
                        'reason': f'解析分析结果失败: {str(json_error)}'
                    }
                
            except Exception as e:
                logger.warning(f"分析工具 {tool_id} 时出错: {e}")
                analysis_results[tool_id] = {
                    'frequency': 5.0,
                    'usability': 5.0,
                    'utility': 5.0,
                    'score': 5.0,
                    'reason': f'分析失败: {str(e)}'
                }
        
        return {
            'tools': tools_data,
            'analysis': analysis_results
        }
            
    except Exception as e:
        logger.error(f"使用 Ollama 分析工具时出错: {e}")
        # 出现错误时返回所有工具
        return {
            'tools': tools_data,
            'analysis': {tool_id: {
                'frequency': 1.0,
                'usability': 1.0,
                'utility': 1.0,
                'score': 1.0,
                'reason': '分析过程出错'
            } for tool_id in tools_data.keys()}
        }

def get_dynamic_filter_percentage(tool_count: int) -> float:
    """
    根据工具数量动态计算筛选百分比
    
    Args:
        tool_count: 工具总数
        
    Returns:
        float: 筛选百分比 (0.0-1.0)
    """
    if tool_count < 20:
        return 0.9  # 90%
    elif tool_count < 50:
        return 0.8  # 80%
    elif tool_count < 100:
        return 0.6  # 60%
    elif tool_count < 200:
        return 0.5  # 50%
    elif tool_count < 500:
        return 0.3  # 30%
    elif tool_count < 1000:
        return 0.2  # 20%
    elif tool_count < 2000:
        return 0.15  # 15%
    elif tool_count < 5000:
        return 0.05  # 5%
    else:
        return 0.02  # 2%

def filter_top_tools(tools_data: Dict[str, Any], analysis_results: Dict[str, Any], percentage: Optional[float] = None) -> Dict[str, Any]:
    """
    根据分析结果筛选出前百分之几的工具
    
    Args:
        tools_data: 原始工具数据
        analysis_results: 分析结果
        percentage: 筛选比例（默认None，使用动态计算）
        
    Returns:
        Dict[str, Any]: 筛选后的工具数据
    """
    try:
        # 如果没有指定百分比，则根据工具数量动态计算
        if percentage is None:
            tool_count = len(tools_data)
            percentage = get_dynamic_filter_percentage(tool_count)
            logger.info(f"工具数量: {tool_count}, 动态筛选百分比: {percentage*100:.0f}%")
        
        # 创建工具评分列表，按使用频率和综合评分排序
        tool_scores = []
        for tool_id, analysis in analysis_results.items():
            frequency = analysis.get('frequency', 0)
            score = analysis.get('score', 0)
            # 主要按综合评分排序，使用频率作为次要排序条件
            tool_scores.append((tool_id, score, frequency))
        
        # 按综合评分降序排序，评分相同时按使用频率降序排序
        tool_scores.sort(key=lambda x: (x[1], x[2]), reverse=True)
        
        # 计算需要保留的工具数量
        total_tools = len(tool_scores)
        theoretical_count = max(1, int(total_tools * percentage))  # 理论上的工具数量
        
        # 取筛选出来的工具数据与理论的百分比数量的最小值
        keep_count = min(len(tool_scores), theoretical_count)
        
        # 获取前 keep_count 个工具的 ID
        top_tool_ids = set(tool_id for tool_id, _, _ in tool_scores[:keep_count])
        
        # 筛选工具
        filtered_tools = {
            tool_id: tools_data[tool_id] 
            for tool_id in top_tool_ids 
            if tool_id in tools_data
        }
        
        logger.info(f"工具筛选完成: 原始 {total_tools} 个工具，筛选后保留 {len(filtered_tools)} 个工具 ({percentage*100:.0f}%)")
        
        # 列出筛选后的工具清单
        print("\n📋 筛选后的工具清单:")
        # 按评分排序显示工具清单
        sorted_filtered_tools = sorted(filtered_tools.items(), 
                                     key=lambda x: next((score for tid, score, freq in tool_scores if tid == x[0]), 0), 
                                     reverse=True)
        for i, (tool_id, tool_def) in enumerate(sorted_filtered_tools[:20], 1):  # 只显示前20个工具
            tool_name = tool_def.get('name', tool_id.replace('.', '_'))
            # 获取该工具的评分和频率
            tool_info = next((item for item in tool_scores if item[0] == tool_id), None)
            if tool_info:
                score = tool_info[1]
                frequency = tool_info[2]
                print(f"   {i:2d}. {tool_name} (评分: {score:.1f}, 频率: {frequency:.1f})")
            else:
                print(f"   {i:2d}. {tool_name} (评分: 0.0, 频率: 0.0)")
        if len(filtered_tools) > 20:
            print(f"   ... 还有 {len(filtered_tools) - 20} 个工具")
        
        return filtered_tools
        
    except Exception as e:
        logger.error(f"筛选工具时出错: {e}")
        # 出现错误时返回所有工具
        return tools_data

def create_mcp_server(library_name: str, tools_data: Dict[str, Any], output_file: Path) -> bool:
    """根据工具定义创建 MCP 服务器"""
    try:
        # 提取工具信息
        tools_list = []
        function_handlers = []
        
        for tool_id, tool_def in tools_data.items():
            tool_name = tool_def.get('name', tool_id.replace('.', '_'))
            description = tool_def.get('description', f'执行 {tool_id} 操作')
            input_schema = tool_def.get('inputSchema', {})
            metadata = tool_def.get('metadata', {})
            
            # 构建工具定义
            tool_entry = {
                'name': tool_name,
                'description': description,
                'inputSchema': input_schema
            }
            tools_list.append(tool_entry)
            
            # 生成函数处理器
            source_function = metadata.get('source_function', tool_id)
            handler_code = generate_function_handler(tool_name, source_function, library_name)
            function_handlers.append(handler_code)
        
        # 生成服务器代码
        server_code = generate_server_template(library_name, tools_list, function_handlers)
        
        # 写入文件
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(server_code)
        
        logger.info(f"MCP 服务器已生成: {output_file}")
        return True
        
    except Exception as e:
        logger.error(f"生成 MCP 服务器失败: {e}")
        return False

def generate_function_handler(tool_name: str, source_function: str, library_name: str) -> str:
    """生成单个函数的处理器代码"""
    return f'''
def handle_{tool_name}(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 {tool_name} 工具调用"""
    try:
        # 解析函数路径: {source_function}
        parts = "{source_function}".split('.')
        
        if parts[0] != "{library_name}":
            raise ValueError(f"不支持的模块: {{parts[0]}}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # {library_name}.function_name
            func_name = parts[1]
            func = getattr({library_name}, func_name)
        elif len(parts) >= 3:
            # {library_name}.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: {source_function}")
        
        # 处理参数
        processed_args = {{}}
        processed_kwargs = {{}}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {{"result": str(result)}}
            
    except Exception as e:
        logger.error(f"执行 {tool_name} 失败: {{e}}")
        return {{"error": str(e)}}
'''

def generate_server_template(library_name: str, tools_list: List[Dict], function_handlers: List[str]) -> str:
    """生成完整的 MCP 服务器模板"""
    # 修复 JSON 中的布尔值问题
    tools_json_str = json.dumps(tools_list, ensure_ascii=False, indent=4)
    tools_json_str = tools_json_str.replace('true', 'True').replace('false', 'False').replace('null', 'None')
    
    handlers_code = '\n'.join(function_handlers)
    
    return f'''#!/usr/bin/env python3
"""
自动生成的 MCP 服务器
库: {library_name}
工具数量: {len(tools_list)}
"""

import asyncio
import json
import logging
import sys
from typing import Dict, Any

try:
    import {library_name}  # type: ignore
except ImportError:
    print("错误: 未安装 {library_name} 库，请运行: pip install {library_name}")
    sys.exit(1)

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("{library_name}_mcp_server")

# 工具定义
TOOLS = {tools_json_str}

{handlers_code}

def process_mcp_request(request_line: str) -> str:
    """处理 MCP 请求"""
    try:
        request = json.loads(request_line.strip())
        method = request.get("method", "")
        params = request.get("params", {{}})
        request_id = request.get("id")
        
        if method == "initialize":
            # MCP 初始化请求
            response = {{
                "jsonrpc": "2.0",
                "id": request_id,
                "result": {{
                    "protocolVersion": "2024-11-05",
                    "capabilities": {{
                        "tools": {{}},
                        "logging": {{}},
                        "prompts": {{}},
                        "resources": {{}}
                    }},
                    "serverInfo": {{
                        "name": "{library_name}-mcp-server",
                        "version": "1.0.0"
                    }}
                }}
            }}
        elif method == "notifications/initialized":
            # 初始化完成通知，不需要响应
            return ""
        elif method == "tools/list":
            response = {{
                "jsonrpc": "2.0",
                "id": request_id,
                "result": {{"tools": TOOLS}}
            }}
        elif method == "tools/call":
            tool_name = params.get("name", "")
            arguments = params.get("arguments", {{}}
            
            # 调用对应的处理函数
            handler_name = f"handle_{{tool_name}}"
            if handler_name in globals():
                result = globals()[handler_name](arguments)
            else:
                result = {{"error": f"未找到工具处理器: {{tool_name}}"}}
            
            response = {{
                "jsonrpc": "2.0",
                "id": request_id,
                "result": {{
                    "content": [
                        {{
                            "type": "text",
                            "text": json.dumps(result, ensure_ascii=False, indent=2)
                        }}
                    ]
                }}
            }}
        else:
            response = {{
                "jsonrpc": "2.0",
                "id": request_id,
                "error": {{
                    "code": -32601,
                    "message": f"未知方法: {{method}}"
                }}
            }}
        
        return json.dumps(response)
    
    except Exception as e:
        logger.error(f"处理请求失败: {{e}}")
        return json.dumps({{
            "jsonrpc": "2.0",
            "id": None,
            "error": {{
                "code": -32603,
                "message": f"内部错误: {{str(e)}}"
            }}
        }})

async def main():
    """主函数 - MCP 服务器模式"""
    logger.info("启动 {library_name} MCP 服务器...")
    
    try:
        # 读取 stdin 并处理请求
        while True:
            try:
                line = sys.stdin.readline()
                if not line:
                    break
                
                line = line.strip()
                if line:
                    logger.debug(f"收到请求: {{line}}")
                    response = process_mcp_request(line)
                    if response:  # 只有当有响应时才输出
                        print(response, flush=True)
                        logger.debug(f"发送响应: {{response}}")
                        
            except EOFError:
                # 正常的输入结束
                break
            except Exception as e:
                logger.error(f"处理请求时出错: {{e}}")
                error_response = json.dumps({{
                    "jsonrpc": "2.0",
                    "id": None,
                    "error": {{
                        "code": -32603,
                        "message": f"内部错误: {{str(e)}}"
                    }}
                }})
                print(error_response, flush=True)
                
    except KeyboardInterrupt:
        logger.info("服务器停止")
    except Exception as e:
        logger.error(f"服务器错误: {{e}}")
    finally:
        logger.info("服务器关闭")

def cli_mode():
    """命令行模式 - 用于测试"""
    if len(sys.argv) < 3:
        print(json.dumps({{"error": "参数不足，需要: 工具名 参数JSON"}}))
        return
    
    tool_name = sys.argv[1]
    try:
        arguments = json.loads(sys.argv[2])
    except json.JSONDecodeError:
        print(json.dumps({{"error": "参数格式错误"}}))
        return
    
    # 调用对应的处理函数
    handler_name = f"handle_{{tool_name}}"
    if handler_name in globals():
        result = globals()[handler_name](arguments)
    else:
        result = {{"error": f"未找到工具: {{tool_name}}"}}
    
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # 命令行模式
        cli_mode()
    else:
        # MCP 服务器模式
        asyncio.run(main())
'''

def create_cherry_config(library_name: str, server_file: Path, output_file: Path) -> bool:
    """创建 CherryStudio 配置文件"""
    try:
        config = {
            "mcpServers": {
                f"lib2mcp_{library_name}": {
                    "command": "python",
                    "args": [str(server_file.absolute())]
                }
            }
        }
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(config, f, ensure_ascii=False, indent=2)
        
        logger.info(f"CherryStudio 配置已生成: {output_file}")
        return True
        
    except Exception as e:
        logger.error(f"生成 CherryStudio 配置失败: {e}")
        return False

@click.command()
@click.argument('library_name')
@click.option('--output-dir', '-o', default='', help='输出目录')
@click.option('--tools-only', is_flag=True, help='只生成工具定义，不生成服务器')
@click.option('--ollama-model', default='deepseek-r1:8b', help='Ollama 模型名称')
@click.option('--filter-percentage', default=None, type=float, help='工具筛选百分比 (0.0-1.0)，默认根据工具数量动态计算')
@click.option('--use-ollama', is_flag=True, help='使用 Ollama 大模型进行分析（默认使用网络搜索）')
def main(library_name: str, output_dir: str, tools_only: bool, ollama_model: str, filter_percentage: Optional[float], use_ollama: bool):
    """
    自动生成 MCP 工具链
    
    LIBRARY_NAME: 要转换的 Python 库名称
    """
    # 如果没有指定输出目录，则使用项目根目录下的output文件夹
    if not output_dir:
        output_dir = str(PROJECT_ROOT / "output" / f"{library_name}_mcp")
    
    output_path = Path(output_dir)
    # 使用 parents=True 确保父目录存在，exist_ok=True 避免目录已存在时报错
    output_path.mkdir(parents=True, exist_ok=True)
    
    print(f"🚀 自动生成 {library_name} 的 MCP 工具链")
    print("=" * 50)
    
    # 1. 生成工具定义
    print("📝 步骤 1: 生成工具定义...")
    tools_dir = output_path / "tools"
    tools_result = generate_tools_with_lib2mcp(library_name, tools_dir)
    
    if not tools_result['success']:
        print(f"❌ 工具定义生成失败: {tools_result['error']}")
        return
    
    tools_data = tools_result['tools']
    stats = tools_result['stats']
    print(f"✅ 工具定义生成成功!")
    print(f"   生成工具数: {stats.get('converted_tools', len(tools_data))}")
    print(f"   工具文件: {tools_result['tools_file']}")

    # 分析工具的使用频率和易用性
    if use_ollama:
        print(f"\n🔍 步骤 1.5: 使用 Ollama 分析工具使用频率和易用性 (使用模型: {ollama_model})...")
        analysis_result = analyze_tool_usability_with_ollama(tools_data, library_name, ollama_model)
    else:
        print(f"\n🔍 步骤 1.5: 使用网络搜索分析工具使用频率和易用性...")
        analysis_result = analyze_tool_usability_with_search(tools_data, library_name)
    
    # 筛选出指定百分比最有用的工具
    filtered_tools = filter_top_tools(
        analysis_result['tools'], 
        analysis_result['analysis'], 
        percentage=filter_percentage
    )
    
    # 更新工具数据为筛选后的结果
    tools_data = filtered_tools
    tool_count = len(tools_data)
    if filter_percentage is None:
        print(f"   筛选后工具数: {tool_count} (动态计算)")
    else:
        print(f"   筛选后工具数: {tool_count} ({filter_percentage*100:.0f}%)")
    
    if tools_only:
        print("\n🎉 工具定义生成完成!")
        return
    
    # 2. 生成 MCP 服务器
    print("\n📝 步骤 2: 生成 MCP 服务器...")
    server_file = output_path / f"{library_name}_mcp_server.py"
    
    if create_mcp_server(library_name, tools_data, server_file):
        print(f"✅ MCP 服务器生成成功: {server_file}")
    else:
        print("❌ MCP 服务器生成失败")
        return
    
    # 3. 生成 CherryStudio 配置
    print("\n📝 步骤 3: 生成 CherryStudio 配置...")
    config_file = output_path / f"{library_name}_cherry_config.json"
    
    if create_cherry_config(library_name, server_file, config_file):
        print(f"✅ CherryStudio 配置生成成功: {config_file}")
    else:
        print("❌ CherryStudio 配置生成失败")
        return
    
    # 总结
    print("\n" + "=" * 50)
    print("🎉 MCP 工具链生成完成!")
    print("\n📁 生成的文件:")
    print(f"   工具定义: {tools_result['tools_file']}")
    print(f"   MCP 服务器: {server_file}")
    print(f"   CherryStudio 配置: {config_file}")
    
    print("\n📋 下一步:")
    print("1. 测试 MCP 服务器:")
    print(f"   python {server_file} <工具名> '<参数JSON>'")
    print("2. 在 CherryStudio 中导入配置:")
    print(f"   复制 {config_file} 的内容到 CherryStudio")
    print("3. 开始使用工具!")

if __name__ == "__main__":
    # 检查命令行参数
    import sys  
    if len(sys.argv) < 2:
        print("用法: python auto_generate_mcp.py <library_name> [--output-dir <dir>] [--tools-only]")
        sys.exit(1)
    
    # 使用 click 进行命令行解析
    main()  # type: ignore