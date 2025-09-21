#!/usr/bin/env python3
"""
自动生成的 MCP 服务器
库: os
工具数量: 7
"""

import asyncio
import json
import logging
import sys
from typing import Dict, Any

try:
    import os  # type: ignore
except ImportError:
    print("错误: 未安装 os 库，请运行: pip install os")
    sys.exit(1)

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("os_mcp_server")

# 工具定义
TOOLS = [
    {
        "name": "os_getenv",
        "description": "Get an environment variable, return None if it doesn't exist.\nThe optional second argument can specify an alternate default.\nkey, default and the result are str.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "key": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "default": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "key"
            ]
        }
    },
    {
        "name": "os_execlpe",
        "description": "execlpe(file, *args, env)\nExecute the executable file (which is searched for along $PATH)\nwith argument list args and environment env, replacing the current\nprocess.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "file": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "args": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "file",
                "args"
            ]
        }
    },
    {
        "name": "os_get_exec_path",
        "description": "Returns the sequence of directories that will be searched for the\nnamed executable (similar to a shell) when launching a process.\n*env* must be an environment variable dict or None.  If *env* is None,\nos.environ will be used.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "env": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": []
        }
    },
    {
        "name": "os_execle",
        "description": "execle(file, *args, env)\nExecute the executable file with argument list args and\nenvironment env, replacing the current process.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "file": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "args": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "file",
                "args"
            ]
        }
    },
    {
        "name": "os_add_dll_directory",
        "description": "Add a path to the DLL search path.\nThis search path is used when resolving dependencies for imported\nextension modules (the module itself is resolved through sys.path),\nand also by ctypes.\nRemove the directory by calling close() on the returned object or\nusing it in a with statement.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "path"
            ]
        }
    },
    {
        "name": "os_execlp",
        "description": "execlp(file, *args)\nExecute the executable file (which is searched for along $PATH)\nwith argument list args, replacing the current process.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "file": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "args": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "file",
                "args"
            ]
        }
    },
    {
        "name": "os_execl",
        "description": "execl(file, *args)\nExecute the executable file with argument list args, replacing the\ncurrent process.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "file": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "args": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "file",
                "args"
            ]
        }
    }
]


def handle_os_getenv(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 os_getenv 工具调用"""
    try:
        # 解析函数路径: os.getenv
        parts = "os.getenv".split('.')
        
        if parts[0] != "os":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # os.function_name
            func_name = parts[1]
            func = getattr(os, func_name)
        elif len(parts) >= 3:
            # os.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: os.getenv")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
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
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 os_getenv 失败: {e}")
        return {"error": str(e)}


def handle_os_execlpe(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 os_execlpe 工具调用"""
    try:
        # 解析函数路径: os.execlpe
        parts = "os.execlpe".split('.')
        
        if parts[0] != "os":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # os.function_name
            func_name = parts[1]
            func = getattr(os, func_name)
        elif len(parts) >= 3:
            # os.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: os.execlpe")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
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
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 os_execlpe 失败: {e}")
        return {"error": str(e)}


def handle_os_get_exec_path(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 os_get_exec_path 工具调用"""
    try:
        # 解析函数路径: os.get_exec_path
        parts = "os.get_exec_path".split('.')
        
        if parts[0] != "os":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # os.function_name
            func_name = parts[1]
            func = getattr(os, func_name)
        elif len(parts) >= 3:
            # os.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: os.get_exec_path")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
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
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 os_get_exec_path 失败: {e}")
        return {"error": str(e)}


def handle_os_execle(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 os_execle 工具调用"""
    try:
        # 解析函数路径: os.execle
        parts = "os.execle".split('.')
        
        if parts[0] != "os":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # os.function_name
            func_name = parts[1]
            func = getattr(os, func_name)
        elif len(parts) >= 3:
            # os.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: os.execle")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
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
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 os_execle 失败: {e}")
        return {"error": str(e)}


def handle_os_add_dll_directory(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 os_add_dll_directory 工具调用"""
    try:
        # 解析函数路径: os.add_dll_directory
        parts = "os.add_dll_directory".split('.')
        
        if parts[0] != "os":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # os.function_name
            func_name = parts[1]
            func = getattr(os, func_name)
        elif len(parts) >= 3:
            # os.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: os.add_dll_directory")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
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
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 os_add_dll_directory 失败: {e}")
        return {"error": str(e)}


def handle_os_execlp(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 os_execlp 工具调用"""
    try:
        # 解析函数路径: os.execlp
        parts = "os.execlp".split('.')
        
        if parts[0] != "os":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # os.function_name
            func_name = parts[1]
            func = getattr(os, func_name)
        elif len(parts) >= 3:
            # os.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: os.execlp")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
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
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 os_execlp 失败: {e}")
        return {"error": str(e)}


def handle_os_execl(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 os_execl 工具调用"""
    try:
        # 解析函数路径: os.execl
        parts = "os.execl".split('.')
        
        if parts[0] != "os":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # os.function_name
            func_name = parts[1]
            func = getattr(os, func_name)
        elif len(parts) >= 3:
            # os.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: os.execl")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
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
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 os_execl 失败: {e}")
        return {"error": str(e)}


def process_mcp_request(request_line: str) -> str:
    """处理 MCP 请求"""
    try:
        request = json.loads(request_line.strip())
        method = request.get("method", "")
        params = request.get("params", {})
        request_id = request.get("id")
        
        if method == "initialize":
            # MCP 初始化请求
            response = {
                "jsonrpc": "2.0",
                "id": request_id,
                "result": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {
                        "tools": {},
                        "logging": {},
                        "prompts": {},
                        "resources": {}
                    },
                    "serverInfo": {
                        "name": "os-mcp-server",
                        "version": "1.0.0"
                    }
                }
            }
        elif method == "notifications/initialized":
            # 初始化完成通知，不需要响应
            return ""
        elif method == "tools/list":
            response = {
                "jsonrpc": "2.0",
                "id": request_id,
                "result": {"tools": TOOLS}
            }
        elif method == "tools/call":
            tool_name = params.get("name", "")
            arguments = params.get("arguments", {})
            
            # 调用对应的处理函数
            handler_name = f"handle_{tool_name}"
            if handler_name in globals():
                result = globals()[handler_name](arguments)
            else:
                result = {"error": f"未找到工具处理器: {tool_name}"}
            
            response = {
                "jsonrpc": "2.0",
                "id": request_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(result, ensure_ascii=False, indent=2)
                        }
                    ]
                }
            }
        else:
            response = {
                "jsonrpc": "2.0",
                "id": request_id,
                "error": {
                    "code": -32601,
                    "message": f"未知方法: {method}"
                }
            }
        
        return json.dumps(response)
    
    except Exception as e:
        logger.error(f"处理请求失败: {e}")
        return json.dumps({
            "jsonrpc": "2.0",
            "id": None,
            "error": {
                "code": -32603,
                "message": f"内部错误: {str(e)}"
            }
        })

async def main():
    """主函数 - MCP 服务器模式"""
    logger.info("启动 os MCP 服务器...")
    
    try:
        # 读取 stdin 并处理请求
        while True:
            try:
                line = sys.stdin.readline()
                if not line:
                    break
                
                line = line.strip()
                if line:
                    logger.debug(f"收到请求: {line}")
                    response = process_mcp_request(line)
                    if response:  # 只有当有响应时才输出
                        print(response, flush=True)
                        logger.debug(f"发送响应: {response}")
                        
            except EOFError:
                # 正常的输入结束
                break
            except Exception as e:
                logger.error(f"处理请求时出错: {e}")
                error_response = json.dumps({
                    "jsonrpc": "2.0",
                    "id": None,
                    "error": {
                        "code": -32603,
                        "message": f"内部错误: {str(e)}"
                    }
                })
                print(error_response, flush=True)
                
    except KeyboardInterrupt:
        logger.info("服务器停止")
    except Exception as e:
        logger.error(f"服务器错误: {e}")
    finally:
        logger.info("服务器关闭")

def cli_mode():
    """命令行模式 - 用于测试"""
    if len(sys.argv) < 3:
        print(json.dumps({"error": "参数不足，需要: 工具名 参数JSON"}))
        return
    
    tool_name = sys.argv[1]
    try:
        arguments = json.loads(sys.argv[2])
    except json.JSONDecodeError:
        print(json.dumps({"error": "参数格式错误"}))
        return
    
    # 调用对应的处理函数
    handler_name = f"handle_{tool_name}"
    if handler_name in globals():
        result = globals()[handler_name](arguments)
    else:
        result = {"error": f"未找到工具: {tool_name}"}
    
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # 命令行模式
        cli_mode()
    else:
        # MCP 服务器模式
        asyncio.run(main())
