# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           pixz
Version:        1.0.7
Release:        %autorelease
Summary:        A parallel, indexing version of XZ
License:        BSD-2-Clause
URL:            https://github.com/vasi/pixz
#!RemoteAsset
Source:         https://github.com/vasi/pixz/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    autotools

# build manpage when we have asciidoc
BuildOption(conf):  --without-manpage
BuildOption(build):  CFLAGS="%{optflags} -fcommon"

BuildRequires:  pkgconfig
BuildRequires:  autoconf
BuildRequires:  xz
BuildRequires:  automake
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(liblzma)

%description
Pixz is a parallel, indexing version of XZ. It produces a collection of
smaller blocks which makes random access to the original data possible.
This is especially useful for large tarballs.

%conf -p
autoreconf -fiv

%files
%license LICENSE
%doc NEWS TODO README.md
%{_bindir}/pixz

%changelog
%autochangelog
