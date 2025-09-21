#!/usr/bin/env python3
"""
展示网络搜索分析的完整过程
"""

import json
from auto_generate_mcp import (
    generate_tools_with_lib2mcp,
    analyze_tool_usability_with_search,
    filter_top_tools
)
from pathlib import Path

def show_network_analysis_process():
    """展示网络搜索分析的完整过程"""
    print("🔍 展示网络搜索分析的完整过程")
    print("=" * 50)
    
    # 创建输出目录
    output_dir = Path("./demo_network_analysis")
    output_dir.mkdir(exist_ok=True)
    
    # 1. 生成工具定义
    print("📝 步骤 1: 生成工具定义 (使用 json 库)...")
    tools_result = generate_tools_with_lib2mcp("json", output_dir)
    
    if not tools_result['success']:
        print(f"❌ 工具定义生成失败: {tools_result['error']}")
        return
    
    tools_data = tools_result['tools']
    print(f"✅ 成功生成 {len(tools_data)} 个工具")
    
    # 2. 显示原始工具列表
    print("\n📋 原始工具列表:")
    for i, (tool_id, tool_def) in enumerate(list(tools_data.items())[:10]):  # 显示前10个
        tool_name = tool_def.get('name', tool_id)
        description = tool_def.get('description', '无描述')[:50]
        print(f"  {i+1:2d}. {tool_name}: {description}...")
    
    # 3. 使用网络搜索分析工具
    print("\n🔍 步骤 2: 使用网络搜索分析工具...")
    print("   分析过程（基于关键词匹配和模式识别）:")
    analysis_result = analyze_tool_usability_with_search(tools_data, "json")
    
    # 4. 显示分析结果
    print("\n📊 分析结果（按评分排序）:")
    sorted_tools = sorted(
        analysis_result['analysis'].items(), 
        key=lambda x: x[1]['score'], 
        reverse=True
    )
    
    for i, (tool_id, analysis) in enumerate(sorted_tools[:10]):  # 显示前10个
        tool_def = analysis_result['tools'][tool_id]
        tool_name = tool_def.get('name', tool_id)
        print(f"  {i+1:2d}. {tool_name}:")
        print(f"      评分: {analysis['score']:.2f}")
        print(f"      频率: {analysis['frequency']} | 易用性: {analysis['usability']} | 实用性: {analysis['utility']}")
        print(f"      理由: {analysis['reason']}")
        print()
    
    # 5. 筛选前40%的工具
    print("🎯 步骤 3: 筛选前40%最有用的工具...")
    filtered_tools = filter_top_tools(
        analysis_result['tools'], 
        analysis_result['analysis'], 
        percentage=0.4
    )
    
    print(f"✅ 筛选完成: {len(tools_data)} → {len(filtered_tools)} 个工具")
    
    # 6. 显示最终结果
    print("\n🏆 最终筛选结果:")
    for i, tool_id in enumerate(list(filtered_tools.keys())):
        tool_def = filtered_tools[tool_id]
        tool_name = tool_def.get('name', tool_id)
        description = tool_def.get('description', '无描述')[:60]
        print(f"  {i+1:2d}. {tool_name}: {description}...")
    
    print("\n🎉 网络搜索分析过程展示完成!")
    print("\n💡 说明:")
    print("  • 默认使用网络搜索分析，无需安装大模型")
    print("  • 基于关键词匹配和模式识别估算工具价值")
    print("  • 自动筛选最有用的工具用于MCP生成")

if __name__ == "__main__":
    show_network_analysis_process()