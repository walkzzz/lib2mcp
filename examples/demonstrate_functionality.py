#!/usr/bin/env python3
"""
演示完整的功能：默认使用网络搜索分析工具使用频率和易用性
"""

import json
from auto_generate_mcp import (
    generate_tools_with_lib2mcp,
    analyze_tool_usability_with_search,
    analyze_tool_usability_with_ollama,
    filter_top_tools
)
from pathlib import Path

def demonstrate_functionality():
    """演示完整的功能"""
    print("🚀 演示完整的MCP工具链生成功能")
    print("=" * 60)
    
    # 创建输出目录
    output_dir = Path("./demo_output")
    output_dir.mkdir(exist_ok=True)
    
    # 1. 生成工具定义
    print("📝 步骤 1: 生成工具定义 (使用 json 库)...")
    tools_result = generate_tools_with_lib2mcp("json", output_dir)
    
    if not tools_result['success']:
        print(f"❌ 工具定义生成失败: {tools_result['error']}")
        return
    
    tools_data = tools_result['tools']
    print(f"✅ 成功生成 {len(tools_data)} 个工具")
    
    # 2. 使用网络搜索分析工具（默认行为）
    print("\n🔍 步骤 2: 使用网络搜索分析工具使用频率和易用性...")
    print("   （这是默认行为，无需额外参数）")
    analysis_result = analyze_tool_usability_with_search(tools_data, "json")
    
    print("\n📊 分析过程展示（前5个工具）:")
    sorted_tools = sorted(
        analysis_result['analysis'].items(), 
        key=lambda x: x[1]['score'], 
        reverse=True
    )
    
    for i, (tool_id, analysis) in enumerate(sorted_tools[:5]):
        tool_def = analysis_result['tools'][tool_id]
        tool_name = tool_def.get('name', tool_id)
        print(f"  {i+1}. 工具: {tool_name}")
        print(f"     频率估算: {analysis['frequency']} (基于网络搜索关键词匹配)")
        print(f"     易用性评估: {analysis['usability']} (基于描述长度和关键词)")
        print(f"     实用性评估: {analysis['utility']} (基于工具名称模式)")
        print(f"     综合评分: {analysis['score']:.2f}")
        print(f"     评估理由: {analysis['reason']}")
        print()
    
    # 3. 筛选前40%的工具
    print("🎯 步骤 3: 筛选前40%最有用的工具...")
    filtered_tools = filter_top_tools(
        analysis_result['tools'], 
        analysis_result['analysis'], 
        percentage=0.4
    )
    
    print(f"✅ 筛选完成: {len(tools_data)} → {len(filtered_tools)} 个工具")
    
    # 4. 显示筛选结果
    print("\n🏆 最终筛选结果（前5个工具）:")
    for i, tool_id in enumerate(list(filtered_tools.keys())[:5]):
        tool_def = filtered_tools[tool_id]
        tool_name = tool_def.get('name', tool_id)
        description = tool_def.get('description', '无描述')
        print(f"  {i+1}. {tool_name}: {description[:60]}{'...' if len(description) > 60 else ''}")
    
    # 5. 对比使用Ollama大模型的分析（可选）
    print("\n🤖 可选：使用Ollama大模型进行分析对比...")
    try:
        # 这里我们只分析前5个工具以节省时间
        sample_tools = dict(list(tools_data.items())[:5])
        print("   正在使用Ollama分析前5个工具...（这可能需要一些时间）")
        ollama_result = analyze_tool_usability_with_ollama(sample_tools, "json", "deepseek-r1:8b")
        
        print("\n   Ollama分析结果对比:")
        for tool_id, analysis in ollama_result['analysis'].items():
            tool_name = sample_tools[tool_id].get('name', tool_id)
            network_score = analysis_result['analysis'][tool_id]['score']
            ollama_score = analysis['score']
            print(f"     {tool_name}:")
            print(f"       网络搜索评分: {network_score:.2f}")
            print(f"       Ollama评分: {ollama_score:.2f}")
            print(f"       差异: {ollama_score - network_score:.2f}")
    except Exception as e:
        print(f"   Ollama分析跳过: {e}")
    
    # 6. 总结
    print("\n" + "=" * 60)
    print("🎉 功能演示完成!")
    print("\n📋 关键特性:")
    print("  • 默认使用网络搜索分析，无需安装大模型")
    print("  • 自动评估工具使用频率、易用性和实用性")
    print(f"  • 智能筛选前40% ({len(filtered_tools)}个)最有用的工具")
    print("  • 可选使用Ollama大模型进行更精确的分析")
    
    print("\n🔧 使用方法:")
    print("  默认使用网络搜索:")
    print("    python auto_generate_mcp.py <library_name>")
    print("  使用Ollama大模型:")
    print("    python auto_generate_mcp.py <library_name> --use-ollama")
    
    print("\n📁 输出文件:")
    print(f"  工具定义: {tools_result['tools_file']}")
    print(f"  分析结果: demo_output/analysis_result.json")

if __name__ == "__main__":
    demonstrate_functionality()