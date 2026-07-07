#!/usr/bin/env python3

# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

import sys
import subprocess
from datetime import datetime
from typing import Set, List
from pathlib import Path

try:
    from reuse.header import find_and_replace_header, extract_reuse_info
    from reuse.comment import PythonCommentStyle
    from reuse.copyright import CopyrightNotice, ReuseInfo, SpdxExpression, YearRange, CopyrightPrefix
except ImportError as e:
    print(f"Error: REUSE API missing: {e}", file=sys.stderr)
    sys.exit(1)

# --- 默认配置 ---
DEFAULT_HOLDERS = [
    "Institute of Software, Chinese Academy of Sciences (ISCAS)",
    "openRuyi Project Contributors"
]
DEFAULT_LICENSE = "MulanPSL-2.0"

def get_first_git_year(file_path: Path) -> int:
    """获取文件的第一次 git 提交年份"""
    try:
        res = subprocess.run(
            ['git', 'log', '--reverse', '--format=%ad', '--date=format:%Y', '--', str(file_path)],
            capture_output=True, text=True, timeout=3
        )
        if res.returncode == 0:
            first_year = res.stdout.strip().split('\n')[0]
            if first_year.isdigit():
                return int(first_year)
    except:
        pass
    return datetime.now().year

def update_file(file_path_str: str):
    file_path = Path(file_path_str).resolve()
    if not file_path.exists():
        return

    # 读取文件内容
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}", file=sys.stderr)
        return

    # 使用 reuse 库检查是否已经有头部
    from reuse.extract import contains_reuse_info
    if contains_reuse_info(original_content):
        # 文件已经有 SPDX 头部，跳过
        return

    # 获取第一次提交的年份
    year = get_first_git_year(file_path)
    
    # 构造 ReuseInfo 对象
    year_range = YearRange(start=str(year), separator=None, end=None)
    new_notices = {
        CopyrightNotice(name=holder, prefix=CopyrightPrefix.SPDX_C, years=(year_range,))
        for holder in DEFAULT_HOLDERS
    }
    new_info = ReuseInfo(
        copyright_notices=new_notices,
        spdx_expressions={SpdxExpression(DEFAULT_LICENSE)},
        contributor_lines=[]
    )

    # 使用 reuse 库添加新头部
    from reuse.header import add_new_header
    final_content = add_new_header(
        original_content,
        new_info,
        style=PythonCommentStyle
    )

    # 写回文件
    if final_content.strip() != original_content.strip():
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(final_content)
        print(f"Added header to {file_path}")

def main():
    for arg in sys.argv[1:]:
        try:
            update_file(arg)
        except Exception as e:
            print(f"Error processing {arg}: {e}")

if __name__ == "__main__":
    main()
