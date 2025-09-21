#!/usr/bin/env python3
"""
测试os模块的MCP服务器功能
"""

import json
import subprocess
import sys

def test_os_mcp():
    """测试os模块的MCP服务器功能"""
    print("🔍 测试os模块的MCP服务器功能")
    
    # 测试os_getenv函数
    print("\n🧪 测试 os_getenv 函数:")
    try:
        # 构造测试参数
        test_args = {"key": "PATH"}
        args_json = json.dumps(test_args, ensure_ascii=False)
        
        # 调用MCP服务器
        result = subprocess.run([
            sys.executable, 
            "os_mcp_server.py", 
            "os_getenv", 
            args_json
        ], capture_output=True, text=True, timeout=10)
        
        print(f"   返回码: {result.returncode}")
        print(f"   标准输出: {result.stdout}")
        if result.stderr:
            print(f"   错误输出: {result.stderr}")
            
    except Exception as e:
        print(f"   测试失败: {e}")
    
    # 测试os_get_exec_path函数
    print("\n🧪 测试 os_get_exec_path 函数:")
    try:
        # 构造测试参数
        test_args = {}
        args_json = json.dumps(test_args, ensure_ascii=False)
        
        # 调用MCP服务器
        result = subprocess.run([
            sys.executable, 
            "os_mcp_server.py", 
            "os_get_exec_path", 
            args_json
        ], capture_output=True, text=True, timeout=10)
        
        print(f"   返回码: {result.returncode}")
        print(f"   标准输出: {result.stdout}")
        if result.stderr:
            print(f"   错误输出: {result.stderr}")
            
    except Exception as e:
        print(f"   测试失败: {e}")

if __name__ == "__main__":
    test_os_mcp()