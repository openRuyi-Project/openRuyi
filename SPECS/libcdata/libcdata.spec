# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libcdata
Version:        20240414
Release:        %autorelease
Summary:        Library for cross-platform C generic data functions
License:        LGPL-3.0-or-later
URL:            https://github.com/libyal/libcdata
#!RemoteAsset
Source0:        %{url}/releases/download/%{version}/%{name}-alpha-%{version}.tar.gz
#!RemoteAsset
Source1:        %{url}/releases/download/%{version}/%{name}-alpha-%{version}.tar.gz.asc
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  gcc
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcerror) >= 20240413
BuildRequires:  pkgconfig(libcthreads) >= 20240413

%description
libcdata is a for cross-platform C generic data functions.

This package is part of the libyal library collection and is used by other libraries in the collection

%package        devel
Summary:        Development files for libcdata, a C generic data library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
libcdata is a for cross-platform C generic data functions.

This subpackage contains libraries and header files for developing
applications that want to make use of libcdata.

%files
%license COPYING*
%{_libdir}/libcdata.so.1*

%files devel
%{_includedir}/libcdata*
%{_libdir}/libcdata.so
%{_libdir}/pkgconfig/libcdata.pc
%{_mandir}/man3/libcdata.3*

%changelog
%autochangelog
