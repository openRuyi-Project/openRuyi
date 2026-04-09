# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           drpm
Version:        0.5.2
Release:        %autorelease
Summary:        Delta RPM library
License:        LGPL-2.1-or-later BSD-3-Clause
URL:            https://github.com/rpm-software-management/drpm
#!RemoteAsset
Source:         https://github.com/rpm-software-management/drpm/releases/download/%{version}/drpm-%{version}.tar.bz2
BuildSystem:    cmake

BuildOption(conf):  -DCMAKE_POLICY_VERSION_MINIMUM:STRING=3.5

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(cmocka)
BuildRequires:  lzlib-devel
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(popt)
BuildRequires:  pkgconfig(rpm)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig

%description
This package provides a library for making, reading and
applying deltarpms, compatible with the original deltarpm packages.

%package        devel
Summary:        Header files for the drpm
License:        LGPL-2.1-or-later
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
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
%autochangelog
