# 项目结构说明

## 目录结构

```
lib2mcp/
├── src/                 # 核心源代码
│   └── lib2mcp/         # 主要库代码
│       ├── core/        # 核心分析和转换逻辑
│       ├── models/      # 数据模型定义
│       ├── cli.py       # 命令行接口
│       ├── config.py    # 配置管理
│       ├── converter.py # 主要转换器
│       └── ...          # 其他核心模块
├── generators/          # MCP工具链生成器
│   └── auto_generate_mcp.py  # 自动生成MCP工具链的主脚本
├── tests/               # 测试文件
│   ├── test_analysis.py      # 分析功能测试
│   ├── test_network_search.py # 网络搜索功能测试
│   └── ...              # 其他测试文件
├── examples/            # 示例和演示代码
│   ├── show_network_analysis.py  # 网络搜索分析演示
│   ├── demonstrate_functionality.py # 功能演示
│   └── final_demo.py    # 最终演示脚本
├── docs/                # 文档
│   └── project_structure.md  # 项目结构说明
├── output/              # 生成的MCP工具链输出目录
├── README.md            # 项目说明
├── requirements.txt     # 依赖列表
├── config.yaml          # 配置文件
└── pyproject.toml       # 项目配置
```

## 各目录说明

### src/
核心源代码目录，包含lib2mcp库的主要实现。

### generators/
MCP工具链生成器目录，包含自动生成MCP工具链的脚本。

### tests/
测试文件目录，包含各种功能测试。

### examples/
示例和演示代码目录，包含使用示例和功能演示。

### docs/
文档目录，包含项目相关文档。

### output/
生成的MCP工具链输出目录，所有生成的文件将存放在此处。

## 使用说明

1. 进入`generators/`目录运行主脚本
2. 生成的文件将保存在`output/`目录中
3. 查看`examples/`目录了解使用方法
4. 运行`tests/`目录中的测试文件验证功能