# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: laokz <zhangkai@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           c-ares
Version:        1.34.6
Release:        %autorelease
Summary:        Library for asynchronous name resolves
License:        MIT
URL:            https://c-ares.org/
VCS:            git:https://github.com/c-ares/c-ares
#!RemoteAsset
Source0:        https://github.com/c-ares/c-ares/releases/download/v%{version}/c-ares-%{version}.tar.gz
#!RemoteAsset
Source1:        https://github.com/c-ares/c-ares/releases/download/v%{version}/c-ares-%{version}.tar.gz.asc
BuildSystem:    cmake

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  pkgconfig

%description
c-ares is a C library that performs DNS requests and name resolves
asynchronously. c-ares is a fork of the library named 'ares', written
by Greg Hudson at MIT.

%package        devel
Summary:        Development files for c-ares
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       glibc-devel
Provides:       c-ares-devel = %{version}-%{release}

%description    devel
c-ares is a C library that performs DNS requests and name resolves
asynchronously. c-ares is a fork of the library named 'ares', written
by Greg Hudson at MIT.

This package provides the development libraries and headers needed
to build packages that depend on c-ares.

%files
%license LICENSE.md
%{_bindir}/adig
%{_bindir}/ahost
%{_mandir}/man1/adig.*
%{_mandir}/man1/ahost.*
%{_libdir}/libcares.so.*

%files devel
%license LICENSE.md
%{_libdir}/libcares.so
%{_includedir}/*.h
%{_mandir}/man3/ares_*
%{_libdir}/pkgconfig/libcares.pc
%{_libdir}/cmake/c-ares/

%changelog
%autochangelog
