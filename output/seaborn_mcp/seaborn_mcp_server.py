#!/usr/bin/env python3
"""
自动生成的 MCP 服务器
库: seaborn
工具数量: 77
"""

import asyncio
import json
import logging
import sys
from typing import Dict, Any

try:
    import seaborn  # type: ignore
except ImportError:
    print("错误: 未安装 seaborn 库，请运行: pip install seaborn")
    sys.exit(1)

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("seaborn_mcp_server")

# 工具定义
TOOLS = [
    {
        "name": "seaborn_distributions_distplot",
        "description": "DEPRECATED\nThis function has been deprecated and will be removed in seaborn v0.14.0.\nIt has been replaced by :func:`histplot` and :func:`displot`, two functions\nwith a modern API and many more capabilities.\nFor a guide to updating, please see this notebook:\nhttps://gist.github.com/mwaskom/de44147ed2974457ad6372750bbe5751",
        "inputSchema": {
            "type": "object",
            "properties": {
                "a": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "bins": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "hist": {
                    "type": "integer",
                    "default": True,
                    "description": "类型从默认值推断: bool"
                },
                "kde": {
                    "type": "integer",
                    "default": True,
                    "description": "类型从默认值推断: bool"
                },
                "rug": {
                    "type": "integer",
                    "default": False,
                    "description": "类型从默认值推断: bool"
                },
                "fit": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "hist_kws": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kde_kws": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "rug_kws": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "fit_kws": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "color": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "vertical": {
                    "type": "integer",
                    "default": False,
                    "description": "类型从默认值推断: bool"
                },
                "norm_hist": {
                    "type": "integer",
                    "default": False,
                    "description": "类型从默认值推断: bool"
                },
                "axlabel": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "label": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "ax": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "x": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": []
        }
    },
    {
        "name": "seaborn_external_docscrape_ClassDoc_keys",
        "description": "D.keys() -> a set-like object providing a view on D's keys",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "seaborn_external_docscrape_FunctionDoc_values",
        "description": "D.values() -> an object providing a view on D's values",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "seaborn_external_docscrape_FunctionDoc_keys",
        "description": "D.keys() -> a set-like object providing a view on D's keys",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "seaborn_widgets_choose_diverging_palette",
        "description": "Launch an interactive widget to choose a diverging color palette.\nThis corresponds with the :func:`diverging_palette` function. This kind\nof palette is good for data that range between interesting low values\nand interesting high values with a meaningful midpoint. (For example,\nchange scores relative to some baseline value).\nRequires IPython 2+ and must be used in the notebook.\nParameters\n----------\nas_cmap : bool\nIf True, the return value is a matplotlib colormap rather than a\nlist of discrete colors.\nReturns\n-------\npal or cmap : list of colors or matplotlib colormap\nObject that can be passed to plotting functions.\nSee Also\n--------\ndiverging_palette : Create a diverging color palette or colormap.\nchoose_colorbrewer_palette : Interactively choose palettes from the\ncolorbrewer set, including diverging palettes.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "as_cmap": {
                    "type": "integer",
                    "default": False,
                    "description": "类型从默认值推断: bool"
                }
            },
            "required": []
        }
    },
    {
        "name": "seaborn_external_docscrape_FunctionDoc_items",
        "description": "D.items() -> a set-like object providing a view on D's items",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "seaborn_utils_load_dataset",
        "description": "Load an example dataset from the online repository (requires internet).\nThis function provides quick access to a small number of example datasets\nthat are useful for documenting seaborn or generating reproducible examples\nfor bug reports. It is not necessary for normal usage.\nNote that some of the datasets have a small amount of preprocessing applied\nto define a proper ordering for categorical variables.\nUse :func:`get_dataset_names` to see a list of available datasets.\nParameters\n----------\nname : str\nName of the dataset (``{name}.csv`` on\nhttps://github.com/mwaskom/seaborn-data).\ncache : boolean, optional\nIf True, try to load from the local cache first, and save to the cache\nif a download is required.\ndata_home : string, optional\nThe directory in which to cache data; see :func:`get_data_home`.\nkws : keys and values, optional\nAdditional keyword arguments are passed to passed through to\n:func:`pandas.read_csv`.\nReturns\n-------\ndf : :class:`pandas.DataFrame`\nTabular data, possibly with some preprocessing applied.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "类型从参数名推断: name"
                },
                "cache": {
                    "type": "integer",
                    "default": True,
                    "description": "类型从默认值推断: bool"
                },
                "data_home": {
                    "type": "object",
                    "description": "类型从参数名推断: data_home"
                },
                "kws": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "name",
                "kws"
            ]
        }
    },
    {
        "name": "seaborn_widgets_choose_cubehelix_palette",
        "description": "Launch an interactive widget to create a sequential cubehelix palette.\nThis corresponds with the :func:`cubehelix_palette` function. This kind\nof palette is good for data that range between relatively uninteresting\nlow values and interesting high values. The cubehelix system allows the\npalette to have more hue variance across the range, which can be helpful\nfor distinguishing a wider range of values.\nRequires IPython 2+ and must be used in the notebook.\nParameters\n----------\nas_cmap : bool\nIf True, the return value is a matplotlib colormap rather than a\nlist of discrete colors.\nReturns\n-------\npal or cmap : list of colors or matplotlib colormap\nObject that can be passed to plotting functions.\nSee Also\n--------\ncubehelix_palette : Create a sequential palette or colormap using the\ncubehelix system.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "as_cmap": {
                    "type": "integer",
                    "default": False,
                    "description": "类型从默认值推断: bool"
                }
            },
            "required": []
        }
    },
    {
        "name": "seaborn_axisgrid_FacetGrid_refline",
        "description": "Add a reference line(s) to each facet.\nParameters\n----------\nx, y : numeric\nValue(s) to draw the line(s) at.\ncolor : :mod:`matplotlib color <matplotlib.colors>`\nSpecifies the color of the reference line(s). Pass ``color=None`` to\nuse ``hue`` mapping.\nlinestyle : str\nSpecifies the style of the reference line(s).\nline_kws : key, value mappings\nOther keyword arguments are passed to :meth:`matplotlib.axes.Axes.axvline`\nwhen ``x`` is not None and :meth:`matplotlib.axes.Axes.axhline` when ``y``\nis not None.\nReturns\n-------\n:class:`FacetGrid` instance\nReturns ``self`` for easy method chaining.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "x": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "y": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "color": {
                    "type": "string",
                    "default": ".5",
                    "description": "类型从默认值推断: str"
                },
                "linestyle": {
                    "type": "string",
                    "default": "--",
                    "description": "类型从默认值推断: str"
                },
                "line_kws": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "line_kws"
            ]
        }
    },
    {
        "name": "seaborn_distributions_ecdfplot",
        "description": "Plot empirical cumulative distribution functions.\nAn ECDF represents the proportion or count of observations falling below each\nunique value in a dataset. Compared to a histogram or density plot, it has the\nadvantage that each observation is visualized directly, meaning that there are\nno binning or smoothing parameters that need to be adjusted. It also aids direct\ncomparisons between multiple distributions. A downside is that the relationship\nbetween the appearance of the plot and the basic properties of the distribution\n(such as its central tendency, variance, and the presence of any bimodality)\nmay not be as intuitive.\nMore information is provided in the :ref:`user guide <tutorial_ecdf>`.\nParameters\n----------\ndata : :class:`pandas.DataFrame`, :class:`numpy.ndarray`, mapping, or sequence\nInput data structure. Either a long-form collection of vectors that can be\nassigned to named variables or a wide-form dataset that will be internally\nreshaped.\nx, y : vectors or keys in ``data``\nVariables that specify positions on the x and y axes.\nhue : vector or key in ``data``\nSemantic variable that is mapped to determine the color of plot elements.\nweights : vector or key in ``data``\nIf provided, weight the contribution of the corresponding data points\ntowards the cumulative distribution using these values.\nstat : {{\"proportion\", \"count\"}}\nDistribution statistic to compute.\ncomplementary : bool\nIf True, use the complementary CDF (1 - CDF)\npalette : string, list, dict, or :class:`matplotlib.colors.Colormap`\nMethod for choosing the colors to use when mapping the ``hue`` semantic.\nString values are passed to :func:`color_palette`. List or dict values\nimply categorical mapping, while a colormap object implies numeric mapping.\nhue_order : vector of strings\nSpecify the order of processing and plotting for categorical levels of the\n``hue`` semantic.\nhue_norm : tuple or :class:`matplotlib.colors.Normalize`\nEither a pair of values that set the normalization range in data units\nor an object that will map from data units into a [0, 1] interval. Usage\nimplies numeric mapping.\nlog_scale : bool or number, or pair of bools or numbers\nSet axis scale(s) to log. A single value sets the data axis for univariate\ndistributions and both axes for bivariate distributions. A pair of values\nsets each axis independently. Numeric values are interpreted as the desired\nbase (default 10). If `False`, defer to the existing Axes scale.\nlegend : bool\nIf False, suppress the legend for semantic variables.\nax : :class:`matplotlib.axes.Axes`\nPre-existing axes for the plot. Otherwise, call :func:`matplotlib.pyplot.gca`\ninternally.\nkwargs\nOther keyword arguments are passed to :meth:`matplotlib.axes.Axes.plot`.\nReturns\n-------\n:class:`matplotlib.axes.Axes`\nThe matplotlib axes containing the plot.\nSee Also\n--------\ndisplot : Figure-level interface to distribution plot functions.\nhistplot : Plot a histogram of binned counts with optional normalization or smoothing.\nkdeplot : Plot univariate or bivariate distributions using kernel density estimation.\nrugplot : Plot a tick at each observation value along the x and/or y axes.\nExamples\n--------\n.. include:: ../docstrings/ecdfplot.rst",
        "inputSchema": {
            "type": "object",
            "properties": {
                "data": {
                    "type": "object",
                    "description": "类型从参数名推断: data"
                },
                "x": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "y": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "hue": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "weights": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "stat": {
                    "type": "string",
                    "default": "proportion",
                    "description": "类型从默认值推断: str"
                },
                "complementary": {
                    "type": "integer",
                    "default": False,
                    "description": "类型从默认值推断: bool"
                },
                "palette": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "hue_order": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "hue_norm": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "log_scale": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "legend": {
                    "type": "integer",
                    "default": True,
                    "description": "类型从默认值推断: bool"
                },
                "ax": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "kwargs"
            ]
        }
    },
    {
        "name": "seaborn_external_docscrape_ClassDoc_get",
        "description": "D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "key": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "default": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "key"
            ]
        }
    },
    {
        "name": "seaborn_axisgrid_PairGrid_apply",
        "description": "Pass the grid to a user-supplied function and return self.\nThe `func` must accept an object of this type for its first\npositional argument. Additional arguments are passed through.\nThe return value of `func` is ignored; this method returns self.\nSee the `pipe` method if you want the return value.\nAdded in v0.12.0.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "func": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "args": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "func",
                "args",
                "kwargs"
            ]
        }
    },
    {
        "name": "seaborn_axisgrid_PairGrid_pipe",
        "description": "Pass the grid to a user-supplied function and return its value.\nThe `func` must accept an object of this type for its first\npositional argument. Additional arguments are passed through.\nThe return value of `func` becomes the return value of this method.\nSee the `apply` method if you want to return self instead.\nAdded in v0.12.0.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "func": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "args": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "func",
                "args",
                "kwargs"
            ]
        }
    },
    {
        "name": "seaborn_categorical_Beeswarm_position_candidates",
        "description": "Return a list of coordinates that might be valid by adjusting x.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "xyr_i": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "neighbors": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "xyr_i",
                "neighbors"
            ]
        }
    },
    {
        "name": "seaborn_external_docscrape_FunctionDoc_get_func",
        "description": "获取数据（FunctionDoc类的方法）",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "seaborn_axisgrid_Grid_add_legend",
        "description": "Draw a legend, maybe placing it outside axes and resizing the figure.\nParameters\n----------\nlegend_data : dict\nDictionary mapping label names (or two-element tuples where the\nsecond element is a label name) to matplotlib artist handles. The\ndefault reads from ``self._legend_data``.\ntitle : string\nTitle for the legend. The default reads from ``self._hue_var``.\nlabel_order : list of labels\nThe order that the legend entries should appear in. The default\nreads from ``self.hue_names``.\nadjust_subtitles : bool\nIf True, modify entries with invisible artists to left-align\nthe labels and set the font size to that of a title.\nkwargs : key, value pairings\nOther keyword arguments are passed to the underlying legend methods\non the Figure or Axes object.\nReturns\n-------\nself : Grid instance\nReturns self for easy chaining.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "legend_data": {
                    "type": "object",
                    "description": "类型从参数名推断: legend_data"
                },
                "title": {
                    "type": "string",
                    "description": "类型从参数名推断: title"
                },
                "label_order": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "adjust_subtitles": {
                    "type": "integer",
                    "default": False,
                    "description": "类型从默认值推断: bool"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "kwargs"
            ]
        }
    },
    {
        "name": "seaborn_axisgrid_PairGrid_map_diag",
        "description": "Plot with a univariate function on each diagonal subplot.\nParameters\n----------\nfunc : callable plotting function\nMust take an x array as a positional argument and draw onto the\n\"currently active\" matplotlib Axes. Also needs to accept kwargs\ncalled ``color`` and  ``label``.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "func": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "func",
                "kwargs"
            ]
        }
    },
    {
        "name": "seaborn_utils_get_color_cycle",
        "description": "Return the list of colors in the current matplotlib color cycle\nParameters\n----------\nNone\nReturns\n-------\ncolors : list\nList of matplotlib colors in the current cycle, or dark gray if\nthe current color cycle is empty.",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "seaborn_axisgrid_FacetGrid_savefig",
        "description": "Save an image of the plot.\nThis wraps :meth:`matplotlib.figure.Figure.savefig`, using bbox_inches=\"tight\"\nby default. Parameters are passed through to the matplotlib function.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "args": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "args",
                "kwargs"
            ]
        }
    },
    {
        "name": "seaborn_utils_get_data_home",
        "description": "Return a path to the cache directory for example datasets.\nThis directory is used by :func:`load_dataset`.\nIf the ``data_home`` argument is not provided, it will use a directory\nspecified by the `SEABORN_DATA` environment variable (if it exists)\nor otherwise default to an OS-appropriate user cache location.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "data_home": {
                    "type": "object",
                    "description": "类型从参数名推断: data_home"
                }
            },
            "required": []
        }
    },
    {
        "name": "seaborn_axisgrid_PairGrid_map_lower",
        "description": "Plot with a bivariate function on the lower diagonal subplots.\nParameters\n----------\nfunc : callable plotting function\nMust take x, y arrays as positional arguments and draw onto the\n\"currently active\" matplotlib Axes. Also needs to accept kwargs\ncalled ``color`` and  ``label``.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "func": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "func",
                "kwargs"
            ]
        }
    },
    {
        "name": "seaborn_axisgrid_FacetGrid_facet_data",
        "description": "Generator for name indices and data subsets for each facet.\nYields\n------\n(i, j, k), data_ijk : tuple of ints, DataFrame\nThe ints provide an index into the {row, col, hue}_names attribute,\nand the dataframe contains a subset of the full data corresponding\nto each facet. The generator yields subsets that correspond with\nthe self.axes.flat iterator, or self.axes[i, j] when `col_wrap`\nis None.",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "seaborn_axisgrid_JointGrid_set_axis_labels",
        "description": "Set axis labels on the bivariate axes.\nParameters\n----------\nxlabel, ylabel : strings\nLabel names for the x and y variables.\nkwargs : key, value mappings\nOther keyword arguments are passed to the following functions:\n- :meth:`matplotlib.axes.Axes.set_xlabel`\n- :meth:`matplotlib.axes.Axes.set_ylabel`\nReturns\n-------\n:class:`JointGrid` instance\nReturns ``self`` for easy method chaining.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "x_var": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "y_var": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "clear_inner": {
                    "type": "integer",
                    "default": True,
                    "description": "类型从默认值推断: bool"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "kwargs"
            ]
        }
    },
    {
        "name": "seaborn_axisgrid_PairGrid_map_upper",
        "description": "Plot with a bivariate function on the upper diagonal subplots.\nParameters\n----------\nfunc : callable plotting function\nMust take x, y arrays as positional arguments and draw onto the\n\"currently active\" matplotlib Axes. Also needs to accept kwargs\ncalled ``color`` and  ``label``.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "func": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "func",
                "kwargs"
            ]
        }
    },
    {
        "name": "seaborn_categorical_Beeswarm_add_gutters",
        "description": "Stop points from extending beyond their territory.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "points": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "center": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "log_scale": {
                    "type": "integer",
                    "default": False,
                    "description": "类型从默认值推断: bool"
                }
            },
            "required": [
                "points",
                "center"
            ]
        }
    },
    {
        "name": "seaborn_axisgrid_JointGrid_refline",
        "description": "Add a reference line(s) to joint and/or marginal axes.\nParameters\n----------\nx, y : numeric\nValue(s) to draw the line(s) at.\njoint, marginal : bools\nWhether to add the reference line(s) to the joint/marginal axes.\ncolor : :mod:`matplotlib color <matplotlib.colors>`\nSpecifies the color of the reference line(s).\nlinestyle : str\nSpecifies the style of the reference line(s).\nline_kws : key, value mappings\nOther keyword arguments are passed to :meth:`matplotlib.axes.Axes.axvline`\nwhen ``x`` is not None and :meth:`matplotlib.axes.Axes.axhline` when ``y``\nis not None.\nReturns\n-------\n:class:`JointGrid` instance\nReturns ``self`` for easy method chaining.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "x": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "y": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "color": {
                    "type": "string",
                    "default": ".5",
                    "description": "类型从默认值推断: str"
                },
                "linestyle": {
                    "type": "string",
                    "default": "--",
                    "description": "类型从默认值推断: str"
                },
                "line_kws": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "line_kws"
            ]
        }
    },
    {
        "name": "seaborn_categorical_stripplot",
        "description": "Draw a categorical scatterplot using jitter to reduce overplotting.\nA strip plot can be drawn on its own, but it is also a good complement\nto a box or violin plot in cases where you want to show all observations\nalong with some representation of the underlying distribution.\n.. note::\nBy default, this function treats one of the variables as categorical\nand draws data at ordinal positions (0, 1, ... n) on the relevant axis.\nThis can be disabled with the `native_scale` parameter.\nSee the :ref:`tutorial <categorical_tutorial>` for more information.\nParameters\n----------\nx, y, hue : names of variables in ``data`` or vector data, optional\nInputs for plotting long-form data. See examples for interpretation.\ndata : DataFrame, array, or list of arrays, optional\nDataset for plotting. If ``x`` and ``y`` are absent, this is\ninterpreted as wide-form. Otherwise it is expected to be long-form.\norder, hue_order : lists of strings, optional\nOrder to plot the categorical levels in; otherwise the levels are\ninferred from the data objects.\njitter : float, ``True``/``1`` is special-cased, optional\nAmount of jitter (only along the categorical axis) to apply. This\ncan be useful when you have many points and they overlap, so that\nit is easier to see the distribution. You can specify the amount\nof jitter (half the width of the uniform random variable support),\nor just use ``True`` for a good default.\ndodge : bool, optional\nWhen using ``hue`` nesting, setting this to ``True`` will separate\nthe strips for different hue levels along the categorical axis.\nOtherwise, the points for each level will be plotted on top of\neach other.\norient : \"v\" | \"h\", optional\nOrientation of the plot (vertical or horizontal). This is usually\ninferred based on the type of the input variables, but it can be used\nto resolve ambiguity when both `x` and `y` are numeric or when\nplotting wide-form data.\ncolor : matplotlib color, optional\nSingle color for the elements in the plot.\npalette : palette name, list, or dict\nColors to use for the different levels of the ``hue`` variable. Should\nbe something that can be interpreted by :func:`color_palette`, or a\ndictionary mapping hue levels to matplotlib colors.\nsize : float, optional\nRadius of the markers, in points.\nedgecolor : matplotlib color, \"gray\" is special-cased, optional\nColor of the lines around each point. If you pass ``\"gray\"``, the\nbrightness is determined by the color palette used for the body\nof the points. Note that `stripplot` has `linewidth=0` by default,\nso edge colors are only visible with nonzero line width.\nlinewidth : float, optional\nWidth of the gray lines that frame the plot elements.\nnative_scale : bool, optional\nWhen True, numeric or datetime values on the categorical axis will maintain\ntheir original scaling rather than being converted to fixed indices.\nformatter : callable, optional\nFunction for converting categorical data into strings. Affects both grouping\nand tick labels.\nlegend : \"auto\", \"brief\", \"full\", or False\nHow to draw the legend. If \"brief\", numeric `hue` and `size`\nvariables will be represented with a sample of evenly spaced values.\nIf \"full\", every group will get an entry in the legend. If \"auto\",\nchoose between brief or full representation based on number of levels.\nIf `False`, no legend data is added and no legend is drawn.\nax : matplotlib Axes, optional\nAxes object to draw the plot onto, otherwise uses the current Axes.\nkwargs : key, value mappings\nOther keyword arguments are passed through to\n:meth:`matplotlib.axes.Axes.scatter`.\nReturns\n-------\nax : matplotlib Axes\nReturns the Axes object with the plot drawn onto it.\nSee Also\n--------\nswarmplot : A categorical scatterplot where the points do not overlap. Can\nbe used with other plots to show each observation.\nboxplot : A traditional box-and-whisker plot with a similar API.\nviolinplot : A combination of boxplot and kernel density estimation.\ncatplot : Combine a categorical plot with a :class:`FacetGrid`.\nExamples\n--------\n.. include:: ../docstrings/stripplot.rst",
        "inputSchema": {
            "type": "object",
            "properties": {
                "data": {
                    "type": "object",
                    "description": "类型从参数名推断: data"
                },
                "x": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "y": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "hue": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "order": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "hue_order": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "jitter": {
                    "type": "integer",
                    "default": True,
                    "description": "类型从默认值推断: bool"
                },
                "dodge": {
                    "type": "integer",
                    "default": False,
                    "description": "类型从默认值推断: bool"
                },
                "orient": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "color": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "palette": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "size": {
                    "type": "integer",
                    "default": 5,
                    "description": "类型从默认值推断: int"
                },
                "edgecolor": {
                    "type": "string",
                    "default": "gray",
                    "description": "类型从默认值推断: str"
                },
                "linewidth": {
                    "type": "integer",
                    "default": 0,
                    "description": "类型从默认值推断: int"
                },
                "hue_norm": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "native_scale": {
                    "type": "integer",
                    "default": False,
                    "description": "类型从默认值推断: bool"
                },
                "formatter": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "legend": {
                    "type": "string",
                    "default": "auto",
                    "description": "类型从默认值推断: str"
                },
                "ax": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "kwargs"
            ]
        }
    },
    {
        "name": "seaborn_axisgrid_Grid_tick_params",
        "description": "Modify the ticks, tick labels, and gridlines.\nParameters\n----------\naxis : {'x', 'y', 'both'}\nThe axis on which to apply the formatting.\nkwargs : keyword arguments\nAdditional keyword arguments to pass to\n:meth:`matplotlib.axes.Axes.tick_params`.\nReturns\n-------\nself : Grid instance\nReturns self for easy chaining.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "axis": {
                    "type": "string",
                    "default": "both",
                    "description": "类型从默认值推断: str"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "kwargs"
            ]
        }
    },
    {
        "name": "seaborn_axisgrid_PairGrid_savefig",
        "description": "Save an image of the plot.\nThis wraps :meth:`matplotlib.figure.Figure.savefig`, using bbox_inches=\"tight\"\nby default. Parameters are passed through to the matplotlib function.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "args": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "args",
                "kwargs"
            ]
        }
    },
    {
        "name": "seaborn_external_docscrape_NumpyDocString_get",
        "description": "D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "key": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "default": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "key"
            ]
        }
    },
    {
        "name": "seaborn_categorical_boxplot",
        "description": "Draw a box plot to show distributions with respect to categories.\nA box plot (or box-and-whisker plot) shows the distribution of quantitative\ndata in a way that facilitates comparisons between variables or across\nlevels of a categorical variable. The box shows the quartiles of the\ndataset while the whiskers extend to show the rest of the distribution,\nexcept for points that are determined to be \"outliers\" using a method\nthat is a function of the inter-quartile range.\n.. note::\nThis function always treats one of the variables as categorical and\ndraws data at ordinal positions (0, 1, ... n) on the relevant axis,\neven when the data has a numeric or date type.\nSee the :ref:`tutorial <categorical_tutorial>` for more information.\nParameters\n----------\ndata : DataFrame, array, or list of arrays, optional\nDataset for plotting. If ``x`` and ``y`` are absent, this is\ninterpreted as wide-form. Otherwise it is expected to be long-form.\nx, y, hue : names of variables in ``data`` or vector data, optional\nInputs for plotting long-form data. See examples for interpretation.\norder, hue_order : lists of strings, optional\nOrder to plot the categorical levels in; otherwise the levels are\ninferred from the data objects.\norient : \"v\" | \"h\", optional\nOrientation of the plot (vertical or horizontal). This is usually\ninferred based on the type of the input variables, but it can be used\nto resolve ambiguity when both `x` and `y` are numeric or when\nplotting wide-form data.\ncolor : matplotlib color, optional\nSingle color for the elements in the plot.\npalette : palette name, list, or dict\nColors to use for the different levels of the ``hue`` variable. Should\nbe something that can be interpreted by :func:`color_palette`, or a\ndictionary mapping hue levels to matplotlib colors.\nsaturation : float, optional\nProportion of the original saturation to draw colors at. Large patches\noften look better with slightly desaturated colors, but set this to\n`1` if you want the plot colors to perfectly match the input color.\nwidth : float, optional\nWidth of a full element when not using hue nesting, or width of all the\nelements for one level of the major grouping variable.\ndodge : bool, optional\nWhen hue nesting is used, whether elements should be shifted along the\ncategorical axis.\nfliersize : float, optional\nSize of the markers used to indicate outlier observations.\nlinewidth : float, optional\nWidth of the gray lines that frame the plot elements.\nwhis : float, optional\nMaximum length of the plot whiskers as proportion of the\ninterquartile range. Whiskers extend to the furthest datapoint\nwithin that range. More extreme points are marked as outliers.\nax : matplotlib Axes, optional\nAxes object to draw the plot onto, otherwise uses the current Axes.\nkwargs : key, value mappings\nOther keyword arguments are passed through to\n:meth:`matplotlib.axes.Axes.boxplot`.\nReturns\n-------\nax : matplotlib Axes\nReturns the Axes object with the plot drawn onto it.\nSee Also\n--------\nviolinplot : A combination of boxplot and kernel density estimation.\nstripplot : A scatterplot where one variable is categorical. Can be used\nin conjunction with other plots to show each observation.\nswarmplot : A categorical scatterplot where the points do not overlap. Can\nbe used with other plots to show each observation.\ncatplot : Combine a categorical plot with a :class:`FacetGrid`.\nExamples\n--------\n.. include:: ../docstrings/boxplot.rst",
        "inputSchema": {
            "type": "object",
            "properties": {
                "data": {
                    "type": "object",
                    "description": "类型从参数名推断: data"
                },
                "x": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "y": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "hue": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "order": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "hue_order": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "orient": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "color": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "palette": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "saturation": {
                    "type": "number",
                    "default": 0.75,
                    "description": "类型从默认值推断: float"
                },
                "width": {
                    "type": "number",
                    "default": 0.8,
                    "description": "类型从默认值推断: float"
                },
                "dodge": {
                    "type": "integer",
                    "default": True,
                    "description": "类型从默认值推断: bool"
                },
                "fliersize": {
                    "type": "integer",
                    "default": 5,
                    "description": "类型从默认值推断: int"
                },
                "linewidth": {
                    "type": "integer",
                    "description": "类型从参数名推断: linewidth"
                },
                "whis": {
                    "type": "number",
                    "default": 1.5,
                    "description": "类型从默认值推断: float"
                },
                "ax": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "kwargs"
            ]
        }
    },
    {
        "name": "seaborn_distributions_rugplot",
        "description": "Plot marginal distributions by drawing ticks along the x and y axes.\nThis function is intended to complement other plots by showing the location\nof individual observations in an unobtrusive way.\nParameters\n----------\ndata : :class:`pandas.DataFrame`, :class:`numpy.ndarray`, mapping, or sequence\nInput data structure. Either a long-form collection of vectors that can be\nassigned to named variables or a wide-form dataset that will be internally\nreshaped.\nx, y : vectors or keys in ``data``\nVariables that specify positions on the x and y axes.\nhue : vector or key in ``data``\nSemantic variable that is mapped to determine the color of plot elements.\nheight : float\nProportion of axes extent covered by each rug element. Can be negative.\nexpand_margins : bool\nIf True, increase the axes margins by the height of the rug to avoid\noverlap with other elements.\npalette : string, list, dict, or :class:`matplotlib.colors.Colormap`\nMethod for choosing the colors to use when mapping the ``hue`` semantic.\nString values are passed to :func:`color_palette`. List or dict values\nimply categorical mapping, while a colormap object implies numeric mapping.\nhue_order : vector of strings\nSpecify the order of processing and plotting for categorical levels of the\n``hue`` semantic.\nhue_norm : tuple or :class:`matplotlib.colors.Normalize`\nEither a pair of values that set the normalization range in data units\nor an object that will map from data units into a [0, 1] interval. Usage\nimplies numeric mapping.\nlegend : bool\nIf False, do not add a legend for semantic variables.\nax : :class:`matplotlib.axes.Axes`\nPre-existing axes for the plot. Otherwise, call :func:`matplotlib.pyplot.gca`\ninternally.\nkwargs\nOther keyword arguments are passed to\n:meth:`matplotlib.collections.LineCollection`\nReturns\n-------\n:class:`matplotlib.axes.Axes`\nThe matplotlib axes containing the plot.\nExamples\n--------\n.. include:: ../docstrings/rugplot.rst",
        "inputSchema": {
            "type": "object",
            "properties": {
                "data": {
                    "type": "object",
                    "description": "类型从参数名推断: data"
                },
                "x": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "y": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "hue": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "height": {
                    "type": "number",
                    "default": 0.025,
                    "description": "类型从默认值推断: float"
                },
                "expand_margins": {
                    "type": "integer",
                    "default": True,
                    "description": "类型从默认值推断: bool"
                },
                "palette": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "hue_order": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "hue_norm": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "legend": {
                    "type": "integer",
                    "default": True,
                    "description": "类型从默认值推断: bool"
                },
                "ax": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "kwargs"
            ]
        }
    },
    {
        "name": "seaborn_axisgrid_Grid_savefig",
        "description": "Save an image of the plot.\nThis wraps :meth:`matplotlib.figure.Figure.savefig`, using bbox_inches=\"tight\"\nby default. Parameters are passed through to the matplotlib function.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "args": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "args",
                "kwargs"
            ]
        }
    },
    {
        "name": "seaborn_matrix_ClusterGrid_format_data",
        "description": "Extract variables from data or use directly.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "data": {
                    "type": "object",
                    "description": "类型从参数名推断: data"
                },
                "pivot_kws": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "z_score": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "standard_scale": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "data",
                "pivot_kws"
            ]
        }
    },
    {
        "name": "seaborn_categorical_Beeswarm_could_overlap",
        "description": "Return a list of all swarm points that could overlap with target.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "xyr_i": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "swarm": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "xyr_i",
                "swarm"
            ]
        }
    },
    {
        "name": "seaborn_axisgrid_FacetGrid_apply",
        "description": "Pass the grid to a user-supplied function and return self.\nThe `func` must accept an object of this type for its first\npositional argument. Additional arguments are passed through.\nThe return value of `func` is ignored; this method returns self.\nSee the `pipe` method if you want the return value.\nAdded in v0.12.0.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "func": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "args": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "func",
                "args",
                "kwargs"
            ]
        }
    },
    {
        "name": "seaborn_axisgrid_JointGrid_savefig",
        "description": "Save an image of the plot.\nThis wraps :meth:`matplotlib.figure.Figure.savefig`, using bbox_inches=\"tight\"\nby default. Parameters are passed through to the matplotlib function.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "args": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "args",
                "kwargs"
            ]
        }
    },
    {
        "name": "seaborn_axisgrid_FacetGrid_map",
        "description": "Apply a plotting function to each facet's subset of the data.\nParameters\n----------\nfunc : callable\nA plotting function that takes data and keyword arguments. It\nmust plot to the currently active matplotlib Axes and take a\n`color` keyword argument. If faceting on the `hue` dimension,\nit must also take a `label` keyword argument.\nargs : strings\nColumn names in self.data that identify variables with data to\nplot. The data for each variable is passed to `func` in the\norder the variables are specified in the call.\nkwargs : keyword arguments\nAll keyword arguments are passed to the plotting function.\nReturns\n-------\nself : object\nReturns self.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "func": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "args": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "func",
                "args",
                "kwargs"
            ]
        }
    },
    {
        "name": "seaborn_external_docscrape_NumpyDocString_keys",
        "description": "D.keys() -> a set-like object providing a view on D's keys",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "seaborn_axisgrid_PairGrid_map_offdiag",
        "description": "Plot with a bivariate function on the off-diagonal subplots.\nParameters\n----------\nfunc : callable plotting function\nMust take x, y arrays as positional arguments and draw onto the\n\"currently active\" matplotlib Axes. Also needs to accept kwargs\ncalled ``color`` and  ``label``.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "func": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "func",
                "kwargs"
            ]
        }
    },
    {
        "name": "seaborn_axisgrid_FacetGrid_set_titles",
        "description": "Draw titles either above each facet or on the grid margins.\nParameters\n----------\ntemplate : string\nTemplate for all titles with the formatting keys {col_var} and\n{col_name} (if using a `col` faceting variable) and/or {row_var}\nand {row_name} (if using a `row` faceting variable).\nrow_template:\nTemplate for the row variable when titles are drawn on the grid\nmargins. Must have {row_var} and {row_name} formatting keys.\ncol_template:\nTemplate for the column variable when titles are drawn on the grid\nmargins. Must have {col_var} and {col_name} formatting keys.\nReturns\n-------\nself: object\nReturns self.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "template": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "row_template": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "col_template": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "kwargs"
            ]
        }
    },
    {
        "name": "seaborn_axisgrid_FacetGrid_set_yticklabels",
        "description": "Set y axis tick labels on the left column of the grid.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "labels": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "kwargs"
            ]
        }
    },
    {
        "name": "seaborn_axisgrid_FacetGrid_map_dataframe",
        "description": "Like ``.map`` but passes args as strings and inserts data in kwargs.\nThis method is suitable for plotting with functions that accept a\nlong-form DataFrame as a `data` keyword argument and access the\ndata in that DataFrame using string variable names.\nParameters\n----------\nfunc : callable\nA plotting function that takes data and keyword arguments. Unlike\nthe `map` method, a function used here must \"understand\" Pandas\nobjects. It also must plot to the currently active matplotlib Axes\nand take a `color` keyword argument. If faceting on the `hue`\ndimension, it must also take a `label` keyword argument.\nargs : strings\nColumn names in self.data that identify variables with data to\nplot. The data for each variable is passed to `func` in the\norder the variables are specified in the call.\nkwargs : keyword arguments\nAll keyword arguments are passed to the plotting function.\nReturns\n-------\nself : object\nReturns self.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "func": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "args": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "func",
                "args",
                "kwargs"
            ]
        }
    },
    {
        "name": "seaborn_external_docscrape_NumpyDocString_items",
        "description": "D.items() -> a set-like object providing a view on D's items",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "seaborn_axisgrid_JointGrid_pipe",
        "description": "Pass the grid to a user-supplied function and return its value.\nThe `func` must accept an object of this type for its first\npositional argument. Additional arguments are passed through.\nThe return value of `func` becomes the return value of this method.\nSee the `apply` method if you want to return self instead.\nAdded in v0.12.0.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "func": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "args": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "func",
                "args",
                "kwargs"
            ]
        }
    },
    {
        "name": "seaborn_categorical_Beeswarm_first_non_overlapping_candidate",
        "description": "Find the first candidate that does not overlap with the swarm.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "candidates": {
                    "type": "integer",
                    "description": "类型从参数名推断: candidates"
                },
                "neighbors": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "candidates",
                "neighbors"
            ]
        }
    },
    {
        "name": "seaborn_axisgrid_FacetGrid_facet_axis",
        "description": "Make the axis identified by these indices active and return it.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "row_i": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "col_j": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "modify_state": {
                    "type": "integer",
                    "default": True,
                    "description": "类型从默认值推断: bool"
                }
            },
            "required": [
                "row_i",
                "col_j"
            ]
        }
    },
    {
        "name": "seaborn_algorithms_bootstrap",
        "description": "Resample one or more arrays with replacement and store aggregate values.\nPositional arguments are a sequence of arrays to bootstrap along the first\naxis and pass to a summary function.\nKeyword arguments:\nn_boot : int, default=10000\nNumber of iterations\naxis : int, default=None\nWill pass axis to ``func`` as a keyword argument.\nunits : array, default=None\nArray of sampling unit IDs. When used the bootstrap resamples units\nand then observations within units instead of individual\ndatapoints.\nfunc : string or callable, default=\"mean\"\nFunction to call on the args that are passed in. If string, uses as\nname of function in the numpy namespace. If nans are present in the\ndata, will try to use nan-aware version of named function.\nseed : Generator | SeedSequence | RandomState | int | None\nSeed for the random number generator; useful if you want\nreproducible resamples.\nReturns\n-------\nboot_dist: array\narray of bootstrapped statistic values",
        "inputSchema": {
            "type": "object",
            "properties": {
                "args": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "args",
                "kwargs"
            ]
        }
    },
    {
        "name": "seaborn_utils_get_dataset_names",
        "description": "Report available example datasets, useful for reporting issues.\nRequires an internet connection.",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "seaborn_external_docscrape_FunctionDoc_get",
        "description": "D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "key": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "default": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "key"
            ]
        }
    },
    {
        "name": "seaborn_axisgrid_PairGrid_add_legend",
        "description": "Draw a legend, maybe placing it outside axes and resizing the figure.\nParameters\n----------\nlegend_data : dict\nDictionary mapping label names (or two-element tuples where the\nsecond element is a label name) to matplotlib artist handles. The\ndefault reads from ``self._legend_data``.\ntitle : string\nTitle for the legend. The default reads from ``self._hue_var``.\nlabel_order : list of labels\nThe order that the legend entries should appear in. The default\nreads from ``self.hue_names``.\nadjust_subtitles : bool\nIf True, modify entries with invisible artists to left-align\nthe labels and set the font size to that of a title.\nkwargs : key, value pairings\nOther keyword arguments are passed to the underlying legend methods\non the Figure or Axes object.\nReturns\n-------\nself : Grid instance\nReturns self for easy chaining.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "legend_data": {
                    "type": "object",
                    "description": "类型从参数名推断: legend_data"
                },
                "title": {
                    "type": "string",
                    "description": "类型从参数名推断: title"
                },
                "label_order": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "adjust_subtitles": {
                    "type": "integer",
                    "default": False,
                    "description": "类型从默认值推断: bool"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "kwargs"
            ]
        }
    },
    {
        "name": "seaborn_axisgrid_FacetGrid_add_legend",
        "description": "Draw a legend, maybe placing it outside axes and resizing the figure.\nParameters\n----------\nlegend_data : dict\nDictionary mapping label names (or two-element tuples where the\nsecond element is a label name) to matplotlib artist handles. The\ndefault reads from ``self._legend_data``.\ntitle : string\nTitle for the legend. The default reads from ``self._hue_var``.\nlabel_order : list of labels\nThe order that the legend entries should appear in. The default\nreads from ``self.hue_names``.\nadjust_subtitles : bool\nIf True, modify entries with invisible artists to left-align\nthe labels and set the font size to that of a title.\nkwargs : key, value pairings\nOther keyword arguments are passed to the underlying legend methods\non the Figure or Axes object.\nReturns\n-------\nself : Grid instance\nReturns self for easy chaining.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "legend_data": {
                    "type": "object",
                    "description": "类型从参数名推断: legend_data"
                },
                "title": {
                    "type": "string",
                    "description": "类型从参数名推断: title"
                },
                "label_order": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "adjust_subtitles": {
                    "type": "integer",
                    "default": False,
                    "description": "类型从默认值推断: bool"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "kwargs"
            ]
        }
    },
    {
        "name": "seaborn_axisgrid_PairGrid_tick_params",
        "description": "Modify the ticks, tick labels, and gridlines.\nParameters\n----------\naxis : {'x', 'y', 'both'}\nThe axis on which to apply the formatting.\nkwargs : keyword arguments\nAdditional keyword arguments to pass to\n:meth:`matplotlib.axes.Axes.tick_params`.\nReturns\n-------\nself : Grid instance\nReturns self for easy chaining.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "axis": {
                    "type": "string",
                    "default": "both",
                    "description": "类型从默认值推断: str"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "kwargs"
            ]
        }
    },
    {
        "name": "seaborn_external_docscrape_strip_blank_lines",
        "description": "Remove leading and trailing blank lines from a list of lines",
        "inputSchema": {
            "type": "object",
            "properties": {
                "l": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "l"
            ]
        }
    },
    {
        "name": "seaborn_axisgrid_jointplot",
        "description": "Draw a plot of two variables with bivariate and univariate graphs.\nThis function provides a convenient interface to the :class:`JointGrid`\nclass, with several canned plot kinds. This is intended to be a fairly\nlightweight wrapper; if you need more flexibility, you should use\n:class:`JointGrid` directly.\nParameters\n----------\ndata : :class:`pandas.DataFrame`, :class:`numpy.ndarray`, mapping, or sequence\nInput data structure. Either a long-form collection of vectors that can be\nassigned to named variables or a wide-form dataset that will be internally\nreshaped.\nx, y : vectors or keys in ``data``\nVariables that specify positions on the x and y axes.\nhue : vector or key in ``data``\nSemantic variable that is mapped to determine the color of plot elements.\nSemantic variable that is mapped to determine the color of plot elements.\nkind : { \"scatter\" | \"kde\" | \"hist\" | \"hex\" | \"reg\" | \"resid\" }\nKind of plot to draw. See the examples for references to the underlying functions.\nheight : numeric\nSize of the figure (it will be square).\nratio : numeric\nRatio of joint axes height to marginal axes height.\nspace : numeric\nSpace between the joint and marginal axes\ndropna : bool\nIf True, remove observations that are missing from ``x`` and ``y``.\n{x, y}lim : pairs of numbers\nAxis limits to set before plotting.\ncolor : :mod:`matplotlib color <matplotlib.colors>`\nSingle color specification for when hue mapping is not used. Otherwise, the\nplot will try to hook into the matplotlib property cycle.\npalette : string, list, dict, or :class:`matplotlib.colors.Colormap`\nMethod for choosing the colors to use when mapping the ``hue`` semantic.\nString values are passed to :func:`color_palette`. List or dict values\nimply categorical mapping, while a colormap object implies numeric mapping.\nhue_order : vector of strings\nSpecify the order of processing and plotting for categorical levels of the\n``hue`` semantic.\nhue_norm : tuple or :class:`matplotlib.colors.Normalize`\nEither a pair of values that set the normalization range in data units\nor an object that will map from data units into a [0, 1] interval. Usage\nimplies numeric mapping.\nmarginal_ticks : bool\nIf False, suppress ticks on the count/density axis of the marginal plots.\n{joint, marginal}_kws : dicts\nAdditional keyword arguments for the plot components.\nkwargs\nAdditional keyword arguments are passed to the function used to\ndraw the plot on the joint Axes, superseding items in the\n``joint_kws`` dictionary.\nReturns\n-------\n:class:`JointGrid`\nAn object managing multiple subplots that correspond to joint and marginal axes\nfor plotting a bivariate relationship or distribution.\nSee Also\n--------\nJointGrid : Set up a figure with joint and marginal views on bivariate data.\nPairGrid : Set up a figure with joint and marginal views on multiple variables.\njointplot : Draw multiple bivariate plots with univariate marginal distributions.\nExamples\n--------\n.. include:: ../docstrings/jointplot.rst",
        "inputSchema": {
            "type": "object",
            "properties": {
                "data": {
                    "type": "object",
                    "description": "类型从参数名推断: data"
                },
                "x": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "y": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "hue": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kind": {
                    "type": "string",
                    "default": "scatter",
                    "description": "类型从默认值推断: str"
                },
                "height": {
                    "type": "integer",
                    "default": 6,
                    "description": "类型从默认值推断: int"
                },
                "ratio": {
                    "type": "integer",
                    "default": 5,
                    "description": "类型从默认值推断: int"
                },
                "space": {
                    "type": "number",
                    "default": 0.2,
                    "description": "类型从默认值推断: float"
                },
                "dropna": {
                    "type": "integer",
                    "default": False,
                    "description": "类型从默认值推断: bool"
                },
                "xlim": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "ylim": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "color": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "palette": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "hue_order": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "hue_norm": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "marginal_ticks": {
                    "type": "integer",
                    "default": False,
                    "description": "类型从默认值推断: bool"
                },
                "joint_kws": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "marginal_kws": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "kwargs"
            ]
        }
    },
    {
        "name": "seaborn_axisgrid_FacetGrid_set_axis_labels",
        "description": "Set axis labels on the left column and bottom row of the grid.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "x_var": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "y_var": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "clear_inner": {
                    "type": "integer",
                    "default": True,
                    "description": "类型从默认值推断: bool"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "kwargs"
            ]
        }
    },
    {
        "name": "seaborn_axisgrid_JointGrid_plot_joint",
        "description": "Draw a bivariate plot on the joint axes of the grid.\nParameters\n----------\nfunc : plotting callable\nIf a seaborn function, it should accept ``x`` and ``y``. Otherwise,\nit must accept ``x`` and ``y`` vectors of data as the first two\npositional arguments, and it must plot on the \"current\" axes.\nIf ``hue`` was defined in the class constructor, the function must\naccept ``hue`` as a parameter.\nkwargs\nKeyword argument are passed to the plotting function.\nReturns\n-------\n:class:`JointGrid` instance\nReturns ``self`` for easy method chaining.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "func": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "func",
                "kwargs"
            ]
        }
    },
    {
        "name": "seaborn_external_appdirs_user_cache_dir",
        "description": "Return full path to the user-specific cache dir for this application.\n\"appname\" is the name of application.\nIf None, just the system directory is returned.\n\"appauthor\" (only used on Windows) is the name of the\nappauthor or distributing body for this application. Typically\nit is the owning company name. This falls back to appname. You may\npass False to disable it.\n\"version\" is an optional version path element to append to the\npath. You might want to use this if you want multiple versions\nof your app to be able to run independently. If used, this\nwould typically be \"<major>.<minor>\".\nOnly applied when appname is present.\n\"opinion\" (boolean) can be False to disable the appending of\n\"Cache\" to the base app data dir for Windows. See\ndiscussion below.\nTypical user cache directories are:\nMac OS X:   ~/Library/Caches/<AppName>\nUnix:       ~/.cache/<AppName> (XDG default)\nWin XP:     C:\\Documents and Settings\\<username>\\Local Settings\\Application Data\\<AppAuthor>\\<AppName>\\Cache\nVista:      C:\\Users\\<username>\\AppData\\Local\\<AppAuthor>\\<AppName>\\Cache\nOn Windows the only suggestion in the MSDN docs is that local settings go in\nthe `CSIDL_LOCAL_APPDATA` directory. This is identical to the non-roaming\napp data dir (the default returned by `user_data_dir` above). Apps typically\nput cache data somewhere *under* the given dir here. Some examples:\n...\\Mozilla\\Firefox\\Profiles\\<ProfileName>\\Cache\n...\\Acme\\SuperApp\\Cache\\1.0\nOPINION: This function appends \"Cache\" to the `CSIDL_LOCAL_APPDATA` value.\nThis can be disabled with the `opinion=False` option.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "appname": {
                    "type": "string",
                    "description": "类型从参数名推断: appname"
                },
                "appauthor": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "version": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "opinion": {
                    "type": "integer",
                    "default": True,
                    "description": "类型从默认值推断: bool"
                }
            },
            "required": []
        }
    },
    {
        "name": "seaborn_widgets_choose_light_palette",
        "description": "Launch an interactive widget to create a light sequential palette.\nThis corresponds with the :func:`light_palette` function. This kind\nof palette is good for data that range between relatively uninteresting\nlow values and interesting high values.\nRequires IPython 2+ and must be used in the notebook.\nParameters\n----------\ninput : {'husl', 'hls', 'rgb'}\nColor space for defining the seed value. Note that the default is\ndifferent than the default input for :func:`light_palette`.\nas_cmap : bool\nIf True, the return value is a matplotlib colormap rather than a\nlist of discrete colors.\nReturns\n-------\npal or cmap : list of colors or matplotlib colormap\nObject that can be passed to plotting functions.\nSee Also\n--------\nlight_palette : Create a sequential palette with bright low values.\ndark_palette : Create a sequential palette with dark low values.\ncubehelix_palette : Create a sequential palette or colormap using the\ncubehelix system.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "input": {
                    "type": "string",
                    "default": "husl",
                    "description": "类型从默认值推断: str"
                },
                "as_cmap": {
                    "type": "integer",
                    "default": False,
                    "description": "类型从默认值推断: bool"
                }
            },
            "required": []
        }
    },
    {
        "name": "seaborn_external_docscrape_ClassDoc_values",
        "description": "D.values() -> an object providing a view on D's values",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "seaborn_axisgrid_JointGrid_plot",
        "description": "Draw the plot by passing functions for joint and marginal axes.\nThis method passes the ``kwargs`` dictionary to both functions. If you\nneed more control, call :meth:`JointGrid.plot_joint` and\n:meth:`JointGrid.plot_marginals` directly with specific parameters.\nParameters\n----------\njoint_func, marginal_func : callables\nFunctions to draw the bivariate and univariate plots. See methods\nreferenced above for information about the required characteristics\nof these functions.\nkwargs\nAdditional keyword arguments are passed to both functions.\nReturns\n-------\n:class:`JointGrid` instance\nReturns ``self`` for easy method chaining.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "joint_func": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "marginal_func": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "joint_func",
                "marginal_func",
                "kwargs"
            ]
        }
    },
    {
        "name": "seaborn_axisgrid_Grid_apply",
        "description": "Pass the grid to a user-supplied function and return self.\nThe `func` must accept an object of this type for its first\npositional argument. Additional arguments are passed through.\nThe return value of `func` is ignored; this method returns self.\nSee the `pipe` method if you want the return value.\nAdded in v0.12.0.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "func": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "args": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "func",
                "args",
                "kwargs"
            ]
        }
    },
    {
        "name": "seaborn_axisgrid_JointGrid_apply",
        "description": "Pass the grid to a user-supplied function and return self.\nThe `func` must accept an object of this type for its first\npositional argument. Additional arguments are passed through.\nThe return value of `func` is ignored; this method returns self.\nSee the `pipe` method if you want the return value.\nAdded in v0.12.0.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "func": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "args": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "func",
                "args",
                "kwargs"
            ]
        }
    },
    {
        "name": "seaborn_axisgrid_FacetGrid_tick_params",
        "description": "Modify the ticks, tick labels, and gridlines.\nParameters\n----------\naxis : {'x', 'y', 'both'}\nThe axis on which to apply the formatting.\nkwargs : keyword arguments\nAdditional keyword arguments to pass to\n:meth:`matplotlib.axes.Axes.tick_params`.\nReturns\n-------\nself : Grid instance\nReturns self for easy chaining.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "axis": {
                    "type": "string",
                    "default": "both",
                    "description": "类型从默认值推断: str"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "kwargs"
            ]
        }
    },
    {
        "name": "seaborn_axisgrid_PairGrid_map",
        "description": "Plot with the same function in every subplot.\nParameters\n----------\nfunc : callable plotting function\nMust take x, y arrays as positional arguments and draw onto the\n\"currently active\" matplotlib Axes. Also needs to accept kwargs\ncalled ``color`` and  ``label``.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "func": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "args": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "func",
                "args",
                "kwargs"
            ]
        }
    },
    {
        "name": "seaborn_external_docscrape_ClassDoc_items",
        "description": "D.items() -> a set-like object providing a view on D's items",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "seaborn_axisgrid_FacetGrid_tight_layout",
        "description": "Call fig.tight_layout within rect that exclude the legend.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "args": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "args",
                "kwargs"
            ]
        }
    },
    {
        "name": "seaborn_axisgrid_JointGrid_plot_marginals",
        "description": "Draw univariate plots on each marginal axes.\nParameters\n----------\nfunc : plotting callable\nIf a seaborn function, it should  accept ``x`` and ``y`` and plot\nwhen only one of them is defined. Otherwise, it must accept a vector\nof data as the first positional argument and determine its orientation\nusing the ``vertical`` parameter, and it must plot on the \"current\" axes.\nIf ``hue`` was defined in the class constructor, it must accept ``hue``\nas a parameter.\nkwargs\nKeyword argument are passed to the plotting function.\nReturns\n-------\n:class:`JointGrid` instance\nReturns ``self`` for easy method chaining.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "func": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "func",
                "kwargs"
            ]
        }
    },
    {
        "name": "seaborn_axisgrid_PairGrid_tight_layout",
        "description": "Call fig.tight_layout within rect that exclude the legend.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "args": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "args",
                "kwargs"
            ]
        }
    },
    {
        "name": "seaborn_widgets_choose_dark_palette",
        "description": "Launch an interactive widget to create a dark sequential palette.\nThis corresponds with the :func:`dark_palette` function. This kind\nof palette is good for data that range between relatively uninteresting\nlow values and interesting high values.\nRequires IPython 2+ and must be used in the notebook.\nParameters\n----------\ninput : {'husl', 'hls', 'rgb'}\nColor space for defining the seed value. Note that the default is\ndifferent than the default input for :func:`dark_palette`.\nas_cmap : bool\nIf True, the return value is a matplotlib colormap rather than a\nlist of discrete colors.\nReturns\n-------\npal or cmap : list of colors or matplotlib colormap\nObject that can be passed to plotting functions.\nSee Also\n--------\ndark_palette : Create a sequential palette with dark low values.\nlight_palette : Create a sequential palette with bright low values.\ncubehelix_palette : Create a sequential palette or colormap using the\ncubehelix system.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "input": {
                    "type": "string",
                    "default": "husl",
                    "description": "类型从默认值推断: str"
                },
                "as_cmap": {
                    "type": "integer",
                    "default": False,
                    "description": "类型从默认值推断: bool"
                }
            },
            "required": []
        }
    },
    {
        "name": "seaborn_categorical_swarmplot",
        "description": "Draw a categorical scatterplot with points adjusted to be non-overlapping.\nThis function is similar to :func:`stripplot`, but the points are adjusted\n(only along the categorical axis) so that they don't overlap. This gives a\nbetter representation of the distribution of values, but it does not scale\nwell to large numbers of observations. This style of plot is sometimes\ncalled a \"beeswarm\".\nA swarm plot can be drawn on its own, but it is also a good complement\nto a box or violin plot in cases where you want to show all observations\nalong with some representation of the underlying distribution.\n.. note::\nBy default, this function treats one of the variables as categorical\nand draws data at ordinal positions (0, 1, ... n) on the relevant axis.\nThis can be disabled with the `native_scale` parameter.\nSee the :ref:`tutorial <categorical_tutorial>` for more information.\nParameters\n----------\ndata : DataFrame, array, or list of arrays, optional\nDataset for plotting. If ``x`` and ``y`` are absent, this is\ninterpreted as wide-form. Otherwise it is expected to be long-form.\nx, y, hue : names of variables in ``data`` or vector data, optional\nInputs for plotting long-form data. See examples for interpretation.\norder, hue_order : lists of strings, optional\nOrder to plot the categorical levels in; otherwise the levels are\ninferred from the data objects.\ndodge : bool, optional\nWhen using ``hue`` nesting, setting this to ``True`` will separate\nthe strips for different hue levels along the categorical axis.\nOtherwise, the points for each level will be plotted in one swarm.\norient : \"v\" | \"h\", optional\nOrientation of the plot (vertical or horizontal). This is usually\ninferred based on the type of the input variables, but it can be used\nto resolve ambiguity when both `x` and `y` are numeric or when\nplotting wide-form data.\ncolor : matplotlib color, optional\nSingle color for the elements in the plot.\npalette : palette name, list, or dict\nColors to use for the different levels of the ``hue`` variable. Should\nbe something that can be interpreted by :func:`color_palette`, or a\ndictionary mapping hue levels to matplotlib colors.\nsize : float, optional\nRadius of the markers, in points.\nedgecolor : matplotlib color, \"gray\" is special-cased, optional\nColor of the lines around each point. If you pass ``\"gray\"``, the\nbrightness is determined by the color palette used for the body\nof the points.\nlinewidth : float, optional\nWidth of the gray lines that frame the plot elements.\nnative_scale : bool, optional\nWhen True, numeric or datetime values on the categorical axis will maintain\ntheir original scaling rather than being converted to fixed indices.\nformatter : callable, optional\nFunction for converting categorical data into strings. Affects both grouping\nand tick labels.\nlegend : \"auto\", \"brief\", \"full\", or False\nHow to draw the legend. If \"brief\", numeric `hue` and `size`\nvariables will be represented with a sample of evenly spaced values.\nIf \"full\", every group will get an entry in the legend. If \"auto\",\nchoose between brief or full representation based on number of levels.\nIf `False`, no legend data is added and no legend is drawn.\nax : matplotlib Axes, optional\nAxes object to draw the plot onto, otherwise uses the current Axes.\nkwargs : key, value mappings\nOther keyword arguments are passed through to\n:meth:`matplotlib.axes.Axes.scatter`.\nReturns\n-------\nax : matplotlib Axes\nReturns the Axes object with the plot drawn onto it.\nSee Also\n--------\nboxplot : A traditional box-and-whisker plot with a similar API.\nviolinplot : A combination of boxplot and kernel density estimation.\nstripplot : A scatterplot where one variable is categorical. Can be used\nin conjunction with other plots to show each observation.\ncatplot : Combine a categorical plot with a :class:`FacetGrid`.\nExamples\n--------\n.. include:: ../docstrings/swarmplot.rst",
        "inputSchema": {
            "type": "object",
            "properties": {
                "data": {
                    "type": "object",
                    "description": "类型从参数名推断: data"
                },
                "x": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "y": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "hue": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "order": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "hue_order": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "dodge": {
                    "type": "integer",
                    "default": False,
                    "description": "类型从默认值推断: bool"
                },
                "orient": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "color": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "palette": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "size": {
                    "type": "integer",
                    "default": 5,
                    "description": "类型从默认值推断: int"
                },
                "edgecolor": {
                    "type": "string",
                    "default": "gray",
                    "description": "类型从默认值推断: str"
                },
                "linewidth": {
                    "type": "integer",
                    "default": 0,
                    "description": "类型从默认值推断: int"
                },
                "hue_norm": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "native_scale": {
                    "type": "integer",
                    "default": False,
                    "description": "类型从默认值推断: bool"
                },
                "formatter": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "legend": {
                    "type": "string",
                    "default": "auto",
                    "description": "类型从默认值推断: str"
                },
                "warn_thresh": {
                    "type": "number",
                    "default": 0.05,
                    "description": "类型从默认值推断: float"
                },
                "ax": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "kwargs"
            ]
        }
    },
    {
        "name": "seaborn_categorical_countplot",
        "description": "Show the counts of observations in each categorical bin using bars.\nA count plot can be thought of as a histogram across a categorical, instead\nof quantitative, variable. The basic API and options are identical to those\nfor :func:`barplot`, so you can compare counts across nested variables.\nNote that the newer :func:`histplot` function offers more functionality, although\nits default behavior is somewhat different.\n.. note::\nThis function always treats one of the variables as categorical and\ndraws data at ordinal positions (0, 1, ... n) on the relevant axis,\neven when the data has a numeric or date type.\nSee the :ref:`tutorial <categorical_tutorial>` for more information.\nParameters\n----------\ndata : DataFrame, array, or list of arrays, optional\nDataset for plotting. If ``x`` and ``y`` are absent, this is\ninterpreted as wide-form. Otherwise it is expected to be long-form.\nx, y, hue : names of variables in ``data`` or vector data, optional\nInputs for plotting long-form data. See examples for interpretation.\norder, hue_order : lists of strings, optional\nOrder to plot the categorical levels in; otherwise the levels are\ninferred from the data objects.\norient : \"v\" | \"h\", optional\nOrientation of the plot (vertical or horizontal). This is usually\ninferred based on the type of the input variables, but it can be used\nto resolve ambiguity when both `x` and `y` are numeric or when\nplotting wide-form data.\ncolor : matplotlib color, optional\nSingle color for the elements in the plot.\npalette : palette name, list, or dict\nColors to use for the different levels of the ``hue`` variable. Should\nbe something that can be interpreted by :func:`color_palette`, or a\ndictionary mapping hue levels to matplotlib colors.\nsaturation : float, optional\nProportion of the original saturation to draw colors at. Large patches\noften look better with slightly desaturated colors, but set this to\n`1` if you want the plot colors to perfectly match the input color.\ndodge : bool, optional\nWhen hue nesting is used, whether elements should be shifted along the\ncategorical axis.\nax : matplotlib Axes, optional\nAxes object to draw the plot onto, otherwise uses the current Axes.\nkwargs : key, value mappings\nOther keyword arguments are passed through to\n:meth:`matplotlib.axes.Axes.bar`.\nReturns\n-------\nax : matplotlib Axes\nReturns the Axes object with the plot drawn onto it.\nSee Also\n--------\nbarplot : Show point estimates and confidence intervals using bars.\ncatplot : Combine a categorical plot with a :class:`FacetGrid`.\nExamples\n--------\n.. include:: ../docstrings/countplot.rst",
        "inputSchema": {
            "type": "object",
            "properties": {
                "data": {
                    "type": "object",
                    "description": "类型从参数名推断: data"
                },
                "x": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "y": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "hue": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "order": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "hue_order": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "orient": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "color": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "palette": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "saturation": {
                    "type": "number",
                    "default": 0.75,
                    "description": "类型从默认值推断: float"
                },
                "width": {
                    "type": "number",
                    "default": 0.8,
                    "description": "类型从默认值推断: float"
                },
                "dodge": {
                    "type": "integer",
                    "default": True,
                    "description": "类型从默认值推断: bool"
                },
                "ax": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "kwargs"
            ]
        }
    },
    {
        "name": "seaborn_axisgrid_pairplot",
        "description": "Plot pairwise relationships in a dataset.\nBy default, this function will create a grid of Axes such that each numeric\nvariable in ``data`` will by shared across the y-axes across a single row and\nthe x-axes across a single column. The diagonal plots are treated\ndifferently: a univariate distribution plot is drawn to show the marginal\ndistribution of the data in each column.\nIt is also possible to show a subset of variables or plot different\nvariables on the rows and columns.\nThis is a high-level interface for :class:`PairGrid` that is intended to\nmake it easy to draw a few common styles. You should use :class:`PairGrid`\ndirectly if you need more flexibility.\nParameters\n----------\ndata : `pandas.DataFrame`\nTidy (long-form) dataframe where each column is a variable and\neach row is an observation.\nhue : name of variable in ``data``\nVariable in ``data`` to map plot aspects to different colors.\nhue_order : list of strings\nOrder for the levels of the hue variable in the palette\npalette : dict or seaborn color palette\nSet of colors for mapping the ``hue`` variable. If a dict, keys\nshould be values  in the ``hue`` variable.\nvars : list of variable names\nVariables within ``data`` to use, otherwise use every column with\na numeric datatype.\n{x, y}_vars : lists of variable names\nVariables within ``data`` to use separately for the rows and\ncolumns of the figure; i.e. to make a non-square plot.\nkind : {'scatter', 'kde', 'hist', 'reg'}\nKind of plot to make.\ndiag_kind : {'auto', 'hist', 'kde', None}\nKind of plot for the diagonal subplots. If 'auto', choose based on\nwhether or not ``hue`` is used.\nmarkers : single matplotlib marker code or list\nEither the marker to use for all scatterplot points or a list of markers\nwith a length the same as the number of levels in the hue variable so that\ndifferently colored points will also have different scatterplot\nmarkers.\nheight : scalar\nHeight (in inches) of each facet.\naspect : scalar\nAspect * height gives the width (in inches) of each facet.\ncorner : bool\nIf True, don't add axes to the upper (off-diagonal) triangle of the\ngrid, making this a \"corner\" plot.\ndropna : boolean\nDrop missing values from the data before plotting.\n{plot, diag, grid}_kws : dicts\nDictionaries of keyword arguments. ``plot_kws`` are passed to the\nbivariate plotting function, ``diag_kws`` are passed to the univariate\nplotting function, and ``grid_kws`` are passed to the :class:`PairGrid`\nconstructor.\nReturns\n-------\ngrid : :class:`PairGrid`\nReturns the underlying :class:`PairGrid` instance for further tweaking.\nSee Also\n--------\nPairGrid : Subplot grid for more flexible plotting of pairwise relationships.\nJointGrid : Grid for plotting joint and marginal distributions of two variables.\nExamples\n--------\n.. include:: ../docstrings/pairplot.rst",
        "inputSchema": {
            "type": "object",
            "properties": {
                "data": {
                    "type": "object",
                    "description": "类型从参数名推断: data"
                },
                "hue": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "hue_order": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "palette": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "vars": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "x_vars": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "y_vars": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kind": {
                    "type": "string",
                    "default": "scatter",
                    "description": "类型从默认值推断: str"
                },
                "diag_kind": {
                    "type": "string",
                    "default": "auto",
                    "description": "类型从默认值推断: str"
                },
                "markers": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "height": {
                    "type": "number",
                    "default": 2.5,
                    "description": "类型从默认值推断: float"
                },
                "aspect": {
                    "type": "integer",
                    "default": 1,
                    "description": "类型从默认值推断: int"
                },
                "corner": {
                    "type": "integer",
                    "default": False,
                    "description": "类型从默认值推断: bool"
                },
                "dropna": {
                    "type": "integer",
                    "default": False,
                    "description": "类型从默认值推断: bool"
                },
                "plot_kws": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "diag_kws": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "grid_kws": {
                    "type": "integer",
                    "description": "类型从参数名推断: grid_kws"
                },
                "size": {
                    "type": "integer",
                    "description": "类型从参数名推断: size"
                }
            },
            "required": [
                "data"
            ]
        }
    },
    {
        "name": "seaborn_axisgrid_FacetGrid_pipe",
        "description": "Pass the grid to a user-supplied function and return its value.\nThe `func` must accept an object of this type for its first\npositional argument. Additional arguments are passed through.\nThe return value of `func` becomes the return value of this method.\nSee the `apply` method if you want to return self instead.\nAdded in v0.12.0.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "func": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "args": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "func",
                "args",
                "kwargs"
            ]
        }
    },
    {
        "name": "seaborn_widgets_choose_colorbrewer_palette",
        "description": "Select a palette from the ColorBrewer set.\nThese palettes are built into matplotlib and can be used by name in\nmany seaborn functions, or by passing the object returned by this function.\nParameters\n----------\ndata_type : {'sequential', 'diverging', 'qualitative'}\nThis describes the kind of data you want to visualize. See the seaborn\ncolor palette docs for more information about how to choose this value.\nNote that you can pass substrings (e.g. 'q' for 'qualitative.\nas_cmap : bool\nIf True, the return value is a matplotlib colormap rather than a\nlist of discrete colors.\nReturns\n-------\npal or cmap : list of colors or matplotlib colormap\nObject that can be passed to plotting functions.\nSee Also\n--------\ndark_palette : Create a sequential palette with dark low values.\nlight_palette : Create a sequential palette with bright low values.\ndiverging_palette : Create a diverging palette from selected colors.\ncubehelix_palette : Create a sequential palette or colormap using the\ncubehelix system.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "data_type": {
                    "type": "object",
                    "description": "类型从参数名推断: data_type"
                },
                "as_cmap": {
                    "type": "integer",
                    "default": False,
                    "description": "类型从默认值推断: bool"
                }
            },
            "required": [
                "data_type"
            ]
        }
    },
    {
        "name": "seaborn_axisgrid_Grid_pipe",
        "description": "Pass the grid to a user-supplied function and return its value.\nThe `func` must accept an object of this type for its first\npositional argument. Additional arguments are passed through.\nThe return value of `func` becomes the return value of this method.\nSee the `apply` method if you want to return self instead.\nAdded in v0.12.0.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "func": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "args": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "func",
                "args",
                "kwargs"
            ]
        }
    },
    {
        "name": "seaborn_axisgrid_Grid_tight_layout",
        "description": "Call fig.tight_layout within rect that exclude the legend.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "args": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "args",
                "kwargs"
            ]
        }
    }
]


def handle_seaborn_distributions_distplot(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_distributions_distplot 工具调用"""
    try:
        # 解析函数路径: seaborn.distributions.distplot
        parts = "seaborn.distributions.distplot".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.distributions.distplot")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_distributions_distplot 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_external_docscrape_ClassDoc_keys(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_external_docscrape_ClassDoc_keys 工具调用"""
    try:
        # 解析函数路径: seaborn.external.docscrape.ClassDoc.keys
        parts = "seaborn.external.docscrape.ClassDoc.keys".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.external.docscrape.ClassDoc.keys")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_external_docscrape_ClassDoc_keys 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_external_docscrape_FunctionDoc_values(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_external_docscrape_FunctionDoc_values 工具调用"""
    try:
        # 解析函数路径: seaborn.external.docscrape.FunctionDoc.values
        parts = "seaborn.external.docscrape.FunctionDoc.values".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.external.docscrape.FunctionDoc.values")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_external_docscrape_FunctionDoc_values 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_external_docscrape_FunctionDoc_keys(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_external_docscrape_FunctionDoc_keys 工具调用"""
    try:
        # 解析函数路径: seaborn.external.docscrape.FunctionDoc.keys
        parts = "seaborn.external.docscrape.FunctionDoc.keys".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.external.docscrape.FunctionDoc.keys")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_external_docscrape_FunctionDoc_keys 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_widgets_choose_diverging_palette(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_widgets_choose_diverging_palette 工具调用"""
    try:
        # 解析函数路径: seaborn.widgets.choose_diverging_palette
        parts = "seaborn.widgets.choose_diverging_palette".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.widgets.choose_diverging_palette")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_widgets_choose_diverging_palette 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_external_docscrape_FunctionDoc_items(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_external_docscrape_FunctionDoc_items 工具调用"""
    try:
        # 解析函数路径: seaborn.external.docscrape.FunctionDoc.items
        parts = "seaborn.external.docscrape.FunctionDoc.items".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.external.docscrape.FunctionDoc.items")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_external_docscrape_FunctionDoc_items 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_utils_load_dataset(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_utils_load_dataset 工具调用"""
    try:
        # 解析函数路径: seaborn.utils.load_dataset
        parts = "seaborn.utils.load_dataset".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.utils.load_dataset")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_utils_load_dataset 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_widgets_choose_cubehelix_palette(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_widgets_choose_cubehelix_palette 工具调用"""
    try:
        # 解析函数路径: seaborn.widgets.choose_cubehelix_palette
        parts = "seaborn.widgets.choose_cubehelix_palette".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.widgets.choose_cubehelix_palette")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_widgets_choose_cubehelix_palette 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_axisgrid_FacetGrid_refline(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_axisgrid_FacetGrid_refline 工具调用"""
    try:
        # 解析函数路径: seaborn.axisgrid.FacetGrid.refline
        parts = "seaborn.axisgrid.FacetGrid.refline".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.axisgrid.FacetGrid.refline")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_axisgrid_FacetGrid_refline 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_distributions_ecdfplot(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_distributions_ecdfplot 工具调用"""
    try:
        # 解析函数路径: seaborn.distributions.ecdfplot
        parts = "seaborn.distributions.ecdfplot".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.distributions.ecdfplot")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_distributions_ecdfplot 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_external_docscrape_ClassDoc_get(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_external_docscrape_ClassDoc_get 工具调用"""
    try:
        # 解析函数路径: seaborn.external.docscrape.ClassDoc.get
        parts = "seaborn.external.docscrape.ClassDoc.get".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.external.docscrape.ClassDoc.get")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_external_docscrape_ClassDoc_get 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_axisgrid_PairGrid_apply(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_axisgrid_PairGrid_apply 工具调用"""
    try:
        # 解析函数路径: seaborn.axisgrid.PairGrid.apply
        parts = "seaborn.axisgrid.PairGrid.apply".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.axisgrid.PairGrid.apply")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_axisgrid_PairGrid_apply 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_axisgrid_PairGrid_pipe(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_axisgrid_PairGrid_pipe 工具调用"""
    try:
        # 解析函数路径: seaborn.axisgrid.PairGrid.pipe
        parts = "seaborn.axisgrid.PairGrid.pipe".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.axisgrid.PairGrid.pipe")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_axisgrid_PairGrid_pipe 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_categorical_Beeswarm_position_candidates(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_categorical_Beeswarm_position_candidates 工具调用"""
    try:
        # 解析函数路径: seaborn.categorical.Beeswarm.position_candidates
        parts = "seaborn.categorical.Beeswarm.position_candidates".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.categorical.Beeswarm.position_candidates")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_categorical_Beeswarm_position_candidates 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_external_docscrape_FunctionDoc_get_func(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_external_docscrape_FunctionDoc_get_func 工具调用"""
    try:
        # 解析函数路径: seaborn.external.docscrape.FunctionDoc.get_func
        parts = "seaborn.external.docscrape.FunctionDoc.get_func".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.external.docscrape.FunctionDoc.get_func")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_external_docscrape_FunctionDoc_get_func 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_axisgrid_Grid_add_legend(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_axisgrid_Grid_add_legend 工具调用"""
    try:
        # 解析函数路径: seaborn.axisgrid.Grid.add_legend
        parts = "seaborn.axisgrid.Grid.add_legend".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.axisgrid.Grid.add_legend")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_axisgrid_Grid_add_legend 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_axisgrid_PairGrid_map_diag(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_axisgrid_PairGrid_map_diag 工具调用"""
    try:
        # 解析函数路径: seaborn.axisgrid.PairGrid.map_diag
        parts = "seaborn.axisgrid.PairGrid.map_diag".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.axisgrid.PairGrid.map_diag")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_axisgrid_PairGrid_map_diag 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_utils_get_color_cycle(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_utils_get_color_cycle 工具调用"""
    try:
        # 解析函数路径: seaborn.utils.get_color_cycle
        parts = "seaborn.utils.get_color_cycle".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.utils.get_color_cycle")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_utils_get_color_cycle 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_axisgrid_FacetGrid_savefig(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_axisgrid_FacetGrid_savefig 工具调用"""
    try:
        # 解析函数路径: seaborn.axisgrid.FacetGrid.savefig
        parts = "seaborn.axisgrid.FacetGrid.savefig".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.axisgrid.FacetGrid.savefig")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_axisgrid_FacetGrid_savefig 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_utils_get_data_home(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_utils_get_data_home 工具调用"""
    try:
        # 解析函数路径: seaborn.utils.get_data_home
        parts = "seaborn.utils.get_data_home".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.utils.get_data_home")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_utils_get_data_home 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_axisgrid_PairGrid_map_lower(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_axisgrid_PairGrid_map_lower 工具调用"""
    try:
        # 解析函数路径: seaborn.axisgrid.PairGrid.map_lower
        parts = "seaborn.axisgrid.PairGrid.map_lower".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.axisgrid.PairGrid.map_lower")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_axisgrid_PairGrid_map_lower 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_axisgrid_FacetGrid_facet_data(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_axisgrid_FacetGrid_facet_data 工具调用"""
    try:
        # 解析函数路径: seaborn.axisgrid.FacetGrid.facet_data
        parts = "seaborn.axisgrid.FacetGrid.facet_data".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.axisgrid.FacetGrid.facet_data")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_axisgrid_FacetGrid_facet_data 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_axisgrid_JointGrid_set_axis_labels(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_axisgrid_JointGrid_set_axis_labels 工具调用"""
    try:
        # 解析函数路径: seaborn.axisgrid.JointGrid.set_axis_labels
        parts = "seaborn.axisgrid.JointGrid.set_axis_labels".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.axisgrid.JointGrid.set_axis_labels")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_axisgrid_JointGrid_set_axis_labels 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_axisgrid_PairGrid_map_upper(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_axisgrid_PairGrid_map_upper 工具调用"""
    try:
        # 解析函数路径: seaborn.axisgrid.PairGrid.map_upper
        parts = "seaborn.axisgrid.PairGrid.map_upper".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.axisgrid.PairGrid.map_upper")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_axisgrid_PairGrid_map_upper 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_categorical_Beeswarm_add_gutters(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_categorical_Beeswarm_add_gutters 工具调用"""
    try:
        # 解析函数路径: seaborn.categorical.Beeswarm.add_gutters
        parts = "seaborn.categorical.Beeswarm.add_gutters".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.categorical.Beeswarm.add_gutters")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_categorical_Beeswarm_add_gutters 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_axisgrid_JointGrid_refline(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_axisgrid_JointGrid_refline 工具调用"""
    try:
        # 解析函数路径: seaborn.axisgrid.JointGrid.refline
        parts = "seaborn.axisgrid.JointGrid.refline".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.axisgrid.JointGrid.refline")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_axisgrid_JointGrid_refline 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_categorical_stripplot(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_categorical_stripplot 工具调用"""
    try:
        # 解析函数路径: seaborn.categorical.stripplot
        parts = "seaborn.categorical.stripplot".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.categorical.stripplot")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_categorical_stripplot 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_axisgrid_Grid_tick_params(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_axisgrid_Grid_tick_params 工具调用"""
    try:
        # 解析函数路径: seaborn.axisgrid.Grid.tick_params
        parts = "seaborn.axisgrid.Grid.tick_params".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.axisgrid.Grid.tick_params")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_axisgrid_Grid_tick_params 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_axisgrid_PairGrid_savefig(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_axisgrid_PairGrid_savefig 工具调用"""
    try:
        # 解析函数路径: seaborn.axisgrid.PairGrid.savefig
        parts = "seaborn.axisgrid.PairGrid.savefig".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.axisgrid.PairGrid.savefig")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_axisgrid_PairGrid_savefig 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_external_docscrape_NumpyDocString_get(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_external_docscrape_NumpyDocString_get 工具调用"""
    try:
        # 解析函数路径: seaborn.external.docscrape.NumpyDocString.get
        parts = "seaborn.external.docscrape.NumpyDocString.get".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.external.docscrape.NumpyDocString.get")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_external_docscrape_NumpyDocString_get 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_categorical_boxplot(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_categorical_boxplot 工具调用"""
    try:
        # 解析函数路径: seaborn.categorical.boxplot
        parts = "seaborn.categorical.boxplot".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.categorical.boxplot")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_categorical_boxplot 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_distributions_rugplot(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_distributions_rugplot 工具调用"""
    try:
        # 解析函数路径: seaborn.distributions.rugplot
        parts = "seaborn.distributions.rugplot".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.distributions.rugplot")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_distributions_rugplot 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_axisgrid_Grid_savefig(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_axisgrid_Grid_savefig 工具调用"""
    try:
        # 解析函数路径: seaborn.axisgrid.Grid.savefig
        parts = "seaborn.axisgrid.Grid.savefig".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.axisgrid.Grid.savefig")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_axisgrid_Grid_savefig 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_matrix_ClusterGrid_format_data(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_matrix_ClusterGrid_format_data 工具调用"""
    try:
        # 解析函数路径: seaborn.matrix.ClusterGrid.format_data
        parts = "seaborn.matrix.ClusterGrid.format_data".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.matrix.ClusterGrid.format_data")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_matrix_ClusterGrid_format_data 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_categorical_Beeswarm_could_overlap(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_categorical_Beeswarm_could_overlap 工具调用"""
    try:
        # 解析函数路径: seaborn.categorical.Beeswarm.could_overlap
        parts = "seaborn.categorical.Beeswarm.could_overlap".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.categorical.Beeswarm.could_overlap")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_categorical_Beeswarm_could_overlap 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_axisgrid_FacetGrid_apply(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_axisgrid_FacetGrid_apply 工具调用"""
    try:
        # 解析函数路径: seaborn.axisgrid.FacetGrid.apply
        parts = "seaborn.axisgrid.FacetGrid.apply".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.axisgrid.FacetGrid.apply")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_axisgrid_FacetGrid_apply 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_axisgrid_JointGrid_savefig(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_axisgrid_JointGrid_savefig 工具调用"""
    try:
        # 解析函数路径: seaborn.axisgrid.JointGrid.savefig
        parts = "seaborn.axisgrid.JointGrid.savefig".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.axisgrid.JointGrid.savefig")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_axisgrid_JointGrid_savefig 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_axisgrid_FacetGrid_map(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_axisgrid_FacetGrid_map 工具调用"""
    try:
        # 解析函数路径: seaborn.axisgrid.FacetGrid.map
        parts = "seaborn.axisgrid.FacetGrid.map".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.axisgrid.FacetGrid.map")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_axisgrid_FacetGrid_map 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_external_docscrape_NumpyDocString_keys(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_external_docscrape_NumpyDocString_keys 工具调用"""
    try:
        # 解析函数路径: seaborn.external.docscrape.NumpyDocString.keys
        parts = "seaborn.external.docscrape.NumpyDocString.keys".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.external.docscrape.NumpyDocString.keys")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_external_docscrape_NumpyDocString_keys 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_axisgrid_PairGrid_map_offdiag(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_axisgrid_PairGrid_map_offdiag 工具调用"""
    try:
        # 解析函数路径: seaborn.axisgrid.PairGrid.map_offdiag
        parts = "seaborn.axisgrid.PairGrid.map_offdiag".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.axisgrid.PairGrid.map_offdiag")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_axisgrid_PairGrid_map_offdiag 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_axisgrid_FacetGrid_set_titles(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_axisgrid_FacetGrid_set_titles 工具调用"""
    try:
        # 解析函数路径: seaborn.axisgrid.FacetGrid.set_titles
        parts = "seaborn.axisgrid.FacetGrid.set_titles".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.axisgrid.FacetGrid.set_titles")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_axisgrid_FacetGrid_set_titles 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_axisgrid_FacetGrid_set_yticklabels(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_axisgrid_FacetGrid_set_yticklabels 工具调用"""
    try:
        # 解析函数路径: seaborn.axisgrid.FacetGrid.set_yticklabels
        parts = "seaborn.axisgrid.FacetGrid.set_yticklabels".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.axisgrid.FacetGrid.set_yticklabels")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_axisgrid_FacetGrid_set_yticklabels 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_axisgrid_FacetGrid_map_dataframe(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_axisgrid_FacetGrid_map_dataframe 工具调用"""
    try:
        # 解析函数路径: seaborn.axisgrid.FacetGrid.map_dataframe
        parts = "seaborn.axisgrid.FacetGrid.map_dataframe".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.axisgrid.FacetGrid.map_dataframe")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_axisgrid_FacetGrid_map_dataframe 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_external_docscrape_NumpyDocString_items(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_external_docscrape_NumpyDocString_items 工具调用"""
    try:
        # 解析函数路径: seaborn.external.docscrape.NumpyDocString.items
        parts = "seaborn.external.docscrape.NumpyDocString.items".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.external.docscrape.NumpyDocString.items")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_external_docscrape_NumpyDocString_items 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_axisgrid_JointGrid_pipe(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_axisgrid_JointGrid_pipe 工具调用"""
    try:
        # 解析函数路径: seaborn.axisgrid.JointGrid.pipe
        parts = "seaborn.axisgrid.JointGrid.pipe".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.axisgrid.JointGrid.pipe")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_axisgrid_JointGrid_pipe 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_categorical_Beeswarm_first_non_overlapping_candidate(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_categorical_Beeswarm_first_non_overlapping_candidate 工具调用"""
    try:
        # 解析函数路径: seaborn.categorical.Beeswarm.first_non_overlapping_candidate
        parts = "seaborn.categorical.Beeswarm.first_non_overlapping_candidate".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.categorical.Beeswarm.first_non_overlapping_candidate")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_categorical_Beeswarm_first_non_overlapping_candidate 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_axisgrid_FacetGrid_facet_axis(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_axisgrid_FacetGrid_facet_axis 工具调用"""
    try:
        # 解析函数路径: seaborn.axisgrid.FacetGrid.facet_axis
        parts = "seaborn.axisgrid.FacetGrid.facet_axis".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.axisgrid.FacetGrid.facet_axis")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_axisgrid_FacetGrid_facet_axis 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_algorithms_bootstrap(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_algorithms_bootstrap 工具调用"""
    try:
        # 解析函数路径: seaborn.algorithms.bootstrap
        parts = "seaborn.algorithms.bootstrap".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.algorithms.bootstrap")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_algorithms_bootstrap 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_utils_get_dataset_names(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_utils_get_dataset_names 工具调用"""
    try:
        # 解析函数路径: seaborn.utils.get_dataset_names
        parts = "seaborn.utils.get_dataset_names".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.utils.get_dataset_names")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_utils_get_dataset_names 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_external_docscrape_FunctionDoc_get(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_external_docscrape_FunctionDoc_get 工具调用"""
    try:
        # 解析函数路径: seaborn.external.docscrape.FunctionDoc.get
        parts = "seaborn.external.docscrape.FunctionDoc.get".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.external.docscrape.FunctionDoc.get")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_external_docscrape_FunctionDoc_get 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_axisgrid_PairGrid_add_legend(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_axisgrid_PairGrid_add_legend 工具调用"""
    try:
        # 解析函数路径: seaborn.axisgrid.PairGrid.add_legend
        parts = "seaborn.axisgrid.PairGrid.add_legend".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.axisgrid.PairGrid.add_legend")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_axisgrid_PairGrid_add_legend 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_axisgrid_FacetGrid_add_legend(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_axisgrid_FacetGrid_add_legend 工具调用"""
    try:
        # 解析函数路径: seaborn.axisgrid.FacetGrid.add_legend
        parts = "seaborn.axisgrid.FacetGrid.add_legend".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.axisgrid.FacetGrid.add_legend")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_axisgrid_FacetGrid_add_legend 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_axisgrid_PairGrid_tick_params(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_axisgrid_PairGrid_tick_params 工具调用"""
    try:
        # 解析函数路径: seaborn.axisgrid.PairGrid.tick_params
        parts = "seaborn.axisgrid.PairGrid.tick_params".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.axisgrid.PairGrid.tick_params")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_axisgrid_PairGrid_tick_params 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_external_docscrape_strip_blank_lines(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_external_docscrape_strip_blank_lines 工具调用"""
    try:
        # 解析函数路径: seaborn.external.docscrape.strip_blank_lines
        parts = "seaborn.external.docscrape.strip_blank_lines".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.external.docscrape.strip_blank_lines")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_external_docscrape_strip_blank_lines 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_axisgrid_jointplot(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_axisgrid_jointplot 工具调用"""
    try:
        # 解析函数路径: seaborn.axisgrid.jointplot
        parts = "seaborn.axisgrid.jointplot".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.axisgrid.jointplot")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_axisgrid_jointplot 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_axisgrid_FacetGrid_set_axis_labels(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_axisgrid_FacetGrid_set_axis_labels 工具调用"""
    try:
        # 解析函数路径: seaborn.axisgrid.FacetGrid.set_axis_labels
        parts = "seaborn.axisgrid.FacetGrid.set_axis_labels".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.axisgrid.FacetGrid.set_axis_labels")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_axisgrid_FacetGrid_set_axis_labels 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_axisgrid_JointGrid_plot_joint(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_axisgrid_JointGrid_plot_joint 工具调用"""
    try:
        # 解析函数路径: seaborn.axisgrid.JointGrid.plot_joint
        parts = "seaborn.axisgrid.JointGrid.plot_joint".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.axisgrid.JointGrid.plot_joint")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_axisgrid_JointGrid_plot_joint 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_external_appdirs_user_cache_dir(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_external_appdirs_user_cache_dir 工具调用"""
    try:
        # 解析函数路径: seaborn.external.appdirs.user_cache_dir
        parts = "seaborn.external.appdirs.user_cache_dir".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.external.appdirs.user_cache_dir")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_external_appdirs_user_cache_dir 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_widgets_choose_light_palette(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_widgets_choose_light_palette 工具调用"""
    try:
        # 解析函数路径: seaborn.widgets.choose_light_palette
        parts = "seaborn.widgets.choose_light_palette".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.widgets.choose_light_palette")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_widgets_choose_light_palette 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_external_docscrape_ClassDoc_values(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_external_docscrape_ClassDoc_values 工具调用"""
    try:
        # 解析函数路径: seaborn.external.docscrape.ClassDoc.values
        parts = "seaborn.external.docscrape.ClassDoc.values".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.external.docscrape.ClassDoc.values")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_external_docscrape_ClassDoc_values 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_axisgrid_JointGrid_plot(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_axisgrid_JointGrid_plot 工具调用"""
    try:
        # 解析函数路径: seaborn.axisgrid.JointGrid.plot
        parts = "seaborn.axisgrid.JointGrid.plot".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.axisgrid.JointGrid.plot")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_axisgrid_JointGrid_plot 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_axisgrid_Grid_apply(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_axisgrid_Grid_apply 工具调用"""
    try:
        # 解析函数路径: seaborn.axisgrid.Grid.apply
        parts = "seaborn.axisgrid.Grid.apply".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.axisgrid.Grid.apply")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_axisgrid_Grid_apply 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_axisgrid_JointGrid_apply(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_axisgrid_JointGrid_apply 工具调用"""
    try:
        # 解析函数路径: seaborn.axisgrid.JointGrid.apply
        parts = "seaborn.axisgrid.JointGrid.apply".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.axisgrid.JointGrid.apply")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_axisgrid_JointGrid_apply 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_axisgrid_FacetGrid_tick_params(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_axisgrid_FacetGrid_tick_params 工具调用"""
    try:
        # 解析函数路径: seaborn.axisgrid.FacetGrid.tick_params
        parts = "seaborn.axisgrid.FacetGrid.tick_params".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.axisgrid.FacetGrid.tick_params")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_axisgrid_FacetGrid_tick_params 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_axisgrid_PairGrid_map(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_axisgrid_PairGrid_map 工具调用"""
    try:
        # 解析函数路径: seaborn.axisgrid.PairGrid.map
        parts = "seaborn.axisgrid.PairGrid.map".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.axisgrid.PairGrid.map")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_axisgrid_PairGrid_map 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_external_docscrape_ClassDoc_items(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_external_docscrape_ClassDoc_items 工具调用"""
    try:
        # 解析函数路径: seaborn.external.docscrape.ClassDoc.items
        parts = "seaborn.external.docscrape.ClassDoc.items".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.external.docscrape.ClassDoc.items")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_external_docscrape_ClassDoc_items 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_axisgrid_FacetGrid_tight_layout(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_axisgrid_FacetGrid_tight_layout 工具调用"""
    try:
        # 解析函数路径: seaborn.axisgrid.FacetGrid.tight_layout
        parts = "seaborn.axisgrid.FacetGrid.tight_layout".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.axisgrid.FacetGrid.tight_layout")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_axisgrid_FacetGrid_tight_layout 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_axisgrid_JointGrid_plot_marginals(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_axisgrid_JointGrid_plot_marginals 工具调用"""
    try:
        # 解析函数路径: seaborn.axisgrid.JointGrid.plot_marginals
        parts = "seaborn.axisgrid.JointGrid.plot_marginals".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.axisgrid.JointGrid.plot_marginals")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_axisgrid_JointGrid_plot_marginals 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_axisgrid_PairGrid_tight_layout(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_axisgrid_PairGrid_tight_layout 工具调用"""
    try:
        # 解析函数路径: seaborn.axisgrid.PairGrid.tight_layout
        parts = "seaborn.axisgrid.PairGrid.tight_layout".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.axisgrid.PairGrid.tight_layout")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_axisgrid_PairGrid_tight_layout 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_widgets_choose_dark_palette(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_widgets_choose_dark_palette 工具调用"""
    try:
        # 解析函数路径: seaborn.widgets.choose_dark_palette
        parts = "seaborn.widgets.choose_dark_palette".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.widgets.choose_dark_palette")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_widgets_choose_dark_palette 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_categorical_swarmplot(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_categorical_swarmplot 工具调用"""
    try:
        # 解析函数路径: seaborn.categorical.swarmplot
        parts = "seaborn.categorical.swarmplot".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.categorical.swarmplot")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_categorical_swarmplot 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_categorical_countplot(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_categorical_countplot 工具调用"""
    try:
        # 解析函数路径: seaborn.categorical.countplot
        parts = "seaborn.categorical.countplot".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.categorical.countplot")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_categorical_countplot 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_axisgrid_pairplot(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_axisgrid_pairplot 工具调用"""
    try:
        # 解析函数路径: seaborn.axisgrid.pairplot
        parts = "seaborn.axisgrid.pairplot".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.axisgrid.pairplot")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_axisgrid_pairplot 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_axisgrid_FacetGrid_pipe(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_axisgrid_FacetGrid_pipe 工具调用"""
    try:
        # 解析函数路径: seaborn.axisgrid.FacetGrid.pipe
        parts = "seaborn.axisgrid.FacetGrid.pipe".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.axisgrid.FacetGrid.pipe")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_axisgrid_FacetGrid_pipe 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_widgets_choose_colorbrewer_palette(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_widgets_choose_colorbrewer_palette 工具调用"""
    try:
        # 解析函数路径: seaborn.widgets.choose_colorbrewer_palette
        parts = "seaborn.widgets.choose_colorbrewer_palette".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.widgets.choose_colorbrewer_palette")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_widgets_choose_colorbrewer_palette 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_axisgrid_Grid_pipe(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_axisgrid_Grid_pipe 工具调用"""
    try:
        # 解析函数路径: seaborn.axisgrid.Grid.pipe
        parts = "seaborn.axisgrid.Grid.pipe".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.axisgrid.Grid.pipe")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_axisgrid_Grid_pipe 失败: {e}")
        return {"error": str(e)}


def handle_seaborn_axisgrid_Grid_tight_layout(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 seaborn_axisgrid_Grid_tight_layout 工具调用"""
    try:
        # 解析函数路径: seaborn.axisgrid.Grid.tight_layout
        parts = "seaborn.axisgrid.Grid.tight_layout".split('.')
        
        if parts[0] != "seaborn":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # seaborn.function_name
            func_name = parts[1]
            func = getattr(seaborn, func_name)
        elif len(parts) >= 3:
            # seaborn.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: seaborn.axisgrid.Grid.tight_layout")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 seaborn_axisgrid_Grid_tight_layout 失败: {e}")
        return {"error": str(e)}


def process_mcp_request(request_line: str) -> str:
    """处理 MCP 请求"""
    try:
        request = json.loads(request_line.strip())
        method = request.get("method", "")
        params = request.get("params", {})
        request_id = request.get("id")
        
        if method == "initialize":
            # MCP 初始化请求
            response = {
                "jsonrpc": "2.0",
                "id": request_id,
                "result": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {
                        "tools": {},
                        "logging": {},
                        "prompts": {},
                        "resources": {}
                    },
                    "serverInfo": {
                        "name": "seaborn-mcp-server",
                        "version": "1.0.0"
                    }
                }
            }
        elif method == "notifications/initialized":
            # 初始化完成通知，不需要响应
            return ""
        elif method == "tools/list":
            response = {
                "jsonrpc": "2.0",
                "id": request_id,
                "result": {"tools": TOOLS}
            }
        elif method == "tools/call":
            tool_name = params.get("name", "")
            arguments = params.get("arguments", {})
            
            # 调用对应的处理函数
            handler_name = f"handle_{tool_name}"
            if handler_name in globals():
                result = globals()[handler_name](arguments)
            else:
                result = {"error": f"未找到工具处理器: {tool_name}"}
            
            response = {
                "jsonrpc": "2.0",
                "id": request_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(result, ensure_ascii=False, indent=2)
                        }
                    ]
                }
            }
        else:
            response = {
                "jsonrpc": "2.0",
                "id": request_id,
                "error": {
                    "code": -32601,
                    "message": f"未知方法: {method}"
                }
            }
        
        return json.dumps(response)
    
    except Exception as e:
        logger.error(f"处理请求失败: {e}")
        return json.dumps({
            "jsonrpc": "2.0",
            "id": None,
            "error": {
                "code": -32603,
                "message": f"内部错误: {str(e)}"
            }
        })

async def main():
    """主函数 - MCP 服务器模式"""
    logger.info("启动 seaborn MCP 服务器...")
    
    try:
        # 读取 stdin 并处理请求
        while True:
            try:
                line = sys.stdin.readline()
                if not line:
                    break
                
                line = line.strip()
                if line:
                    logger.debug(f"收到请求: {line}")
                    response = process_mcp_request(line)
                    if response:  # 只有当有响应时才输出
                        print(response, flush=True)
                        logger.debug(f"发送响应: {response}")
                        
            except EOFError:
                # 正常的输入结束
                break
            except Exception as e:
                logger.error(f"处理请求时出错: {e}")
                error_response = json.dumps({
                    "jsonrpc": "2.0",
                    "id": None,
                    "error": {
                        "code": -32603,
                        "message": f"内部错误: {str(e)}"
                    }
                })
                print(error_response, flush=True)
                
    except KeyboardInterrupt:
        logger.info("服务器停止")
    except Exception as e:
        logger.error(f"服务器错误: {e}")
    finally:
        logger.info("服务器关闭")

def cli_mode():
    """命令行模式 - 用于测试"""
    if len(sys.argv) < 3:
        print(json.dumps({"error": "参数不足，需要: 工具名 参数JSON"}))
        return
    
    tool_name = sys.argv[1]
    try:
        arguments = json.loads(sys.argv[2])
    except json.JSONDecodeError:
        print(json.dumps({"error": "参数格式错误"}))
        return
    
    # 调用对应的处理函数
    handler_name = f"handle_{tool_name}"
    if handler_name in globals():
        result = globals()[handler_name](arguments)
    else:
        result = {"error": f"未找到工具: {tool_name}"}
    
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # 命令行模式
        cli_mode()
    else:
        # MCP 服务器模式
        asyncio.run(main())
