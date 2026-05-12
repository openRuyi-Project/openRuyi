# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           snappy
Version:        1.2.2
Release:        %autorelease
Summary:        A fast compressor/decompressor
License:        BSD-3-Clause
URL:            https://github.com/google/snappy
#!RemoteAsset:  sha256:90f74bc1fbf78a6c56b3c4a082a05103b3a56bb17bca1a27e052ea11723292dc
Source0:        https://github.com/google/snappy/archive/%{version}/snappy-%{version}.tar.gz
BuildSystem:    cmake

# https://sources.debian.org/patches/snappy/1.2.2-1/add_option_to_enable_rtti.patch/
Patch2000:      2000-honor-SNAPPY_ENABLE_RTTI.patch

BuildOption(conf):  -DBUILD_SHARED_LIBS:BOOL=ON
BuildOption(conf):  -DSNAPPY_ENABLE_RTTI:BOOL=ON
BuildOption(conf):  -DCMAKE_CXX_STANDARD:STRING=17
BuildOption(conf):  -DSNAPPY_BUILD_TESTS:BOOL=OFF
BuildOption(conf):  -DSNAPPY_BUILD_BENCHMARKS:BOOL=OFF

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  cmake

%description
Snappy is a compression/decomp-ression library. It does not aim for maximum
compression, or compatibility with any other compression library; instead,
it aims for very high speeds and reasonable compression.

%package        devel
Summary:        Development files for snappy
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files, libraries, and documentation for
developing applications that use the Snappy library.

%files
%license COPYING
%doc AUTHORS
%{_libdir}/libsnappy.so.*

%files devel
%doc NEWS README.md
%doc format_*.txt framing_*.txt
%{_includedir}/snappy*.h
%{_libdir}/libsnappy.so
%dir %{_libdir}/cmake
%dir %{_libdir}/cmake/Snappy
%{_libdir}/cmake/Snappy/*

%changelog
%autochangelog
