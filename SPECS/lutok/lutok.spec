# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           lutok
Version:        0.6.1
Release:        %autorelease
Summary:        A lightweight C++ API library for Lua
License:        BSD-3-Clause
URL:            https://github.com/jmmv/lutok
#!RemoteAsset
Source:         https://github.com/freebsd/lutok/archive/refs/tags/lutok-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --without-doxygen

BuildRequires:  gcc-c++
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(lua)
BuildRequires:  make

Requires:       lua

%description
Lutok provides thin C++ wrappers around the Lua C API to ease the
interaction between C++ and Lua.

%package        devel
Summary:        Development files for the Lutok library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(lua)

%description    devel
This package provides the header files, pkg-config files, and symbolic links
needed to develop applications that use the Lutok library.

%conf -p
autoreconf -fiv

%files
%license COPYING
%doc AUTHORS NEWS
%doc %{_docdir}/lutok
%{_libdir}/liblutok.so*

%files devel
%{_includedir}/lutok
%{_libdir}/liblutok.so
%{_libdir}/pkgconfig/lutok.pc

%changelog
%autochangelog
