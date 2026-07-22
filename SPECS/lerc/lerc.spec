# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           lerc
Version:        4.1.1
Release:        %autorelease
Summary:        Limited Error Raster Compression library
License:        Apache-2.0
URL:            https://github.com/Esri/lerc
#!RemoteAsset:  sha256:fe2860e10635166cd9f2144e429ec6b870d471e9957f5812ba2da0973770b022
Source0:        %{url}/archive/refs/tags/v%{version}/%{version}.tar.gz
BuildSystem:    cmake

BuildRequires:  cmake

%description
LERC is an image and raster compression library that supports controlled
lossy and lossless compression for all common pixel types.

%package        devel
Summary:        Development files for LERC
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers and pkg-config metadata for developing applications with LERC.

%files
%license LICENSE
%{_libdir}/libLerc.so.*

%files devel
%{_includedir}/Lerc_c_api.h
%{_includedir}/Lerc_types.h
%{_libdir}/libLerc.so
%{_libdir}/pkgconfig/Lerc.pc

%changelog
%autochangelog
