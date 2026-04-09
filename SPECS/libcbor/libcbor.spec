# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libcbor
Version:        0.11.0
Release:        %autorelease
Summary:        Library for parsing Concise Binary Object Representation (CBOR)
License:        MIT
URL:            https://github.com/PJK/libcbor
#!RemoteAsset
Source0:        https://github.com/PJK/libcbor/archive/v%{version}.tar.gz
BuildSystem:    cmake

# The libcbor declaration depends on an outdated version of cmake.
BuildOption(conf):  -DCMAKE_POLICY_VERSION_MINIMUM=3.5

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(cmocka)

%description
libcbor is a C99 library for parsing and generating CBOR (RFC 7049),
a general-purpose schema-less binary data format.

It supports flexible memory management, UTF-8, streams & incremental
processing, and has a layered architecture.

%package        devel
Summary:        Development files for libcbor
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
libcbor is a C library for parsing and generating CBOR.
The libcbor-devel contains libraries and header files for libcbor.

%files
%license LICENSE.md
%{_libdir}/*.so.*

%files devel
%{_includedir}/cbor.h
%dir %{_includedir}/cbor
%{_includedir}/cbor/*.h
%dir %{_includedir}/cbor/internal
%{_includedir}/cbor/internal/*.h
%{_libdir}/libcbor.so
%{_libdir}/pkgconfig/libcbor.pc
%{_libdir}/cmake

%changelog
%autochangelog
