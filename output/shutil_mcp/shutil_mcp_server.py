#!/usr/bin/env python3
"""
自动生成的 MCP 服务器
库: shutil
工具数量: 8
"""

import asyncio
import json
import logging
import sys
from typing import Dict, Any

try:
    import shutil  # type: ignore
except ImportError:
    print("错误: 未安装 shutil 库，请运行: pip install shutil")
    sys.exit(1)

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("shutil_mcp_server")

# 工具定义
TOOLS = [
    {
        "name": "shutil_get_unpack_formats",
        "description": "Returns a list of supported formats for unpacking.\nEach element of the returned sequence is a tuple\n(name, extensions, description)",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "shutil_get_archive_formats",
        "description": "Returns a list of supported formats for archiving and unarchiving.\nEach element of the returned sequence is a tuple (name, description)",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "shutil_chown",
        "description": "Change owner user and group of the given path.\nuser and group can be the uid/gid or the user/group names, and in that case,\nthey are converted to their respective uid/gid.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "user": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "group": {
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
        "name": "shutil_get_terminal_size",
        "description": "Get the size of the terminal window.\nFor each of the two dimensions, the environment variable, COLUMNS\nand LINES respectively, is checked. If the variable is defined and\nthe value is a positive integer, it is used.\nWhen COLUMNS or LINES is not defined, which is the common case,\nthe terminal connected to sys.__stdout__ is queried\nby invoking os.get_terminal_size.\nIf the terminal size cannot be successfully queried, either because\nthe system doesn't support querying, or because we are not\nconnected to a terminal, the value given in fallback parameter\nis used. Fallback defaults to (80, 24) which is the default\nsize used by many terminal emulators.\nThe value returned is a named tuple of type os.terminal_size.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "fallback": {
                    "type": "string",
                    "default": "(80, 24)",
                    "description": "类型从默认值推断: tuple"
                }
            },
            "required": []
        }
    },
    {
        "name": "shutil_copyfileobj",
        "description": "copy data from file-like object fsrc to file-like object fdst",
        "inputSchema": {
            "type": "object",
            "properties": {
                "fsrc": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "fdst": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "length": {
                    "type": "integer",
                    "default": 0,
                    "description": "类型从默认值推断: int"
                }
            },
            "required": [
                "fsrc",
                "fdst"
            ]
        }
    },
    {
        "name": "shutil_copy2",
        "description": "Copy data and metadata. Return the file's destination.\nMetadata is copied with copystat(). Please see the copystat function\nfor more information.\nThe destination may be a directory.\nIf follow_symlinks is False, symlinks won't be followed. This\nresembles GNU's \"cp -P src dst\".",
        "inputSchema": {
            "type": "object",
            "properties": {
                "src": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "dst": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "follow_symlinks": {
                    "type": "integer",
                    "default": True,
                    "description": "类型从默认值推断: bool"
                }
            },
            "required": [
                "src",
                "dst"
            ]
        }
    },
    {
        "name": "shutil_copy",
        "description": "Copy data and mode bits (\"cp src dst\"). Return the file's destination.\nThe destination may be a directory.\nIf follow_symlinks is False, symlinks won't be followed. This\nresembles GNU's \"cp -P src dst\".\nIf source and destination are the same file, a SameFileError will be\nraised.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "src": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "dst": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "follow_symlinks": {
                    "type": "integer",
                    "default": True,
                    "description": "类型从默认值推断: bool"
                }
            },
            "required": [
                "src",
                "dst"
            ]
        }
    },
    {
        "name": "shutil_copyfile",
        "description": "Copy data from src to dst in the most efficient way possible.\nIf follow_symlinks is not set and src is a symbolic link, a new\nsymlink will be created instead of copying the file it points to.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "src": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "dst": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "follow_symlinks": {
                    "type": "integer",
                    "default": True,
                    "description": "类型从默认值推断: bool"
                }
            },
            "required": [
                "src",
                "dst"
            ]
        }
    }
]


def handle_shutil_get_unpack_formats(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 shutil_get_unpack_formats 工具调用"""
    try:
        # 解析函数路径: shutil.get_unpack_formats
        parts = "shutil.get_unpack_formats".split('.')
        
        if parts[0] != "shutil":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # shutil.function_name
            func_name = parts[1]
            func = getattr(shutil, func_name)
        elif len(parts) >= 3:
            # shutil.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: shutil.get_unpack_formats")
        
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
        logger.error(f"执行 shutil_get_unpack_formats 失败: {e}")
        return {"error": str(e)}


def handle_shutil_get_archive_formats(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 shutil_get_archive_formats 工具调用"""
    try:
        # 解析函数路径: shutil.get_archive_formats
        parts = "shutil.get_archive_formats".split('.')
        
        if parts[0] != "shutil":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # shutil.function_name
            func_name = parts[1]
            func = getattr(shutil, func_name)
        elif len(parts) >= 3:
            # shutil.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: shutil.get_archive_formats")
        
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
        logger.error(f"执行 shutil_get_archive_formats 失败: {e}")
        return {"error": str(e)}


def handle_shutil_chown(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 shutil_chown 工具调用"""
    try:
        # 解析函数路径: shutil.chown
        parts = "shutil.chown".split('.')
        
        if parts[0] != "shutil":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # shutil.function_name
            func_name = parts[1]
            func = getattr(shutil, func_name)
        elif len(parts) >= 3:
            # shutil.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: shutil.chown")
        
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
        logger.error(f"执行 shutil_chown 失败: {e}")
        return {"error": str(e)}


def handle_shutil_get_terminal_size(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 shutil_get_terminal_size 工具调用"""
    try:
        # 解析函数路径: shutil.get_terminal_size
        parts = "shutil.get_terminal_size".split('.')
        
        if parts[0] != "shutil":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # shutil.function_name
            func_name = parts[1]
            func = getattr(shutil, func_name)
        elif len(parts) >= 3:
            # shutil.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: shutil.get_terminal_size")
        
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
        logger.error(f"执行 shutil_get_terminal_size 失败: {e}")
        return {"error": str(e)}


def handle_shutil_copyfileobj(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 shutil_copyfileobj 工具调用"""
    try:
        # 解析函数路径: shutil.copyfileobj
        parts = "shutil.copyfileobj".split('.')
        
        if parts[0] != "shutil":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # shutil.function_name
            func_name = parts[1]
            func = getattr(shutil, func_name)
        elif len(parts) >= 3:
            # shutil.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: shutil.copyfileobj")
        
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
        logger.error(f"执行 shutil_copyfileobj 失败: {e}")
        return {"error": str(e)}


def handle_shutil_copy2(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 shutil_copy2 工具调用"""
    try:
        # 解析函数路径: shutil.copy2
        parts = "shutil.copy2".split('.')
        
        if parts[0] != "shutil":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # shutil.function_name
            func_name = parts[1]
            func = getattr(shutil, func_name)
        elif len(parts) >= 3:
            # shutil.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: shutil.copy2")
        
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
        logger.error(f"执行 shutil_copy2 失败: {e}")
        return {"error": str(e)}


def handle_shutil_copy(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 shutil_copy 工具调用"""
    try:
        # 解析函数路径: shutil.copy
        parts = "shutil.copy".split('.')
        
        if parts[0] != "shutil":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # shutil.function_name
            func_name = parts[1]
            func = getattr(shutil, func_name)
        elif len(parts) >= 3:
            # shutil.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: shutil.copy")
        
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
        logger.error(f"执行 shutil_copy 失败: {e}")
        return {"error": str(e)}


def handle_shutil_copyfile(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 shutil_copyfile 工具调用"""
    try:
        # 解析函数路径: shutil.copyfile
        parts = "shutil.copyfile".split('.')
        
        if parts[0] != "shutil":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # shutil.function_name
            func_name = parts[1]
            func = getattr(shutil, func_name)
        elif len(parts) >= 3:
            # shutil.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: shutil.copyfile")
        
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
        logger.error(f"执行 shutil_copyfile 失败: {e}")
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
                        "name": "shutil-mcp-server",
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
    logger.info("启动 shutil MCP 服务器...")
    
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
