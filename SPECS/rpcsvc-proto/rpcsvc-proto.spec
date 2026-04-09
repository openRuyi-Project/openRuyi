# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           rpcsvc-proto
Version:        1.4.4
Release:        %autorelease
Summary:        RPC protocol definitions and rpcgen compiler
License:        BSD-3-Clause
URL:            https://github.com/thkukuk/rpcsvc-proto
#!RemoteAsset
Source:         https://github.com/thkukuk/rpcsvc-proto/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  libtool
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  make
BuildRequires:  gcc

%description
The rpcsvc-proto package includes several rpcsvc header files
and the rpcgen protocol compiler from SunRPC sources.
This is a metapackage for dependency resolution.

%package     -n rpcgen
Summary:        RPC protocol compiler

%description -n rpcgen
rpcgen is a tool that generates C code to implement an RPC protocol.
The input to rpcgen is a language similar to C known as RPC Language
(Remote Procedure Call Language).

%package        devel
Summary:        RPC protocol definition header files

%description    devel
This package includes several rpcsvc header files from SunRPC sources
(as formerly shipped with glibc).

%conf -p
autoreconf -fiv

%files -n rpcgen
%license COPYING
%{_bindir}/rpcgen
%{_mandir}/man1/rpcgen.1*

%files devel
%license COPYING
%dir %{_includedir}/rpcsvc
%{_includedir}/rpcsvc/*

%changelog
%autochangelog
