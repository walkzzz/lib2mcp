#!/usr/bin/env python3
"""
详细测试网络搜索分析功能
"""

import json
from auto_generate_mcp import (
    generate_tools_with_lib2mcp,
    analyze_tool_usability_with_search,
    filter_top_tools
)
from pathlib import Path

def test_detailed_analysis():
    """详细测试网络搜索分析功能"""
    print("🔍 详细测试网络搜索分析功能...")
    
    # 创建临时输出目录
    output_dir = Path("./test_output_detailed")
    output_dir.mkdir(exist_ok=True)
    
    # 生成工具定义（使用requests库）
    print("📝 生成工具定义...")
    tools_result = generate_tools_with_lib2mcp("requests", output_dir)
    
    if not tools_result['success']:
        print(f"❌ 工具定义生成失败: {tools_result['error']}")
        return
    
    tools_data = tools_result['tools']
    print(f"✅ 成功生成 {len(tools_data)} 个工具")
    
    # 显示前几个工具
    print("\n📋 原始工具列表（前10个）:")
    for i, (tool_id, tool_def) in enumerate(list(tools_data.items())[:10]):
        tool_name = tool_def.get('name', tool_id)
        description = tool_def.get('description', '无描述')
        print(f"  {i+1}. {tool_name}: {description[:60]}{'...' if len(description) > 60 else ''}")
    
    # 使用网络搜索分析工具
    print("\n🔍 使用网络搜索分析工具使用频率和易用性...")
    analysis_result = analyze_tool_usability_with_search(tools_data, "requests")
    
    print("\n📊 详细分析结果（前15个）:")
    sorted_tools = sorted(
        analysis_result['analysis'].items(), 
        key=lambda x: x[1]['score'], 
        reverse=True
    )
    
    for i, (tool_id, analysis) in enumerate(sorted_tools[:15]):
        tool_def = analysis_result['tools'][tool_id]
        tool_name = tool_def.get('name', tool_id)
        description = tool_def.get('description', '无描述')
        print(f"  {i+1}. {tool_name}:")
        print(f"     描述: {description[:80]}{'...' if len(description) > 80 else ''}")
        print(f"     评分: {analysis['score']:.2f}")
        print(f"     使用频率: {analysis['frequency']}")
        print(f"     易用性: {analysis['usability']}")
        print(f"     实用性: {analysis['utility']}")
        print(f"     理由: {analysis['reason']}")
        print()
    
    # 筛选前40%的工具
    print("🎯 筛选前40%的工具...")
    filtered_tools = filter_top_tools(
        analysis_result['tools'], 
        analysis_result['analysis'], 
        percentage=0.4
    )
    
    print(f"✅ 筛选完成: 原始 {len(tools_data)} 个工具 -> 筛选后 {len(filtered_tools)} 个工具")
    
    # 显示筛选后的工具
    print("\n🏆 筛选后的工具（前20个）:")
    for i, tool_id in enumerate(list(filtered_tools.keys())[:20]):
        tool_def = filtered_tools[tool_id]
        tool_name = tool_def.get('name', tool_id)
        description = tool_def.get('description', '无描述')
        print(f"  {i+1}. {tool_name}: {description[:60]}{'...' if len(description) > 60 else ''}")
    
    # 保存分析结果到文件
    analysis_output = {
        'original_tools_count': len(tools_data),
        'filtered_tools_count': len(filtered_tools),
        'analysis_details': [
            {
                'tool_id': tool_id,
                'tool_name': analysis_result['tools'][tool_id].get('name', tool_id),
                'analysis': analysis
            }
            for tool_id, analysis in sorted_tools
        ],
        'filtered_tools': list(filtered_tools.keys())
    }
    
    analysis_file = output_dir / "analysis_result.json"
    with open(analysis_file, 'w', encoding='utf-8') as f:
        json.dump(analysis_output, f, ensure_ascii=False, indent=2)
    
    print(f"\n💾 分析结果已保存到: {analysis_file}")
    print("\n🎉 详细测试完成!")

if __name__ == "__main__":
    test_detailed_analysis()