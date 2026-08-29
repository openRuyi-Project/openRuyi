# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           benchmark
Version:        1.9.5
Release:        %autorelease
Summary:        Microbenchmark support library
License:        Apache-2.0
URL:            https://github.com/google/benchmark
#!RemoteAsset:  sha256:9631341c82bac4a288bef951f8b26b41f69021794184ece969f8473977eaa340
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBENCHMARK_ENABLE_WERROR=OFF
BuildOption(conf):  -DBENCHMARK_USE_BUNDLED_GTEST=OFF

BuildRequires:  cmake
BuildRequires:  pkgconfig(gmock)
BuildRequires:  pkgconfig(gtest)

%description
Benchmark is a library for measuring and reporting the performance of C++
code.

%package        devel
Summary:        Development files for benchmark
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Header files and build metadata for developing applications with benchmark.

%files
%doc %{_docdir}/%{name}/
%license LICENSE
%{_libdir}/libbenchmark.so.*
%{_libdir}/libbenchmark_main.so.*
%{_datadir}/googlebenchmark/

%files devel
%{_includedir}/benchmark/
%{_libdir}/cmake/benchmark/
%{_libdir}/libbenchmark.so
%{_libdir}/libbenchmark_main.so
%{_libdir}/pkgconfig/benchmark.pc
%{_libdir}/pkgconfig/benchmark_main.pc

%changelog
%autochangelog
