"""
Command Line Interface

命令行界面，提供用户友好的转换和查询功能。
"""

import click
import sys
import json
from pathlib import Path
from typing import List, Optional

from . import LibraryConverter, ToolQueryManager, Config
from .exceptions import Lib2MCPError


@click.group()
@click.option('--config', '-c', type=click.Path(exists=True), help='配置文件路径')
@click.option('--verbose', '-v', is_flag=True, help='详细输出')
@click.pass_context
def cli(ctx, config, verbose):
    """Lib2MCP - Python库到MCP工具转换器"""
    
    # 设置日志级别
    if verbose:
        import logging
        logging.basicConfig(level=logging.DEBUG)
    
    # 加载配置
    try:
        ctx.obj = Config(config) if config else Config()
        ctx.obj.setup_logging()
    except Exception as e:
        click.echo(f"加载配置失败: {e}", err=True)
        sys.exit(1)


@cli.command()
@click.argument('libraries', nargs=-1, required=True)
@click.option('--output', '-o', type=click.Path(), help='输出目录')
@click.option('--format', 'output_format', type=click.Choice(['json', 'yaml']), default='json', help='输出格式')
@click.pass_obj
def convert(config, libraries, output, output_format):
    """转换Python库为MCP工具"""
    
    # 更新配置
    if output:
        config.output.output_directory = str(output)
    config.output.format = output_format
    
    try:
        converter = LibraryConverter(config)
        
        if len(libraries) == 1:
            # 单个库转换
            library = libraries[0]
            click.echo(f"转换库: {library}")
            
            with click.progressbar(length=100, label='转换进度') as bar:
                result = converter.convert_library(library, config.get_output_dir())
                bar.update(100)
            
            # 显示结果
            stats = result['statistics']
            click.echo(f"✅ 转换完成!")
            click.echo(f"   API总数: {stats['total_apis']}")
            click.echo(f"   生成工具: {stats['converted_tools']}")
            click.echo(f"   验证通过: {stats['validated_tools']}")
            
            if stats['validation_failures'] > 0:
                click.echo(f"   ⚠️ 验证失败: {stats['validation_failures']}")
        
        else:
            # 批量转换
            click.echo(f"批量转换 {len(libraries)} 个库...")
            
            result = converter.convert_multiple_libraries(list(libraries), config.get_output_dir())
            
            # 显示结果
            summary = result['summary']
            click.echo(f"✅ 批量转换完成!")
            click.echo(f"   成功转换: {summary['successful_count']}/{summary['total_libraries']}")
            click.echo(f"   总工具数: {summary['total_tools']}")
            
            if result['failed_conversions']:
                click.echo("❌ 转换失败的库:")
                for lib, error in result['failed_conversions'].items():
                    click.echo(f"   {lib}: {error}")
    
    except Lib2MCPError as e:
        click.echo(f"❌ 转换失败: {e}", err=True)
        sys.exit(1)
    except Exception as e:
        click.echo(f"❌ 未知错误: {e}", err=True)
        sys.exit(1)


@cli.group()
def query():
    """查询和管理生成的工具"""
    pass


@query.command('search')
@click.argument('keyword')
@click.option('--tools-file', type=click.Path(exists=True), help='工具文件路径')
@click.option('--limit', default=10, help='结果数量限制')
def search_tools(keyword, tools_file, limit):
    """搜索工具"""
    
    if not tools_file:
        # 在当前目录查找工具文件
        tools_files = list(Path('.').glob('*_tools.json'))
        if not tools_files:
            click.echo("❌ 未找到工具文件，请使用 --tools-file 指定", err=True)
            return
        tools_file = tools_files[0]
        click.echo(f"使用工具文件: {tools_file}")
    
    try:
        with open(tools_file, 'r', encoding='utf-8') as f:
            tools = json.load(f)
        
        query_manager = ToolQueryManager(tools)
        results = query_manager.search_tools(keyword, limit)
        
        if results:
            click.echo(f"找到 {len(results)} 个相关工具:")
            for i, result in enumerate(results, 1):
                tool = result['tool']
                score = result['score']
                click.echo(f"{i}. {tool['name']} (相关度: {score:.1f})")
                click.echo(f"   描述: {tool.get('description', '无描述')}")
                click.echo()
        else:
            click.echo(f"未找到与 '{keyword}' 相关的工具")
    
    except Exception as e:
        click.echo(f"❌ 搜索失败: {e}", err=True)


@query.command('list')
@click.option('--tools-file', type=click.Path(exists=True), help='工具文件路径')
@click.option('--page', default=1, help='页码')
@click.option('--size', default=20, help='每页大小')
def list_tools(tools_file, page, size):
    """列出所有工具"""
    
    if not tools_file:
        tools_files = list(Path('.').glob('*_tools.json'))
        if not tools_files:
            click.echo("❌ 未找到工具文件", err=True)
            return
        tools_file = tools_files[0]
    
    try:
        with open(tools_file, 'r', encoding='utf-8') as f:
            tools = json.load(f)
        
        query_manager = ToolQueryManager(tools)
        result = query_manager.list_all_tools(page, size)
        
        pagination = result['pagination']
        click.echo(f"工具列表 (第{pagination['page']}/{pagination['pages']}页，共{pagination['total']}个):")
        
        for i, item in enumerate(result['tools'], 1):
            tool = item['tool']
            click.echo(f"{i}. {tool['name']}")
            click.echo(f"   {tool.get('description', '无描述')}")
            click.echo()
    
    except Exception as e:
        click.echo(f"❌ 列表显示失败: {e}", err=True)


@query.command('stats')
@click.option('--tools-file', type=click.Path(exists=True), help='工具文件路径')
def show_stats(tools_file):
    """显示工具统计信息"""
    
    if not tools_file:
        tools_files = list(Path('.').glob('*_tools.json'))
        if not tools_files:
            click.echo("❌ 未找到工具文件", err=True)
            return
        tools_file = tools_files[0]
    
    try:
        with open(tools_file, 'r', encoding='utf-8') as f:
            tools = json.load(f)
        
        query_manager = ToolQueryManager(tools)
        stats = query_manager.get_statistics()
        
        click.echo("📊 工具统计信息:")
        click.echo(f"   总工具数: {stats['total_tools']}")
        click.echo(f"   模块数: {stats['module_count']}")
        click.echo(f"   关键词数: {stats['keyword_count']}")
        
        if stats['modules']:
            click.echo("   模块列表:")
            for module in sorted(stats['modules'])[:10]:  # 只显示前10个
                module_tools = query_manager.filter_by_module(module)
                click.echo(f"     {module} ({len(module_tools)} 个工具)")
            
            if len(stats['modules']) > 10:
                click.echo(f"     ... 还有 {len(stats['modules']) - 10} 个模块")
    
    except Exception as e:
        click.echo(f"❌ 统计显示失败: {e}", err=True)


@cli.command()
@click.option('--output', '-o', type=click.Path(), default='config.yaml', help='配置文件输出路径')
def init_config(output):
    """生成默认配置文件"""
    
    try:
        from .config import create_default_config_file
        create_default_config_file(output)
        click.echo(f"✅ 默认配置文件已生成: {output}")
        click.echo("可以编辑此文件来自定义转换行为")
    
    except Exception as e:
        click.echo(f"❌ 生成配置文件失败: {e}", err=True)


@cli.command()
def version():
    """显示版本信息"""
    from . import __version__
    click.echo(f"Lib2MCP {__version__}")


def main():
    """主入口函数"""
    try:
        cli()
    except KeyboardInterrupt:
        click.echo("\n用户中断操作")
        sys.exit(130)
    except Exception as e:
        click.echo(f"❌ 程序异常: {e}", err=True)
        sys.exit(1)


if __name__ == '__main__':
    main()