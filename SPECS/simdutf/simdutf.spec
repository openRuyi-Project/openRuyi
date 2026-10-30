# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           simdutf
Version:        9.3.3
Release:        %autorelease
Summary:        High-speed Unicode validation and transcoding library
License:        Apache-2.0 OR MIT
URL:            https://github.com/simdutf/simdutf
#!RemoteAsset:  sha256:441e374e8629bd8469f6d5cde9f0fa17ef3ad158aeb077791606d8aa73b565ef
Source0:        https://github.com/simdutf/simdutf/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DSIMDUTF_CXX_STANDARD=20
BuildOption(conf):  -DSIMDUTF_ATOMIC_BASE64_TESTS:BOOL=ON
BuildOption(conf):  -DSIMDUTF_BENCHMARKS:BOOL=OFF
BuildOption(conf):  -DSIMDUTF_TOOLS:BOOL=ON
BuildOption(conf):  -DSIMDUTF_TOOL_TESTS:BOOL=ON

BuildRequires:  cmake >= 3.18
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(python3)

%description
A C++ library for validating and transcoding Unicode (UTF-8, UTF-16, UTF-32)
at high speeds using SIMD instructions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files, pkg-config, and CMake files needed
to develop applications that use the simdutf library.

%package        tools
Summary:        Unicode and Base64 conversion tools

%description    tools
sutf converts text between character encodings. fastbase64 encodes and
decodes Base64 data. fastbase64.coreutils provides the GNU-style interface.

%files
%doc AUTHORS README.md
%license LICENSE-APACHE LICENSE-MIT
%{_libdir}/libsimdutf.so.*

%files devel
%{_includedir}/simdutf.h
%{_includedir}/simdutf_c.h
%{_includedir}/simdutf
%{_libdir}/cmake/simdutf
%{_libdir}/libsimdutf.so
%{_libdir}/pkgconfig/simdutf.pc

%files tools
%license LICENSE-APACHE LICENSE-MIT
%{_bindir}/sutf
%{_bindir}/fastbase64
%{_bindir}/fastbase64.coreutils
%{_mandir}/man1/sutf.1*
%{_mandir}/man1/fastbase64.1*
%{_mandir}/man1/fastbase64.coreutils.1*

%changelog
%autochangelog
