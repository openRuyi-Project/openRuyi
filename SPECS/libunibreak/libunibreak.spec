# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define altver 6_1

Name:           libunibreak
Version:        6.1
Release:        %autorelease
Summary:        Unicode line-breaking library
License:        Zlib
URL:            https://github.com/adah1972/libunibreak
#!RemoteAsset
Source:         https://github.com/adah1972/libunibreak/releases/download/libunibreak_%{altver}/libunibreak-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  pkgconfig
BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  automake

%description
Libunibreak is an implementation of the Unicode line breaking and word breaking
algorithms. This is a metapackage that requires the runtime library.

%package        devel
Summary:        Development files for libunibreak
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
This package contains the header files and libraries for developing
applications that use the libunibreak library.

%files
%license LICENCE
%doc AUTHORS NEWS README.md
%{_libdir}/*.so.6*

%files devel
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/libunibreak.pc

%changelog
%autochangelog
