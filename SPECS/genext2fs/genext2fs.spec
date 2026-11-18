# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           genext2fs
Version:        1.6.3
Release:        %autorelease
Summary:        ext2 filesystem generator
License:        GPL-2.0-only
URL:            https://github.com/bestouff/genext2fs/
#!RemoteAsset:  sha256:e3503a5bae3fd4b5b2c2d4f49b5b7f8d08e7accb20ab28c0f9647389b2c8a079
Source0:        https://github.com/bestouff/genext2fs/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    autotools

# Store full ino_t in struct hdlink_s to preserve 64-bit host inode numbers
Patch2000:      2000-fix-64bit-inode-hardlink.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  e2fsprogs
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(python3)

%description
genext2fs generates an ext2 filesystem as a normal (non-root) user.
It does not require you to mount the image file to copy files on it,
nor does it require that you become the superuser to make device nodes.

%conf -p
autoreconf -fi

%files
%doc AUTHORS README.md
%license COPYING
%{_bindir}/genext2fs
%{_mandir}/man8/genext2fs.8*

%changelog
%autochangelog
