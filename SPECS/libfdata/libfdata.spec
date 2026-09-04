# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libfdata
Version:        20260521
Release:        %autorelease
Summary:        Library to provide generic file data functions
License:        LGPL-3.0-or-later
URL:            https://github.com/libyal/libfdata
#!RemoteAsset:  sha256:42a8a8f50b3c52cea4bcf79f9a47aa152fbef509f7c910edb2ed1890c2adee2d
Source0:        %{url}/releases/download/%{version}/libfdata-alpha-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcdata) >= 20240414
BuildRequires:  pkgconfig(libcerror) >= 20240413
BuildRequires:  pkgconfig(libcnotify) >= 20240414
BuildRequires:  pkgconfig(libcthreads) >= 20240413
BuildRequires:  pkgconfig(libfcache) >= 20240414

%description
libfdata is a library to provide generic file data functions for the libyal family of libraries.

%package        devel
Summary:        Development files for libfdata
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
libfdata is a library to provide generic file data functions for the libyal family of libraries.

This subpackage contains libraries and header files for developing
applications that want to make use of libfdata.

%files
%license COPYING*
%{_libdir}/libfdata.so.*

%files devel
%{_includedir}/libfdata.h
%{_includedir}/libfdata/
%{_libdir}/libfdata.so
%{_libdir}/pkgconfig/libfdata.pc
%{_mandir}/man3/libfdata.3*

%changelog
%autochangelog
