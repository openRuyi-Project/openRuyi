#!/usr/bin/env python3

# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: lzyprime <2383518170@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

import sys
import re

def check_file(file_path):
    errors = []
    lines = [line.strip() for line in open(file_path).readlines()]

    sourcelines = [idx for idx,line in enumerate(lines) if re.match(r'^Source(\d+)?:\s+(https?://|%{url})', line)]


    # 步骤2: 如果存在，检查每一个 Source\d+ 行是否有注释
    for idx in sourcelines:
        if not re.match(r'^#!RemoteAsset:  sha256:[0-9a-f]{64}$', lines[idx - 1]):
            errors.append(f'\033[33m{file_path}:{idx}-{idx+1}\033[0m: \033[1;31mError\033[0m - The source line is missing the required #!RemoteAsset:  sha256:xxx comment.\n{lines[idx-1]}\n{lines[idx]}\n---')

    return errors

def main():
    all_errors = []
    for file_path in sys.argv[1:]:
        all_errors.extend(check_file(file_path))

    if all_errors:
        print('\n'.join(all_errors))
    sys.exit(len(all_errors))

if __name__ == '__main__':
    main()
