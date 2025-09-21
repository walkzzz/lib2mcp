#!/usr/bin/env python3
"""
自动生成的 MCP 服务器
库: zipfile
工具数量: 83
"""

import asyncio
import json
import logging
import sys
from typing import Dict, Any

try:
    import zipfile  # type: ignore
except ImportError:
    print("错误: 未安装 zipfile 库，请运行: pip install zipfile")
    sys.exit(1)

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("zipfile_mcp_server")

# 工具定义
TOOLS = [
    {
        "name": "zipfile_is_zipfile",
        "description": "Quickly see if a file is a ZIP file by checking the magic number.\nThe filename argument may be a file or file-like object too.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "filename": {
                    "type": "string",
                    "description": "类型从参数名推断: filename"
                }
            },
            "required": [
                "filename"
            ]
        }
    },
    {
        "name": "zipfile_main",
        "description": "执行main操作（zipfile模块的函数）",
        "inputSchema": {
            "type": "object",
            "properties": {
                "args": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": []
        }
    },
    {
        "name": "zipfile_CompleteDirs_close",
        "description": "Close the file, and for mode 'w', 'x' and 'a' write the ending\nrecords.",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "zipfile_CompleteDirs_extract",
        "description": "Extract a member from the archive to the current working directory,\nusing its full name. Its file information is extracted as accurately\nas possible. `member' may be a filename or a ZipInfo object. You can\nspecify a different directory using `path'.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "member": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "path": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "pwd": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "member"
            ]
        }
    },
    {
        "name": "zipfile_CompleteDirs_extractall",
        "description": "Extract all members from the archive to the current working\ndirectory. `path' specifies a different directory to extract to.\n`members' is optional and must be a subset of the list returned\nby namelist().",
        "inputSchema": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "members": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "pwd": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": []
        }
    },
    {
        "name": "zipfile_CompleteDirs_getinfo",
        "description": "Supplement getinfo for implied dirs.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "类型从参数名推断: name"
                }
            },
            "required": [
                "name"
            ]
        }
    },
    {
        "name": "zipfile_CompleteDirs_infolist",
        "description": "Return a list of class ZipInfo instances for files in the\narchive.",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "zipfile_CompleteDirs_mkdir",
        "description": "Creates a directory inside the zip archive.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "zinfo_or_directory_name": {
                    "type": "string",
                    "description": "类型从参数名推断: zinfo_or_directory_name"
                },
                "mode": {
                    "type": "integer",
                    "default": 511,
                    "description": "类型从默认值推断: int"
                }
            },
            "required": [
                "zinfo_or_directory_name"
            ]
        }
    },
    {
        "name": "zipfile_CompleteDirs_namelist",
        "description": "执行namelist操作（CompleteDirs类的方法）",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "zipfile_CompleteDirs_open",
        "description": "Return file-like object for 'name'.\nname is a string for the file name within the ZIP file, or a ZipInfo\nobject.\nmode should be 'r' to read a file already in the ZIP file, or 'w' to\nwrite to a file newly added to the archive.\npwd is the password to decrypt files (only used for reading).\nWhen writing, if the file size is not known in advance but may exceed\n2 GiB, pass force_zip64 to use the ZIP64 format, which can handle large\nfiles.  If the size is known in advance, it is best to pass a ZipInfo\ninstance for name, with zinfo.file_size set.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "类型从参数名推断: name"
                },
                "mode": {
                    "type": "string",
                    "default": "r",
                    "description": "类型从默认值推断: str"
                },
                "pwd": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "force_zip64": {
                    "type": "integer",
                    "default": False,
                    "description": "类型从默认值推断: bool"
                }
            },
            "required": [
                "name"
            ]
        }
    },
    {
        "name": "zipfile_CompleteDirs_printdir",
        "description": "Print a table of contents for the zip file.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "file": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": []
        }
    },
    {
        "name": "zipfile_CompleteDirs_read",
        "description": "Return file bytes for name.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "类型从参数名推断: name"
                },
                "pwd": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "name"
            ]
        }
    },
    {
        "name": "zipfile_CompleteDirs_resolve_dir",
        "description": "If the name represents a directory, return that name\nas a directory (with the trailing slash).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "类型从参数名推断: name"
                }
            },
            "required": [
                "name"
            ]
        }
    },
    {
        "name": "zipfile_CompleteDirs_setpassword",
        "description": "Set default password for encrypted files.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "pwd": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "pwd"
            ]
        }
    },
    {
        "name": "zipfile_CompleteDirs_testzip",
        "description": "Read all the files and check the CRC.",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "zipfile_CompleteDirs_write",
        "description": "Put the bytes from filename into the archive under the name\narcname.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "filename": {
                    "type": "string",
                    "description": "类型从参数名推断: filename"
                },
                "arcname": {
                    "type": "string",
                    "description": "类型从参数名推断: arcname"
                },
                "compress_type": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "compresslevel": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "filename"
            ]
        }
    },
    {
        "name": "zipfile_CompleteDirs_writestr",
        "description": "Write a file into the archive.  The contents is 'data', which\nmay be either a 'str' or a 'bytes' instance; if it is a 'str',\nit is encoded as UTF-8 first.\n'zinfo_or_arcname' is either a ZipInfo instance or\nthe name of the file in the archive.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "zinfo_or_arcname": {
                    "type": "string",
                    "description": "类型从参数名推断: zinfo_or_arcname"
                },
                "data": {
                    "type": "object",
                    "description": "类型从参数名推断: data"
                },
                "compress_type": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "compresslevel": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "zinfo_or_arcname",
                "data"
            ]
        }
    },
    {
        "name": "zipfile_FastLookup_close",
        "description": "Close the file, and for mode 'w', 'x' and 'a' write the ending\nrecords.",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "zipfile_FastLookup_extract",
        "description": "Extract a member from the archive to the current working directory,\nusing its full name. Its file information is extracted as accurately\nas possible. `member' may be a filename or a ZipInfo object. You can\nspecify a different directory using `path'.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "member": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "path": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "pwd": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "member"
            ]
        }
    },
    {
        "name": "zipfile_FastLookup_extractall",
        "description": "Extract all members from the archive to the current working\ndirectory. `path' specifies a different directory to extract to.\n`members' is optional and must be a subset of the list returned\nby namelist().",
        "inputSchema": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "members": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "pwd": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": []
        }
    },
    {
        "name": "zipfile_FastLookup_getinfo",
        "description": "Supplement getinfo for implied dirs.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "类型从参数名推断: name"
                }
            },
            "required": [
                "name"
            ]
        }
    },
    {
        "name": "zipfile_FastLookup_infolist",
        "description": "Return a list of class ZipInfo instances for files in the\narchive.",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "zipfile_FastLookup_mkdir",
        "description": "Creates a directory inside the zip archive.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "zinfo_or_directory_name": {
                    "type": "string",
                    "description": "类型从参数名推断: zinfo_or_directory_name"
                },
                "mode": {
                    "type": "integer",
                    "default": 511,
                    "description": "类型从默认值推断: int"
                }
            },
            "required": [
                "zinfo_or_directory_name"
            ]
        }
    },
    {
        "name": "zipfile_FastLookup_namelist",
        "description": "执行namelist操作（FastLookup类的方法）",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "zipfile_FastLookup_open",
        "description": "Return file-like object for 'name'.\nname is a string for the file name within the ZIP file, or a ZipInfo\nobject.\nmode should be 'r' to read a file already in the ZIP file, or 'w' to\nwrite to a file newly added to the archive.\npwd is the password to decrypt files (only used for reading).\nWhen writing, if the file size is not known in advance but may exceed\n2 GiB, pass force_zip64 to use the ZIP64 format, which can handle large\nfiles.  If the size is known in advance, it is best to pass a ZipInfo\ninstance for name, with zinfo.file_size set.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "类型从参数名推断: name"
                },
                "mode": {
                    "type": "string",
                    "default": "r",
                    "description": "类型从默认值推断: str"
                },
                "pwd": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "force_zip64": {
                    "type": "integer",
                    "default": False,
                    "description": "类型从默认值推断: bool"
                }
            },
            "required": [
                "name"
            ]
        }
    },
    {
        "name": "zipfile_FastLookup_printdir",
        "description": "Print a table of contents for the zip file.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "file": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": []
        }
    },
    {
        "name": "zipfile_FastLookup_read",
        "description": "Return file bytes for name.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "类型从参数名推断: name"
                },
                "pwd": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "name"
            ]
        }
    },
    {
        "name": "zipfile_FastLookup_resolve_dir",
        "description": "If the name represents a directory, return that name\nas a directory (with the trailing slash).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "类型从参数名推断: name"
                }
            },
            "required": [
                "name"
            ]
        }
    },
    {
        "name": "zipfile_FastLookup_setpassword",
        "description": "Set default password for encrypted files.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "pwd": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "pwd"
            ]
        }
    },
    {
        "name": "zipfile_FastLookup_testzip",
        "description": "Read all the files and check the CRC.",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "zipfile_FastLookup_write",
        "description": "Put the bytes from filename into the archive under the name\narcname.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "filename": {
                    "type": "string",
                    "description": "类型从参数名推断: filename"
                },
                "arcname": {
                    "type": "string",
                    "description": "类型从参数名推断: arcname"
                },
                "compress_type": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "compresslevel": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "filename"
            ]
        }
    },
    {
        "name": "zipfile_FastLookup_writestr",
        "description": "Write a file into the archive.  The contents is 'data', which\nmay be either a 'str' or a 'bytes' instance; if it is a 'str',\nit is encoded as UTF-8 first.\n'zinfo_or_arcname' is either a ZipInfo instance or\nthe name of the file in the archive.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "zinfo_or_arcname": {
                    "type": "string",
                    "description": "类型从参数名推断: zinfo_or_arcname"
                },
                "data": {
                    "type": "object",
                    "description": "类型从参数名推断: data"
                },
                "compress_type": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "compresslevel": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "zinfo_or_arcname",
                "data"
            ]
        }
    },
    {
        "name": "zipfile_LZMACompressor_compress",
        "description": "执行compress操作（LZMACompressor类的方法）",
        "inputSchema": {
            "type": "object",
            "properties": {
                "data": {
                    "type": "object",
                    "description": "类型从参数名推断: data"
                }
            },
            "required": [
                "data"
            ]
        }
    },
    {
        "name": "zipfile_LZMACompressor_flush",
        "description": "执行flush操作（LZMACompressor类的方法）",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "zipfile_LZMADecompressor_decompress",
        "description": "执行decompress操作（LZMADecompressor类的方法）",
        "inputSchema": {
            "type": "object",
            "properties": {
                "data": {
                    "type": "object",
                    "description": "类型从参数名推断: data"
                }
            },
            "required": [
                "data"
            ]
        }
    },
    {
        "name": "zipfile_Path_exists",
        "description": "执行exists操作（Path类的方法）",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "zipfile_Path_is_dir",
        "description": "执行is_dir操作（Path类的方法）",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "zipfile_Path_is_file",
        "description": "执行is_file操作（Path类的方法）",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "zipfile_Path_iterdir",
        "description": "执行iterdir操作（Path类的方法）",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "zipfile_Path_joinpath",
        "description": "执行joinpath操作（Path类的方法）",
        "inputSchema": {
            "type": "object",
            "properties": {
                "other": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "other"
            ]
        }
    },
    {
        "name": "zipfile_Path_open",
        "description": "Open this entry as text or binary following the semantics\nof ``pathlib.Path.open()`` by passing arguments through\nto io.TextIOWrapper().",
        "inputSchema": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "类型从参数名推断: name"
                },
                "mode": {
                    "type": "string",
                    "default": "r",
                    "description": "类型从默认值推断: str"
                },
                "pwd": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "force_zip64": {
                    "type": "integer",
                    "default": False,
                    "description": "类型从默认值推断: bool"
                }
            },
            "required": [
                "name"
            ]
        }
    },
    {
        "name": "zipfile_Path_read_bytes",
        "description": "读取数据（Path类的方法）",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "zipfile_Path_read_text",
        "description": "读取数据（Path类的方法）",
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
        "name": "zipfile_PyZipFile_close",
        "description": "Close the file, and for mode 'w', 'x' and 'a' write the ending\nrecords.",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "zipfile_PyZipFile_extract",
        "description": "Extract a member from the archive to the current working directory,\nusing its full name. Its file information is extracted as accurately\nas possible. `member' may be a filename or a ZipInfo object. You can\nspecify a different directory using `path'.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "member": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "path": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "pwd": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "member"
            ]
        }
    },
    {
        "name": "zipfile_PyZipFile_extractall",
        "description": "Extract all members from the archive to the current working\ndirectory. `path' specifies a different directory to extract to.\n`members' is optional and must be a subset of the list returned\nby namelist().",
        "inputSchema": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "members": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "pwd": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": []
        }
    },
    {
        "name": "zipfile_PyZipFile_getinfo",
        "description": "Return the instance of ZipInfo given 'name'.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "类型从参数名推断: name"
                }
            },
            "required": [
                "name"
            ]
        }
    },
    {
        "name": "zipfile_PyZipFile_infolist",
        "description": "Return a list of class ZipInfo instances for files in the\narchive.",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "zipfile_PyZipFile_mkdir",
        "description": "Creates a directory inside the zip archive.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "zinfo_or_directory_name": {
                    "type": "string",
                    "description": "类型从参数名推断: zinfo_or_directory_name"
                },
                "mode": {
                    "type": "integer",
                    "default": 511,
                    "description": "类型从默认值推断: int"
                }
            },
            "required": [
                "zinfo_or_directory_name"
            ]
        }
    },
    {
        "name": "zipfile_PyZipFile_namelist",
        "description": "Return a list of file names in the archive.",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "zipfile_PyZipFile_open",
        "description": "Return file-like object for 'name'.\nname is a string for the file name within the ZIP file, or a ZipInfo\nobject.\nmode should be 'r' to read a file already in the ZIP file, or 'w' to\nwrite to a file newly added to the archive.\npwd is the password to decrypt files (only used for reading).\nWhen writing, if the file size is not known in advance but may exceed\n2 GiB, pass force_zip64 to use the ZIP64 format, which can handle large\nfiles.  If the size is known in advance, it is best to pass a ZipInfo\ninstance for name, with zinfo.file_size set.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "类型从参数名推断: name"
                },
                "mode": {
                    "type": "string",
                    "default": "r",
                    "description": "类型从默认值推断: str"
                },
                "pwd": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "force_zip64": {
                    "type": "integer",
                    "default": False,
                    "description": "类型从默认值推断: bool"
                }
            },
            "required": [
                "name"
            ]
        }
    },
    {
        "name": "zipfile_PyZipFile_printdir",
        "description": "Print a table of contents for the zip file.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "file": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": []
        }
    },
    {
        "name": "zipfile_PyZipFile_read",
        "description": "Return file bytes for name.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "类型从参数名推断: name"
                },
                "pwd": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "name"
            ]
        }
    },
    {
        "name": "zipfile_PyZipFile_setpassword",
        "description": "Set default password for encrypted files.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "pwd": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "pwd"
            ]
        }
    },
    {
        "name": "zipfile_PyZipFile_testzip",
        "description": "Read all the files and check the CRC.",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "zipfile_PyZipFile_write",
        "description": "Put the bytes from filename into the archive under the name\narcname.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "filename": {
                    "type": "string",
                    "description": "类型从参数名推断: filename"
                },
                "arcname": {
                    "type": "string",
                    "description": "类型从参数名推断: arcname"
                },
                "compress_type": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "compresslevel": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "filename"
            ]
        }
    },
    {
        "name": "zipfile_PyZipFile_writepy",
        "description": "Add all files from \"pathname\" to the ZIP archive.\nIf pathname is a package directory, search the directory and\nall package subdirectories recursively for all *.py and enter\nthe modules into the archive.  If pathname is a plain\ndirectory, listdir *.py and enter all modules.  Else, pathname\nmust be a Python *.py file and the module will be put into the\narchive.  Added modules are always module.pyc.\nThis method will compile the module.py into module.pyc if\nnecessary.\nIf filterfunc(pathname) is given, it is called with every argument.\nWhen it is False, the file or directory is skipped.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "pathname": {
                    "type": "string",
                    "description": "类型从参数名推断: pathname"
                },
                "basename": {
                    "type": "string",
                    "default": "",
                    "description": "类型从默认值推断: str"
                },
                "filterfunc": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "pathname"
            ]
        }
    },
    {
        "name": "zipfile_PyZipFile_writestr",
        "description": "Write a file into the archive.  The contents is 'data', which\nmay be either a 'str' or a 'bytes' instance; if it is a 'str',\nit is encoded as UTF-8 first.\n'zinfo_or_arcname' is either a ZipInfo instance or\nthe name of the file in the archive.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "zinfo_or_arcname": {
                    "type": "string",
                    "description": "类型从参数名推断: zinfo_or_arcname"
                },
                "data": {
                    "type": "object",
                    "description": "类型从参数名推断: data"
                },
                "compress_type": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "compresslevel": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "zinfo_or_arcname",
                "data"
            ]
        }
    },
    {
        "name": "zipfile_ZipExtFile_close",
        "description": "关闭数据（ZipExtFile类的方法）",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "zipfile_ZipExtFile_peek",
        "description": "Returns buffered bytes without advancing the position.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "n": {
                    "type": "integer",
                    "default": 1,
                    "description": "类型从默认值推断: int"
                }
            },
            "required": []
        }
    },
    {
        "name": "zipfile_ZipExtFile_read",
        "description": "Read and return up to n bytes.\nIf the argument is omitted, None, or negative, data is read and returned until EOF is reached.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "类型从参数名推断: name"
                },
                "pwd": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "name"
            ]
        }
    },
    {
        "name": "zipfile_ZipExtFile_read1",
        "description": "Read up to n bytes with at most one read() system call.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "n": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "n"
            ]
        }
    },
    {
        "name": "zipfile_ZipExtFile_readable",
        "description": "读取数据（ZipExtFile类的方法）",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "zipfile_ZipExtFile_readline",
        "description": "Read and return a line from the stream.\nIf limit is specified, at most limit bytes will be read.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "limit": {
                    "type": "integer",
                    "default": -1,
                    "description": "类型从默认值推断: int"
                }
            },
            "required": []
        }
    },
    {
        "name": "zipfile_ZipExtFile_seek",
        "description": "执行seek操作（ZipExtFile类的方法）",
        "inputSchema": {
            "type": "object",
            "properties": {
                "offset": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "whence": {
                    "type": "integer",
                    "default": 0,
                    "description": "类型从默认值推断: int"
                }
            },
            "required": [
                "offset"
            ]
        }
    },
    {
        "name": "zipfile_ZipExtFile_seekable",
        "description": "执行seekable操作（ZipExtFile类的方法）",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "zipfile_ZipExtFile_tell",
        "description": "执行tell操作（ZipExtFile类的方法）",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "zipfile_ZipFile_close",
        "description": "Close the file, and for mode 'w', 'x' and 'a' write the ending\nrecords.",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "zipfile_ZipFile_extract",
        "description": "Extract a member from the archive to the current working directory,\nusing its full name. Its file information is extracted as accurately\nas possible. `member' may be a filename or a ZipInfo object. You can\nspecify a different directory using `path'.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "member": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "path": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "pwd": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "member"
            ]
        }
    },
    {
        "name": "zipfile_ZipFile_extractall",
        "description": "Extract all members from the archive to the current working\ndirectory. `path' specifies a different directory to extract to.\n`members' is optional and must be a subset of the list returned\nby namelist().",
        "inputSchema": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "members": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "pwd": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": []
        }
    },
    {
        "name": "zipfile_ZipFile_getinfo",
        "description": "Return the instance of ZipInfo given 'name'.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "类型从参数名推断: name"
                }
            },
            "required": [
                "name"
            ]
        }
    },
    {
        "name": "zipfile_ZipFile_infolist",
        "description": "Return a list of class ZipInfo instances for files in the\narchive.",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "zipfile_ZipFile_mkdir",
        "description": "Creates a directory inside the zip archive.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "zinfo_or_directory_name": {
                    "type": "string",
                    "description": "类型从参数名推断: zinfo_or_directory_name"
                },
                "mode": {
                    "type": "integer",
                    "default": 511,
                    "description": "类型从默认值推断: int"
                }
            },
            "required": [
                "zinfo_or_directory_name"
            ]
        }
    },
    {
        "name": "zipfile_ZipFile_namelist",
        "description": "Return a list of file names in the archive.",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "zipfile_ZipFile_open",
        "description": "Return file-like object for 'name'.\nname is a string for the file name within the ZIP file, or a ZipInfo\nobject.\nmode should be 'r' to read a file already in the ZIP file, or 'w' to\nwrite to a file newly added to the archive.\npwd is the password to decrypt files (only used for reading).\nWhen writing, if the file size is not known in advance but may exceed\n2 GiB, pass force_zip64 to use the ZIP64 format, which can handle large\nfiles.  If the size is known in advance, it is best to pass a ZipInfo\ninstance for name, with zinfo.file_size set.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "类型从参数名推断: name"
                },
                "mode": {
                    "type": "string",
                    "default": "r",
                    "description": "类型从默认值推断: str"
                },
                "pwd": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "force_zip64": {
                    "type": "integer",
                    "default": False,
                    "description": "类型从默认值推断: bool"
                }
            },
            "required": [
                "name"
            ]
        }
    },
    {
        "name": "zipfile_ZipFile_printdir",
        "description": "Print a table of contents for the zip file.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "file": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": []
        }
    },
    {
        "name": "zipfile_ZipFile_read",
        "description": "Return file bytes for name.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "类型从参数名推断: name"
                },
                "pwd": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "name"
            ]
        }
    },
    {
        "name": "zipfile_ZipFile_setpassword",
        "description": "Set default password for encrypted files.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "pwd": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "pwd"
            ]
        }
    },
    {
        "name": "zipfile_ZipFile_testzip",
        "description": "Read all the files and check the CRC.",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "zipfile_ZipFile_write",
        "description": "Put the bytes from filename into the archive under the name\narcname.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "filename": {
                    "type": "string",
                    "description": "类型从参数名推断: filename"
                },
                "arcname": {
                    "type": "string",
                    "description": "类型从参数名推断: arcname"
                },
                "compress_type": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "compresslevel": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "filename"
            ]
        }
    },
    {
        "name": "zipfile_ZipFile_writestr",
        "description": "Write a file into the archive.  The contents is 'data', which\nmay be either a 'str' or a 'bytes' instance; if it is a 'str',\nit is encoded as UTF-8 first.\n'zinfo_or_arcname' is either a ZipInfo instance or\nthe name of the file in the archive.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "zinfo_or_arcname": {
                    "type": "string",
                    "description": "类型从参数名推断: zinfo_or_arcname"
                },
                "data": {
                    "type": "object",
                    "description": "类型从参数名推断: data"
                },
                "compress_type": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "compresslevel": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "zinfo_or_arcname",
                "data"
            ]
        }
    },
    {
        "name": "zipfile_ZipInfo_FileHeader",
        "description": "Return the per-file header as a bytes object.\nWhen the optional zip64 arg is None rather than a bool, we will\ndecide based upon the file_size and compress_size, if known,\nFalse otherwise.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "zip64": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": []
        }
    },
    {
        "name": "zipfile_ZipInfo_is_dir",
        "description": "Return True if this archive member is a directory.",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    }
]


def handle_zipfile_is_zipfile(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_is_zipfile 工具调用"""
    try:
        # 解析函数路径: zipfile.is_zipfile
        parts = "zipfile.is_zipfile".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.is_zipfile")
        
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
        logger.error(f"执行 zipfile_is_zipfile 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_main(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_main 工具调用"""
    try:
        # 解析函数路径: zipfile.main
        parts = "zipfile.main".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.main")
        
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
        logger.error(f"执行 zipfile_main 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_CompleteDirs_close(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_CompleteDirs_close 工具调用"""
    try:
        # 解析函数路径: zipfile.CompleteDirs.close
        parts = "zipfile.CompleteDirs.close".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.CompleteDirs.close")
        
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
        logger.error(f"执行 zipfile_CompleteDirs_close 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_CompleteDirs_extract(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_CompleteDirs_extract 工具调用"""
    try:
        # 解析函数路径: zipfile.CompleteDirs.extract
        parts = "zipfile.CompleteDirs.extract".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.CompleteDirs.extract")
        
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
        logger.error(f"执行 zipfile_CompleteDirs_extract 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_CompleteDirs_extractall(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_CompleteDirs_extractall 工具调用"""
    try:
        # 解析函数路径: zipfile.CompleteDirs.extractall
        parts = "zipfile.CompleteDirs.extractall".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.CompleteDirs.extractall")
        
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
        logger.error(f"执行 zipfile_CompleteDirs_extractall 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_CompleteDirs_getinfo(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_CompleteDirs_getinfo 工具调用"""
    try:
        # 解析函数路径: zipfile.CompleteDirs.getinfo
        parts = "zipfile.CompleteDirs.getinfo".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.CompleteDirs.getinfo")
        
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
        logger.error(f"执行 zipfile_CompleteDirs_getinfo 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_CompleteDirs_infolist(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_CompleteDirs_infolist 工具调用"""
    try:
        # 解析函数路径: zipfile.CompleteDirs.infolist
        parts = "zipfile.CompleteDirs.infolist".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.CompleteDirs.infolist")
        
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
        logger.error(f"执行 zipfile_CompleteDirs_infolist 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_CompleteDirs_mkdir(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_CompleteDirs_mkdir 工具调用"""
    try:
        # 解析函数路径: zipfile.CompleteDirs.mkdir
        parts = "zipfile.CompleteDirs.mkdir".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.CompleteDirs.mkdir")
        
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
        logger.error(f"执行 zipfile_CompleteDirs_mkdir 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_CompleteDirs_namelist(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_CompleteDirs_namelist 工具调用"""
    try:
        # 解析函数路径: zipfile.CompleteDirs.namelist
        parts = "zipfile.CompleteDirs.namelist".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.CompleteDirs.namelist")
        
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
        logger.error(f"执行 zipfile_CompleteDirs_namelist 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_CompleteDirs_open(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_CompleteDirs_open 工具调用"""
    try:
        # 解析函数路径: zipfile.CompleteDirs.open
        parts = "zipfile.CompleteDirs.open".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.CompleteDirs.open")
        
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
        logger.error(f"执行 zipfile_CompleteDirs_open 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_CompleteDirs_printdir(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_CompleteDirs_printdir 工具调用"""
    try:
        # 解析函数路径: zipfile.CompleteDirs.printdir
        parts = "zipfile.CompleteDirs.printdir".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.CompleteDirs.printdir")
        
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
        logger.error(f"执行 zipfile_CompleteDirs_printdir 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_CompleteDirs_read(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_CompleteDirs_read 工具调用"""
    try:
        # 解析函数路径: zipfile.CompleteDirs.read
        parts = "zipfile.CompleteDirs.read".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.CompleteDirs.read")
        
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
        logger.error(f"执行 zipfile_CompleteDirs_read 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_CompleteDirs_resolve_dir(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_CompleteDirs_resolve_dir 工具调用"""
    try:
        # 解析函数路径: zipfile.CompleteDirs.resolve_dir
        parts = "zipfile.CompleteDirs.resolve_dir".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.CompleteDirs.resolve_dir")
        
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
        logger.error(f"执行 zipfile_CompleteDirs_resolve_dir 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_CompleteDirs_setpassword(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_CompleteDirs_setpassword 工具调用"""
    try:
        # 解析函数路径: zipfile.CompleteDirs.setpassword
        parts = "zipfile.CompleteDirs.setpassword".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.CompleteDirs.setpassword")
        
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
        logger.error(f"执行 zipfile_CompleteDirs_setpassword 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_CompleteDirs_testzip(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_CompleteDirs_testzip 工具调用"""
    try:
        # 解析函数路径: zipfile.CompleteDirs.testzip
        parts = "zipfile.CompleteDirs.testzip".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.CompleteDirs.testzip")
        
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
        logger.error(f"执行 zipfile_CompleteDirs_testzip 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_CompleteDirs_write(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_CompleteDirs_write 工具调用"""
    try:
        # 解析函数路径: zipfile.CompleteDirs.write
        parts = "zipfile.CompleteDirs.write".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.CompleteDirs.write")
        
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
        logger.error(f"执行 zipfile_CompleteDirs_write 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_CompleteDirs_writestr(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_CompleteDirs_writestr 工具调用"""
    try:
        # 解析函数路径: zipfile.CompleteDirs.writestr
        parts = "zipfile.CompleteDirs.writestr".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.CompleteDirs.writestr")
        
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
        logger.error(f"执行 zipfile_CompleteDirs_writestr 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_FastLookup_close(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_FastLookup_close 工具调用"""
    try:
        # 解析函数路径: zipfile.FastLookup.close
        parts = "zipfile.FastLookup.close".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.FastLookup.close")
        
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
        logger.error(f"执行 zipfile_FastLookup_close 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_FastLookup_extract(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_FastLookup_extract 工具调用"""
    try:
        # 解析函数路径: zipfile.FastLookup.extract
        parts = "zipfile.FastLookup.extract".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.FastLookup.extract")
        
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
        logger.error(f"执行 zipfile_FastLookup_extract 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_FastLookup_extractall(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_FastLookup_extractall 工具调用"""
    try:
        # 解析函数路径: zipfile.FastLookup.extractall
        parts = "zipfile.FastLookup.extractall".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.FastLookup.extractall")
        
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
        logger.error(f"执行 zipfile_FastLookup_extractall 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_FastLookup_getinfo(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_FastLookup_getinfo 工具调用"""
    try:
        # 解析函数路径: zipfile.FastLookup.getinfo
        parts = "zipfile.FastLookup.getinfo".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.FastLookup.getinfo")
        
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
        logger.error(f"执行 zipfile_FastLookup_getinfo 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_FastLookup_infolist(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_FastLookup_infolist 工具调用"""
    try:
        # 解析函数路径: zipfile.FastLookup.infolist
        parts = "zipfile.FastLookup.infolist".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.FastLookup.infolist")
        
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
        logger.error(f"执行 zipfile_FastLookup_infolist 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_FastLookup_mkdir(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_FastLookup_mkdir 工具调用"""
    try:
        # 解析函数路径: zipfile.FastLookup.mkdir
        parts = "zipfile.FastLookup.mkdir".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.FastLookup.mkdir")
        
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
        logger.error(f"执行 zipfile_FastLookup_mkdir 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_FastLookup_namelist(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_FastLookup_namelist 工具调用"""
    try:
        # 解析函数路径: zipfile.FastLookup.namelist
        parts = "zipfile.FastLookup.namelist".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.FastLookup.namelist")
        
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
        logger.error(f"执行 zipfile_FastLookup_namelist 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_FastLookup_open(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_FastLookup_open 工具调用"""
    try:
        # 解析函数路径: zipfile.FastLookup.open
        parts = "zipfile.FastLookup.open".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.FastLookup.open")
        
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
        logger.error(f"执行 zipfile_FastLookup_open 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_FastLookup_printdir(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_FastLookup_printdir 工具调用"""
    try:
        # 解析函数路径: zipfile.FastLookup.printdir
        parts = "zipfile.FastLookup.printdir".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.FastLookup.printdir")
        
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
        logger.error(f"执行 zipfile_FastLookup_printdir 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_FastLookup_read(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_FastLookup_read 工具调用"""
    try:
        # 解析函数路径: zipfile.FastLookup.read
        parts = "zipfile.FastLookup.read".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.FastLookup.read")
        
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
        logger.error(f"执行 zipfile_FastLookup_read 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_FastLookup_resolve_dir(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_FastLookup_resolve_dir 工具调用"""
    try:
        # 解析函数路径: zipfile.FastLookup.resolve_dir
        parts = "zipfile.FastLookup.resolve_dir".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.FastLookup.resolve_dir")
        
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
        logger.error(f"执行 zipfile_FastLookup_resolve_dir 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_FastLookup_setpassword(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_FastLookup_setpassword 工具调用"""
    try:
        # 解析函数路径: zipfile.FastLookup.setpassword
        parts = "zipfile.FastLookup.setpassword".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.FastLookup.setpassword")
        
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
        logger.error(f"执行 zipfile_FastLookup_setpassword 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_FastLookup_testzip(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_FastLookup_testzip 工具调用"""
    try:
        # 解析函数路径: zipfile.FastLookup.testzip
        parts = "zipfile.FastLookup.testzip".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.FastLookup.testzip")
        
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
        logger.error(f"执行 zipfile_FastLookup_testzip 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_FastLookup_write(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_FastLookup_write 工具调用"""
    try:
        # 解析函数路径: zipfile.FastLookup.write
        parts = "zipfile.FastLookup.write".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.FastLookup.write")
        
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
        logger.error(f"执行 zipfile_FastLookup_write 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_FastLookup_writestr(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_FastLookup_writestr 工具调用"""
    try:
        # 解析函数路径: zipfile.FastLookup.writestr
        parts = "zipfile.FastLookup.writestr".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.FastLookup.writestr")
        
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
        logger.error(f"执行 zipfile_FastLookup_writestr 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_LZMACompressor_compress(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_LZMACompressor_compress 工具调用"""
    try:
        # 解析函数路径: zipfile.LZMACompressor.compress
        parts = "zipfile.LZMACompressor.compress".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.LZMACompressor.compress")
        
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
        logger.error(f"执行 zipfile_LZMACompressor_compress 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_LZMACompressor_flush(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_LZMACompressor_flush 工具调用"""
    try:
        # 解析函数路径: zipfile.LZMACompressor.flush
        parts = "zipfile.LZMACompressor.flush".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.LZMACompressor.flush")
        
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
        logger.error(f"执行 zipfile_LZMACompressor_flush 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_LZMADecompressor_decompress(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_LZMADecompressor_decompress 工具调用"""
    try:
        # 解析函数路径: zipfile.LZMADecompressor.decompress
        parts = "zipfile.LZMADecompressor.decompress".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.LZMADecompressor.decompress")
        
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
        logger.error(f"执行 zipfile_LZMADecompressor_decompress 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_Path_exists(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_Path_exists 工具调用"""
    try:
        # 解析函数路径: zipfile.Path.exists
        parts = "zipfile.Path.exists".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.Path.exists")
        
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
        logger.error(f"执行 zipfile_Path_exists 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_Path_is_dir(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_Path_is_dir 工具调用"""
    try:
        # 解析函数路径: zipfile.Path.is_dir
        parts = "zipfile.Path.is_dir".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.Path.is_dir")
        
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
        logger.error(f"执行 zipfile_Path_is_dir 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_Path_is_file(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_Path_is_file 工具调用"""
    try:
        # 解析函数路径: zipfile.Path.is_file
        parts = "zipfile.Path.is_file".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.Path.is_file")
        
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
        logger.error(f"执行 zipfile_Path_is_file 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_Path_iterdir(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_Path_iterdir 工具调用"""
    try:
        # 解析函数路径: zipfile.Path.iterdir
        parts = "zipfile.Path.iterdir".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.Path.iterdir")
        
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
        logger.error(f"执行 zipfile_Path_iterdir 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_Path_joinpath(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_Path_joinpath 工具调用"""
    try:
        # 解析函数路径: zipfile.Path.joinpath
        parts = "zipfile.Path.joinpath".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.Path.joinpath")
        
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
        logger.error(f"执行 zipfile_Path_joinpath 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_Path_open(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_Path_open 工具调用"""
    try:
        # 解析函数路径: zipfile.Path.open
        parts = "zipfile.Path.open".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.Path.open")
        
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
        logger.error(f"执行 zipfile_Path_open 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_Path_read_bytes(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_Path_read_bytes 工具调用"""
    try:
        # 解析函数路径: zipfile.Path.read_bytes
        parts = "zipfile.Path.read_bytes".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.Path.read_bytes")
        
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
        logger.error(f"执行 zipfile_Path_read_bytes 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_Path_read_text(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_Path_read_text 工具调用"""
    try:
        # 解析函数路径: zipfile.Path.read_text
        parts = "zipfile.Path.read_text".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.Path.read_text")
        
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
        logger.error(f"执行 zipfile_Path_read_text 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_PyZipFile_close(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_PyZipFile_close 工具调用"""
    try:
        # 解析函数路径: zipfile.PyZipFile.close
        parts = "zipfile.PyZipFile.close".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.PyZipFile.close")
        
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
        logger.error(f"执行 zipfile_PyZipFile_close 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_PyZipFile_extract(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_PyZipFile_extract 工具调用"""
    try:
        # 解析函数路径: zipfile.PyZipFile.extract
        parts = "zipfile.PyZipFile.extract".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.PyZipFile.extract")
        
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
        logger.error(f"执行 zipfile_PyZipFile_extract 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_PyZipFile_extractall(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_PyZipFile_extractall 工具调用"""
    try:
        # 解析函数路径: zipfile.PyZipFile.extractall
        parts = "zipfile.PyZipFile.extractall".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.PyZipFile.extractall")
        
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
        logger.error(f"执行 zipfile_PyZipFile_extractall 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_PyZipFile_getinfo(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_PyZipFile_getinfo 工具调用"""
    try:
        # 解析函数路径: zipfile.PyZipFile.getinfo
        parts = "zipfile.PyZipFile.getinfo".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.PyZipFile.getinfo")
        
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
        logger.error(f"执行 zipfile_PyZipFile_getinfo 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_PyZipFile_infolist(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_PyZipFile_infolist 工具调用"""
    try:
        # 解析函数路径: zipfile.PyZipFile.infolist
        parts = "zipfile.PyZipFile.infolist".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.PyZipFile.infolist")
        
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
        logger.error(f"执行 zipfile_PyZipFile_infolist 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_PyZipFile_mkdir(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_PyZipFile_mkdir 工具调用"""
    try:
        # 解析函数路径: zipfile.PyZipFile.mkdir
        parts = "zipfile.PyZipFile.mkdir".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.PyZipFile.mkdir")
        
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
        logger.error(f"执行 zipfile_PyZipFile_mkdir 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_PyZipFile_namelist(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_PyZipFile_namelist 工具调用"""
    try:
        # 解析函数路径: zipfile.PyZipFile.namelist
        parts = "zipfile.PyZipFile.namelist".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.PyZipFile.namelist")
        
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
        logger.error(f"执行 zipfile_PyZipFile_namelist 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_PyZipFile_open(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_PyZipFile_open 工具调用"""
    try:
        # 解析函数路径: zipfile.PyZipFile.open
        parts = "zipfile.PyZipFile.open".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.PyZipFile.open")
        
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
        logger.error(f"执行 zipfile_PyZipFile_open 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_PyZipFile_printdir(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_PyZipFile_printdir 工具调用"""
    try:
        # 解析函数路径: zipfile.PyZipFile.printdir
        parts = "zipfile.PyZipFile.printdir".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.PyZipFile.printdir")
        
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
        logger.error(f"执行 zipfile_PyZipFile_printdir 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_PyZipFile_read(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_PyZipFile_read 工具调用"""
    try:
        # 解析函数路径: zipfile.PyZipFile.read
        parts = "zipfile.PyZipFile.read".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.PyZipFile.read")
        
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
        logger.error(f"执行 zipfile_PyZipFile_read 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_PyZipFile_setpassword(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_PyZipFile_setpassword 工具调用"""
    try:
        # 解析函数路径: zipfile.PyZipFile.setpassword
        parts = "zipfile.PyZipFile.setpassword".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.PyZipFile.setpassword")
        
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
        logger.error(f"执行 zipfile_PyZipFile_setpassword 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_PyZipFile_testzip(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_PyZipFile_testzip 工具调用"""
    try:
        # 解析函数路径: zipfile.PyZipFile.testzip
        parts = "zipfile.PyZipFile.testzip".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.PyZipFile.testzip")
        
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
        logger.error(f"执行 zipfile_PyZipFile_testzip 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_PyZipFile_write(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_PyZipFile_write 工具调用"""
    try:
        # 解析函数路径: zipfile.PyZipFile.write
        parts = "zipfile.PyZipFile.write".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.PyZipFile.write")
        
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
        logger.error(f"执行 zipfile_PyZipFile_write 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_PyZipFile_writepy(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_PyZipFile_writepy 工具调用"""
    try:
        # 解析函数路径: zipfile.PyZipFile.writepy
        parts = "zipfile.PyZipFile.writepy".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.PyZipFile.writepy")
        
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
        logger.error(f"执行 zipfile_PyZipFile_writepy 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_PyZipFile_writestr(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_PyZipFile_writestr 工具调用"""
    try:
        # 解析函数路径: zipfile.PyZipFile.writestr
        parts = "zipfile.PyZipFile.writestr".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.PyZipFile.writestr")
        
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
        logger.error(f"执行 zipfile_PyZipFile_writestr 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_ZipExtFile_close(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_ZipExtFile_close 工具调用"""
    try:
        # 解析函数路径: zipfile.ZipExtFile.close
        parts = "zipfile.ZipExtFile.close".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.ZipExtFile.close")
        
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
        logger.error(f"执行 zipfile_ZipExtFile_close 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_ZipExtFile_peek(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_ZipExtFile_peek 工具调用"""
    try:
        # 解析函数路径: zipfile.ZipExtFile.peek
        parts = "zipfile.ZipExtFile.peek".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.ZipExtFile.peek")
        
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
        logger.error(f"执行 zipfile_ZipExtFile_peek 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_ZipExtFile_read(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_ZipExtFile_read 工具调用"""
    try:
        # 解析函数路径: zipfile.ZipExtFile.read
        parts = "zipfile.ZipExtFile.read".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.ZipExtFile.read")
        
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
        logger.error(f"执行 zipfile_ZipExtFile_read 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_ZipExtFile_read1(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_ZipExtFile_read1 工具调用"""
    try:
        # 解析函数路径: zipfile.ZipExtFile.read1
        parts = "zipfile.ZipExtFile.read1".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.ZipExtFile.read1")
        
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
        logger.error(f"执行 zipfile_ZipExtFile_read1 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_ZipExtFile_readable(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_ZipExtFile_readable 工具调用"""
    try:
        # 解析函数路径: zipfile.ZipExtFile.readable
        parts = "zipfile.ZipExtFile.readable".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.ZipExtFile.readable")
        
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
        logger.error(f"执行 zipfile_ZipExtFile_readable 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_ZipExtFile_readline(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_ZipExtFile_readline 工具调用"""
    try:
        # 解析函数路径: zipfile.ZipExtFile.readline
        parts = "zipfile.ZipExtFile.readline".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.ZipExtFile.readline")
        
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
        logger.error(f"执行 zipfile_ZipExtFile_readline 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_ZipExtFile_seek(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_ZipExtFile_seek 工具调用"""
    try:
        # 解析函数路径: zipfile.ZipExtFile.seek
        parts = "zipfile.ZipExtFile.seek".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.ZipExtFile.seek")
        
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
        logger.error(f"执行 zipfile_ZipExtFile_seek 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_ZipExtFile_seekable(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_ZipExtFile_seekable 工具调用"""
    try:
        # 解析函数路径: zipfile.ZipExtFile.seekable
        parts = "zipfile.ZipExtFile.seekable".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.ZipExtFile.seekable")
        
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
        logger.error(f"执行 zipfile_ZipExtFile_seekable 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_ZipExtFile_tell(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_ZipExtFile_tell 工具调用"""
    try:
        # 解析函数路径: zipfile.ZipExtFile.tell
        parts = "zipfile.ZipExtFile.tell".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.ZipExtFile.tell")
        
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
        logger.error(f"执行 zipfile_ZipExtFile_tell 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_ZipFile_close(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_ZipFile_close 工具调用"""
    try:
        # 解析函数路径: zipfile.ZipFile.close
        parts = "zipfile.ZipFile.close".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.ZipFile.close")
        
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
        logger.error(f"执行 zipfile_ZipFile_close 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_ZipFile_extract(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_ZipFile_extract 工具调用"""
    try:
        # 解析函数路径: zipfile.ZipFile.extract
        parts = "zipfile.ZipFile.extract".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.ZipFile.extract")
        
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
        logger.error(f"执行 zipfile_ZipFile_extract 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_ZipFile_extractall(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_ZipFile_extractall 工具调用"""
    try:
        # 解析函数路径: zipfile.ZipFile.extractall
        parts = "zipfile.ZipFile.extractall".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.ZipFile.extractall")
        
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
        logger.error(f"执行 zipfile_ZipFile_extractall 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_ZipFile_getinfo(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_ZipFile_getinfo 工具调用"""
    try:
        # 解析函数路径: zipfile.ZipFile.getinfo
        parts = "zipfile.ZipFile.getinfo".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.ZipFile.getinfo")
        
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
        logger.error(f"执行 zipfile_ZipFile_getinfo 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_ZipFile_infolist(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_ZipFile_infolist 工具调用"""
    try:
        # 解析函数路径: zipfile.ZipFile.infolist
        parts = "zipfile.ZipFile.infolist".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.ZipFile.infolist")
        
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
        logger.error(f"执行 zipfile_ZipFile_infolist 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_ZipFile_mkdir(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_ZipFile_mkdir 工具调用"""
    try:
        # 解析函数路径: zipfile.ZipFile.mkdir
        parts = "zipfile.ZipFile.mkdir".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.ZipFile.mkdir")
        
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
        logger.error(f"执行 zipfile_ZipFile_mkdir 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_ZipFile_namelist(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_ZipFile_namelist 工具调用"""
    try:
        # 解析函数路径: zipfile.ZipFile.namelist
        parts = "zipfile.ZipFile.namelist".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.ZipFile.namelist")
        
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
        logger.error(f"执行 zipfile_ZipFile_namelist 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_ZipFile_open(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_ZipFile_open 工具调用"""
    try:
        # 解析函数路径: zipfile.ZipFile.open
        parts = "zipfile.ZipFile.open".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.ZipFile.open")
        
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
        logger.error(f"执行 zipfile_ZipFile_open 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_ZipFile_printdir(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_ZipFile_printdir 工具调用"""
    try:
        # 解析函数路径: zipfile.ZipFile.printdir
        parts = "zipfile.ZipFile.printdir".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.ZipFile.printdir")
        
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
        logger.error(f"执行 zipfile_ZipFile_printdir 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_ZipFile_read(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_ZipFile_read 工具调用"""
    try:
        # 解析函数路径: zipfile.ZipFile.read
        parts = "zipfile.ZipFile.read".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.ZipFile.read")
        
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
        logger.error(f"执行 zipfile_ZipFile_read 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_ZipFile_setpassword(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_ZipFile_setpassword 工具调用"""
    try:
        # 解析函数路径: zipfile.ZipFile.setpassword
        parts = "zipfile.ZipFile.setpassword".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.ZipFile.setpassword")
        
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
        logger.error(f"执行 zipfile_ZipFile_setpassword 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_ZipFile_testzip(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_ZipFile_testzip 工具调用"""
    try:
        # 解析函数路径: zipfile.ZipFile.testzip
        parts = "zipfile.ZipFile.testzip".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.ZipFile.testzip")
        
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
        logger.error(f"执行 zipfile_ZipFile_testzip 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_ZipFile_write(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_ZipFile_write 工具调用"""
    try:
        # 解析函数路径: zipfile.ZipFile.write
        parts = "zipfile.ZipFile.write".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.ZipFile.write")
        
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
        logger.error(f"执行 zipfile_ZipFile_write 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_ZipFile_writestr(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_ZipFile_writestr 工具调用"""
    try:
        # 解析函数路径: zipfile.ZipFile.writestr
        parts = "zipfile.ZipFile.writestr".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.ZipFile.writestr")
        
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
        logger.error(f"执行 zipfile_ZipFile_writestr 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_ZipInfo_FileHeader(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_ZipInfo_FileHeader 工具调用"""
    try:
        # 解析函数路径: zipfile.ZipInfo.FileHeader
        parts = "zipfile.ZipInfo.FileHeader".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.ZipInfo.FileHeader")
        
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
        logger.error(f"执行 zipfile_ZipInfo_FileHeader 失败: {e}")
        return {"error": str(e)}


def handle_zipfile_ZipInfo_is_dir(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 zipfile_ZipInfo_is_dir 工具调用"""
    try:
        # 解析函数路径: zipfile.ZipInfo.is_dir
        parts = "zipfile.ZipInfo.is_dir".split('.')
        
        if parts[0] != "zipfile":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # zipfile.function_name
            func_name = parts[1]
            func = getattr(zipfile, func_name)
        elif len(parts) >= 3:
            # zipfile.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: zipfile.ZipInfo.is_dir")
        
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
        logger.error(f"执行 zipfile_ZipInfo_is_dir 失败: {e}")
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
                        "name": "zipfile-mcp-server",
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
    logger.info("启动 zipfile MCP 服务器...")
    
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
