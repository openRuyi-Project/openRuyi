# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jingkun Zheng <zhengjingkun@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global commit 877328f188a3c7d1fa855871a278eb48d530c4c0
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           cpuinfo
Version:        0+git20260202.%{shortcommit}
Release:        %autorelease
Summary:        Library for obtaining CPU information
License:        BSD-2-Clause
URL:            https://github.com/pytorch/cpuinfo
#!RemoteAsset
Source:         https://github.com/pytorch/cpuinfo/archive/%{commit}/cpuinfo-%{commit}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DCPUINFO_LIBRARY_TYPE:STRING=shared
BuildOption(conf):  -DCPUINFO_BUILD_TOOLS:BOOL=ON
BuildOption(conf):  -DCPUINFO_BUILD_UNIT_TESTS:BOOL=OFF
BuildOption(conf):  -DCPUINFO_BUILD_MOCK_TESTS:BOOL=OFF
BuildOption(conf):  -DCPUINFO_BUILD_BENCHMARKS:BOOL=OFF

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
cpuinfo is a library to detect essential for performance optimization
information about host CPU.

%package        devel
Summary:        Development files for the cpuinfo library

%description    devel
This package contains the header files and development files for the
cpuinfo library.

%files
%license LICENSE
%doc README.md
%{_bindir}/cache-info
%{_bindir}/cpu-info
%{_bindir}/isa-info
%ifarch x86_64
%{_bindir}/cpuid-dump
%endif

%files devel
%{_includedir}/cpuinfo.h
%{_libdir}/libcpuinfo.so
%{_libdir}/pkgconfig/libcpuinfo.pc
%dir %{_datadir}/cpuinfo
%{_datadir}/cpuinfo/*.cmake

%changelog
%autochangelog
