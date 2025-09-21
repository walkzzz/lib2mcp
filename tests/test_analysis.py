#!/usr/bin/env python3
import json
from auto_generate_mcp import analyze_tool_usability_with_ollama

# 创建一个简单的测试工具数据
test_tools = {
    "requests.get": {
        "name": "requests.get",
        "description": "发送 HTTP GET 请求",
        "inputSchema": {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string",
                    "description": "请求的 URL"
                }
            },
            "required": ["url"]
        }
    }
}

print("测试 Ollama 工具分析功能...")
print("使用的模型: deepseek-r1:8b")

# 调用分析函数
result = analyze_tool_usability_with_ollama(test_tools, "requests", "deepseek-r1:8b")

print("\n分析结果:")
print(json.dumps(result, ensure_ascii=False, indent=2))