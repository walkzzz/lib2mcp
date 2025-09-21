#!/usr/bin/env python3
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

try:
    import click  # type: ignore
except ImportError:
    print("错误: 需要安装 click 库，请运行: pip install click")
    sys.exit(1)

# 设置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
            arguments = params.get("arguments", {{}})
            
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
def main(library_name: str, output_dir: str, tools_only: bool):
    """
    自动生成 MCP 工具链
    
    LIBRARY_NAME: 要转换的 Python 库名称
    """
    # 如果没有指定输出目录，则使用库名作为默认目录
    if not output_dir:
        output_dir = f"{library_name}_mcp"
    
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
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