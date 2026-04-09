# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global commit       560c60d342a76076f0557a3946924c6478470044
%global shortcommit  %(c=%{commit}; echo ${c:0:7})

Name:           pthreadpool
Version:        0+git20260202.%{shortcommit}
Release:        %autorelease
Summary:        Portable thread pool
License:        BSD-2-Clause
URL:            https://github.com/Maratyszcza/pthreadpool
#!RemoteAsset:  sha256:8d8ebab96df6aa12922643060e72c43bfdca9fd80cf5aacaf7391bc6850560a3
Source0:        https://github.com/Maratyszcza/pthreadpool/archive/%{commit}/pthreadpool-%{commit}.tar.gz
BuildSystem:    cmake

# use system instad of downlaod from net.
Patch0:         0001-fix-use-system-fxdiv.patch

BuildOption(conf):  -DPTHREADPOOL_USE_SYSTEM_LIBS=ON
BuildOption(conf):  -DPTHREADPOOL_BUILD_BENCHMARKS=OFF
BuildOption(conf):  -DPTHREADPOOL_BUILD_TESTS=ON

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  fxdiv-devel
BuildRequires:  pkgconfig(gtest)

%description
pthreadpool is a portable and efficient thread pool implementation.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for pthreadpool.

%files
%license LICENSE
%doc README.md
%{_libdir}/libpthreadpool.so.*

%files devel
%{_includedir}/pthreadpool.h
%{_libdir}/libpthreadpool.so

%changelog
%autochangelog
