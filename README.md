# Lib2MCP - Python Library to MCP Tool Converter

Lib2MCP 是一个强大的工具，可自动将 Python 库 API 转换为 MCP (Model Context Protocol) 工具规范，使 AI 模型能够直接调用 Python 库函数。

## 项目结构

```
lib2mcp/
├── src/                 # 核心源代码
│   └── lib2mcp/         # 主要库代码
├── generators/          # MCP工具链生成器
├── tests/               # 测试文件
├── examples/            # 示例和演示代码
├── docs/                # 文档
├── output/              # 生成的MCP工具链输出目录
├── README.md            # 项目说明
├── requirements.txt     # 依赖列表
└── config.yaml          # 配置文件
```

## 环境要求

- Python 版本: 3.10.18 (固定使用此版本)
- 支持的操作系统: Windows, macOS, Linux

## 安装依赖

```bash
pip install -r requirements.txt
```

## 使用方法

### 基本用法

```bash
# 生成指定库的 MCP 工具链（默认使用网络搜索分析）
cd generators
python auto_generate_mcp.py <library_name>

# 示例
python auto_generate_mcp.py requests
```

### 高级选项

```bash
# 指定输出目录
python auto_generate_mcp.py requests --output-dir ../output/my_output

# 只生成工具定义，不生成服务器
python auto_generate_mcp.py requests --tools-only

# 使用 Ollama 大模型进行分析（可选）
python auto_generate_mcp.py requests --use-ollama

# 指定 Ollama 模型
python auto_generate_mcp.py requests --use-ollama --ollama-model deepseek-r1:8b

# 自定义工具筛选百分比
python auto_generate_mcp.py requests --filter-percentage 0.5
```

## 网络搜索分析（默认行为）

本项目默认使用网络搜索分析来评估工具的使用频率和易用性，无需安装大模型即可智能筛选最有价值的工具：

- 基于关键词匹配估算使用频率
- 评估工具易用性和实用性
- 自动筛选前40%最有用的工具

## Ollama 集成（可选）

可选使用 Ollama 本地大模型来分析工具的使用频率和易用性，提供更精确的分析结果。

### 安装 Ollama

请从 [Ollama 官网](https://ollama.com/) 下载并安装 Ollama。

### 拉取默认模型

```bash
ollama pull deepseek-r1:8b
```

## 生成的文件

运行脚本后将生成以下文件：

1. `tools/<library_name>_tools.json` - 工具定义文件
2. `<library_name>_mcp_server.py` - MCP 服务器脚本
3. `<library_name>_cherry_config.json` - CherryStudio 配置文件

## 示例和演示

查看 `examples/` 目录中的示例代码：

- `show_network_analysis.py` - 展示网络搜索分析过程
- `demonstrate_functionality.py` - 完整功能演示
- `final_demo.py` - 最终演示脚本

## 测试

运行测试文件位于 `tests/` 目录：

```bash
cd tests
python test_analysis.py
```

## 许可证

MIT