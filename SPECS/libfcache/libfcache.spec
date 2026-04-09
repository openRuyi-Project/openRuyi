# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libfcache
Version:        20240414
Release:        %autorelease
Summary:        Library to provide generic file data cache functions
License:        LGPL-3.0-or-later
URL:            https://github.com/libyal/libfcache
#!RemoteAsset
Source0:        %{url}/releases/download/%{version}/libfcache-alpha-%{version}.tar.gz
#!RemoteAsset
Source1:        %{url}/releases/download/%{version}/libfcache-alpha-%{version}.tar.gz.asc
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  gcc
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcdata) >= 20240414
BuildRequires:  pkgconfig(libcerror) >= 20240413
BuildRequires:  pkgconfig(libcthreads) >= 20240413

%description
libfcache is a library to provide generic file data cache functions.

This package is part of the libyal library collection and is used by
other libraries in the collection.

%package        devel
Summary:        Development files for libfcache
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
libfcache is a library to provide generic file data cache functions.

This subpackage contains libraries and header files for developing
applications that want to make use of libfcache.

%files
%license COPYING*
%{_libdir}/libfcache.so.*

%files devel
%license COPYING*
%{_includedir}/libfcache.h
%{_includedir}/libfcache/
%{_libdir}/libfcache.so
%{_libdir}/pkgconfig/libfcache.pc
%{_mandir}/man3/libfcache.3*

%changelog
%autochangelog
