#!/usr/bin/env python3
import json
import os
from auto_generate_mcp import generate_tools_with_lib2mcp, analyze_tool_usability_with_ollama, filter_top_tools
from pathlib import Path

def main():
    print("测试完整的工具分析和筛选流程...")
    
    # 创建输出目录
    output_dir = Path("test_output")
    output_dir.mkdir(exist_ok=True)
    
    # 1. 生成工具定义
    print("步骤 1: 生成工具定义...")
    tools_result = generate_tools_with_lib2mcp("requests", output_dir)
    
    if not tools_result['success']:
        print(f"工具定义生成失败: {tools_result['error']}")
        return
    
    tools_data = tools_result['tools']
    print(f"成功生成 {len(tools_data)} 个工具")
    
    # 2. 分析工具
    print("\n步骤 2: 分析工具使用频率和易用性...")
    analysis_result = analyze_tool_usability_with_ollama(tools_data, "requests", "deepseek-r1:8b")
    
    print(f"分析完成，共分析 {len(analysis_result['analysis'])} 个工具")
    
    # 显示前几个工具的分析结果
    print("\n前5个工具的分析结果:")
    for i, (tool_id, analysis) in enumerate(list(analysis_result['analysis'].items())[:5]):
        print(f"{i+1}. {tool_id}")
        print(f"   综合评分: {analysis.get('score', 'N/A')}")
        print(f"   理由: {analysis.get('reason', 'N/A')[:100]}...")
        print()
    
    # 3. 筛选工具
    print("步骤 3: 筛选最有用的工具 (40%)...")
    filtered_tools = filter_top_tools(
        analysis_result['tools'], 
        analysis_result['analysis'], 
        percentage=0.4
    )
    
    print(f"筛选完成: 从 {len(tools_data)} 个工具中筛选出 {len(filtered_tools)} 个工具")
    
    # 显示筛选后的工具
    print("\n筛选后的工具:")
    for tool_id in list(filtered_tools.keys())[:10]:
        print(f"  - {tool_id}")
    
    print("\n流程测试完成!")

if __name__ == "__main__":
    main()