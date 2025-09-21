#!/usr/bin/env python3
"""
测试网络搜索功能
"""

import json
from auto_generate_mcp import (
    generate_tools_with_lib2mcp,
    analyze_tool_usability_with_search,
    filter_top_tools
)
from pathlib import Path

def test_network_search_analysis():
    """测试网络搜索分析功能"""
    print("🔍 测试网络搜索分析功能...")
    
    # 创建临时输出目录
    output_dir = Path("./test_output")
    output_dir.mkdir(exist_ok=True)
    
    # 生成工具定义（使用一个简单的库）
    print("📝 生成工具定义...")
    tools_result = generate_tools_with_lib2mcp("json", output_dir)
    
    if not tools_result['success']:
        print(f"❌ 工具定义生成失败: {tools_result['error']}")
        return
    
    tools_data = tools_result['tools']
    print(f"✅ 成功生成 {len(tools_data)} 个工具")
    
    # 使用网络搜索分析工具
    print("🔍 使用网络搜索分析工具...")
    analysis_result = analyze_tool_usability_with_search(tools_data, "json")
    
    print("📊 分析结果:")
    for tool_id, analysis in list(analysis_result['analysis'].items())[:5]:  # 只显示前5个
        tool_name = analysis_result['tools'][tool_id].get('name', tool_id)
        print(f"  {tool_name}: 评分 {analysis['score']:.2f} ({analysis['reason']})")
    
    # 筛选前40%的工具
    print("🎯 筛选前40%的工具...")
    filtered_tools = filter_top_tools(
        analysis_result['tools'], 
        analysis_result['analysis'], 
        percentage=0.4
    )
    
    print(f"✅ 筛选完成: 原始 {len(tools_data)} 个工具 -> 筛选后 {len(filtered_tools)} 个工具")
    
    # 显示筛选后的工具
    print("🏆 筛选后的工具:")
    for tool_id in list(filtered_tools.keys())[:10]:  # 只显示前10个
        tool_name = filtered_tools[tool_id].get('name', tool_id)
        print(f"  - {tool_name}")
    
    print("🎉 测试完成!")

if __name__ == "__main__":
    test_network_search_analysis()