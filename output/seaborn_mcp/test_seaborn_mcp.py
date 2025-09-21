#!/usr/bin/env python3
"""
测试Seaborn的MCP服务器功能
"""

import json
import subprocess
import sys

def test_seaborn_mcp():
    """测试Seaborn的MCP服务器功能"""
    print("🔍 测试Seaborn的MCP服务器功能")
    
    # 测试seaborn_utils_load_dataset函数
    print("\n🧪 测试 seaborn_utils_load_dataset 函数:")
    try:
        # 构造测试参数
        test_args = {"name": "tips"}
        args_json = json.dumps(test_args, ensure_ascii=False)
        
        # 调用MCP服务器
        result = subprocess.run([
            sys.executable, 
            "seaborn_mcp_server.py", 
            "seaborn_utils_load_dataset", 
            args_json
        ], capture_output=True, text=True, timeout=30)
        
        print(f"   返回码: {result.returncode}")
        if result.returncode == 0:
            print("   ✓ 测试成功")
            # 只显示前200个字符以避免输出过长
            output_preview = result.stdout[:200] + "..." if len(result.stdout) > 200 else result.stdout
            print(f"   输出预览: {output_preview}")
        else:
            print("   ✗ 测试失败")
            print(f"   错误输出: {result.stderr}")
            
    except Exception as e:
        print(f"   测试失败: {e}")
    
    # 测试seaborn_axisgrid_pairplot函数
    print("\n🧪 测试 seaborn_axisgrid_pairplot 函数:")
    try:
        # 首先加载数据集
        load_args = {"name": "iris"}
        load_args_json = json.dumps(load_args, ensure_ascii=False)
        
        # 调用MCP服务器加载数据
        load_result = subprocess.run([
            sys.executable, 
            "seaborn_mcp_server.py", 
            "seaborn_utils_load_dataset", 
            load_args_json
        ], capture_output=True, text=True, timeout=30)
        
        if load_result.returncode == 0:
            print("   ✓ 数据加载成功")
            # 构造pairplot参数
            plot_args = {"data": "iris_data"}  # 这里需要实际的数据对象
            plot_args_json = json.dumps(plot_args, ensure_ascii=False)
            
            print("   注意: pairplot需要实际的数据对象作为参数，这里仅演示调用方式")
        else:
            print("   ✗ 数据加载失败")
            print(f"   错误输出: {load_result.stderr}")
            
    except Exception as e:
        print(f"   测试失败: {e}")

if __name__ == "__main__":
    test_seaborn_mcp()