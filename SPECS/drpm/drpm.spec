# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           drpm
Version:        0.5.2
Release:        %autorelease
Summary:        Delta RPM library
License:        LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-BSD
URL:            https://github.com/rpm-software-management/drpm
#!RemoteAsset
Source:         https://github.com/rpm-software-management/drpm/releases/download/%{version}/drpm-%{version}.tar.bz2

BuildSystem:    cmake

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  bzip2-devel
BuildRequires:  cmocka-devel
BuildRequires:  lzlib-devel
BuildRequires:  openssl-devel
BuildRequires:  popt-devel
BuildRequires:  rpm-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(libzstd)

BuildRequires:  pkgconfig

BuildOption(conf): -DCMAKE_POLICY_VERSION_MINIMUM:STRING=3.5
%description
This package provides a library for making, reading and
applying deltarpms, compatible with the original deltarpm packages.

%package devel
Summary:        Header files for the drpm
License:        LGPL-2.1-or-later
Requires:       %{name} = %{version}

%description devel
This subpackage contains libraries and header files for developing
applications that want to make use of drpm.

%files
%license COPYING LICENSE.BSD
%{_libdir}/libdrpm.so.*

%files devel
%{_libdir}/libdrpm.so
%{_includedir}/drpm.h
%{_libdir}/pkgconfig/drpm.pc
%changelog
%{?autochangelog}
