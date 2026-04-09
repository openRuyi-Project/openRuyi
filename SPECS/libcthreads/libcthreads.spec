# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libcthreads
Version:        20240413
Release:        %autorelease
Summary:        Library for cross-platform C threads functions
License:        LGPL-3.0-or-later
URL:            https://github.com/libyal/libcthreads
#!RemoteAsset
Source0:        %{url}/releases/download/%{version}/libcthreads-alpha-%{version}.tar.gz
#!RemoteAsset
Source1:        %{url}/releases/download/%{version}/libcthreads-alpha-%{version}.tar.gz.asc
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  gcc
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcerror) >= 20240413

%description
libcthreads is a library for cross-platform C threads functions.

This package is part of the libyal library collection.

%package        devel
Summary:        Development files for libcthreads, a C thread library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
libcthreads is a library for cross-platform C threads functions.

This subpackage contains libraries and header files for developing
applications that want to make use of libcthreads.

%files
%license COPYING.LESSER
%{_libdir}/libcthreads.so.1*

%files devel
%{_includedir}/libcthreads*
%{_libdir}/libcthreads.so
%{_libdir}/pkgconfig/libcthreads.pc
%{_mandir}/man3/libcthreads.3*

%changelog
%autochangelog
