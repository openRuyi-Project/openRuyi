# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libdeflate
Version:        1.25
Release:        %autorelease
Summary:        Fast DEFLATE, zlib, and gzip compression and decompression
License:        MIT
URL:            https://github.com/ebiggers/libdeflate
#!RemoteAsset:  sha256:fed5cd22f00f30cc4c2e5329f94e2b8a901df9fa45ee255cb70e2b0b42344477
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DLIBDEFLATE_BUILD_STATIC_LIB=OFF

BuildRequires:  cmake

%description
Libdeflate is a library for fast, whole-buffer DEFLATE-based compression and
decompression. It provides zlib and gzip format support through a simple C API.

%package        devel
Summary:        Development files for libdeflate
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the headers, pkg-config metadata, and CMake files needed
to develop applications using libdeflate.

%files
%license COPYING
%{_bindir}/libdeflate-gunzip
%{_bindir}/libdeflate-gzip
%{_libdir}/libdeflate.so.0*

%files devel
%{_includedir}/libdeflate.h
%{_libdir}/libdeflate.so
%{_libdir}/pkgconfig/libdeflate.pc
%{_libdir}/cmake/libdeflate/

%changelog
%autochangelog
