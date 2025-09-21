# 使用指南

## 快速开始

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 生成MCP工具链
```bash
# 进入生成器目录
cd generators

# 为指定库生成MCP工具链（默认使用网络搜索分析）
python auto_generate_mcp.py <库名>

# 示例：为json库生成MCP工具链
python auto_generate_mcp.py json
```

## 高级用法

### 指定输出目录
```bash
python auto_generate_mcp.py json --output-dir ../my_output
```

### 只生成工具定义
```bash
python auto_generate_mcp.py json --tools-only
```

### 使用Ollama大模型分析
```bash
# 需要先安装并运行Ollama
python auto_generate_mcp.py json --use-ollama
```

### 自定义筛选比例
```bash
# 筛选前50%的工具
python auto_generate_mcp.py json --filter-percentage 0.5
```

## 生成的文件

运行脚本后将在项目根目录的`output/`文件夹中生成以下文件：

1. `output/<库名>_mcp/tools/<库名>_tools.json` - 工具定义文件
2. `output/<库名>_mcp/<库名>_mcp_server.py` - MCP服务器脚本
3. `output/<库名>_mcp/<库名>_cherry_config.json` - CherryStudio配置文件

## 使用生成的MCP工具链

### 1. 在CherryStudio中使用
1. 打开CherryStudio
2. 导入生成的配置文件`<库名>_cherry_config.json`
3. 即可使用该库的API工具

### 2. 测试MCP服务器
```bash
# 测试特定工具
python <库名>_mcp_server.py <工具名> '<参数JSON>'

# 示例
python json_mcp_server.py json_dumps '{"obj": {"key": "value"}}'
```

## 网络搜索分析 vs Ollama分析

### 网络搜索分析（默认）
- 无需安装额外软件
- 基于关键词匹配估算工具价值
- 快速且轻量级

### Ollama分析（可选）
- 需要安装Ollama
- 使用大模型进行更精确的分析
- 需要更多计算资源和时间

## 常见问题

### 1. 生成的工具太少或太多怎么办？
调整`--filter-percentage`参数来控制筛选比例：
```bash
# 筛选前30%的工具
python auto_generate_mcp.py json --filter-percentage 0.3

# 筛选前70%的工具
python auto_generate_mcp.py json --filter-percentage 0.7
```

### 2. 如何查看所有可用选项？
```bash
python auto_generate_mcp.py --help
```

### 3. 生成的工具不准确怎么办？
尝试使用Ollama大模型分析：
```bash
python auto_generate_mcp.py json --use-ollama
```