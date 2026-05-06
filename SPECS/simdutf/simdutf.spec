# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           simdutf
Version:        9.0.0
Release:        %autorelease
Summary:        High-speed Unicode validation and transcoding library
License:        Apache-2.0 AND BSD-3-Clause
URL:            https://github.com/simdutf/simdutf
#!RemoteAsset:  sha256:fd2ce975f29809a975a8da8843cfb3a7265af3f71be548f199d23cf65e101764
Source0:        https://github.com/simdutf/simdutf/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DSIMDUTF_BENCHMARKS:BOOL=OFF
BuildOption(conf):  -DSIMDUTF_TOOLS:BOOL=OFF

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
A C++ library for validating and transcoding Unicode (UTF-8, UTF-16, UTF-32)
at high speeds using SIMD instructions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files, pkg-config, and CMake files needed
to develop applications that use the simdutf library.

%files
%license LICENSE-APACHE
%doc AUTHORS README.md
%{_libdir}/libsimdutf.so.*

%files devel
%{_includedir}/simdutf.h
%{_includedir}/simdutf_c.h
%{_includedir}/simdutf
%dir %{_libdir}/cmake
%{_libdir}/cmake/simdutf
%{_libdir}/libsimdutf.so
%{_libdir}/pkgconfig/simdutf.pc

%changelog
%autochangelog
