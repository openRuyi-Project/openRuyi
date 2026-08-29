# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           erofs-utils
Version:        1.9.1
Release:        %autorelease
Summary:        Utilities for the Extendable Read-Only Filesystem (EROFS)
License:        GPL-2.0-or-later
URL:            https://github.com/erofs/erofs-utils
VCS:            git:https://github.com/erofs/erofs-utils.git
#!RemoteAsset:  sha256:a9ef5ab67c4b8d2d3e9ed71f39cd008bda653142a720d8a395a36f1110d0c432
Source:         https://github.com/erofs/erofs-utils/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --enable-lzma

BuildRequires:  autoconf >= 2.69
BuildRequires:  automake
BuildRequires:  lz4-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(liblzma) >= 5.3.2
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(zlib)
Supplements:    filesystem(erofs)

%description
mkfs.erofs is a user-space tool to create EROFS filesystem images. It supports
various compression algorithms and features for creating efficient read-only
filesystems, especially for embedded devices.

%conf -p
autoreconf -fiv

%files
%license COPYING
%{_bindir}/*erofs
%{_mandir}/man1/*erofs*
%{_mandir}/man8/*erofs*

%changelog
%autochangelog
