# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           protobuf-c
Version:        1.5.2
Release:        %autorelease
Summary:        C bindings for Google's Protocol Buffers
License:        BSD-2-Clause
URL:            https://github.com/protobuf-c/protobuf-c
#!RemoteAsset
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(protobuf)

%description
Protocol Buffers are a way of encoding structured data in an efficient yet
extensible format. This package provides a code generator and run-time
libraries to use Protocol Buffers from pure C (not C++).

It uses a modified version of protoc called protoc-c.

%package        compiler
Summary:        Protocol Buffers C compiler
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description compiler
This package contains a modified version of the Protocol Buffers
compiler for the C programming language called protoc-c.

%package        devel
Summary:        Protocol Buffers C headers and libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-compiler%{?_isa} = %{version}-%{release}

%description    devel
This package contains protobuf-c headers and libraries.

%files
%license LICENSE
%doc README.md TODO
%{_libdir}/libprotobuf-c.so.1*

%files compiler
%{_bindir}/protoc-c
%{_bindir}/protoc-gen-c

%files devel
%dir %{_includedir}/google
%{_includedir}/protobuf-c/
%{_includedir}/google/protobuf-c/
%{_libdir}/libprotobuf-c.so
%{_libdir}/pkgconfig/libprotobuf-c.pc

%changelog
%autochangelog
