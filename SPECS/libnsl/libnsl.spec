# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libnsl
Version:        2.0.1
Release:        %autorelease
Summary:        Public client interface library for NIS(YP) and NIS+
License:        BSD-3-Clause AND LGPL-2.1-or-later
URL:            https://github.com/thkukuk/libnsl
#!RemoteAsset
Source0:        %{url}/archive/v%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(libtirpc)

%description
This package contains the libnsl library. This library contains
the public client interface for NIS(YP) and NIS+.
This code was formerly part of glibc, but is now standalone to
be able to link against TI-RPC for IPv6 support.

%package        devel
Summary:        Development files for libnsl
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for libnsl2

%conf -p
autoreconf -fiv

%install -a
rm %{buildroot}%{_libdir}/%{name}.la

%files
%license COPYING
%{_libdir}/libnsl.so.*

%files devel
%{_libdir}/libnsl.so
%{_includedir}/*
%{_libdir}/pkgconfig/libnsl.pc

%changelog
%{?autochangelog}
