# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           llhttp
Version:        9.3.0
Release:        %autorelease
Summary:        Port of http_parser to llparse
License:        MIT
URL:            https://github.com/nodejs/llhttp
#!RemoteAsset
Source:         https://github.com/nodejs/llhttp/archive/refs/tags/release/v%{version}.tar.gz
BuildSystem:    cmake

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++

%description
This project is a port of http_parser to TypeScript. llparse is used to
generate the output C source file, which can be compiled and linked.

%package devel
Summary:        Development files for llhttp
Requires:       %{name} = %{version}

%description devel
The llhttp-devel package contains libraries and header files for
developing applications that use llhttp.

%files
%license LICENSE
%doc README.md
%{_libdir}/libllhttp.so*

%files devel
%{_includedir}/llhttp.h
%{_libdir}/libllhttp.so
%{_libdir}/pkgconfig/libllhttp.pc
%{_libdir}/cmake/llhttp/

%changelog
%{?autochangelog}
