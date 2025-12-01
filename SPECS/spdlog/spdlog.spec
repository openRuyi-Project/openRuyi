# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           spdlog
Version:        1.15.3
Release:        %autorelease
Summary:        Super fast C++ logging library
License:        MIT
URL:            https://github.com/gabime/spdlog
#!RemoteAsset
Source:         https://github.com/gabime/spdlog/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf): -DSPDLOG_BUILD_SHARED:BOOL=ON
BuildOption(conf): -DSPDLOG_BUILD_EXAMPLE:BOOL=OFF
BuildOption(conf): -DSPDLOG_INSTALL:BOOL=ON
BuildOption(conf): -DSPDLOG_FMT_EXTERNAL:BOOL=ON
BuildOption(conf): -DSPDLOG_BUILD_BENCH:BOOL=OFF
BuildOption(conf): -DSPDLOG_BUILD_TESTS:BOOL=OFF

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ninja
BuildRequires:  fmt-devel >= 10.0.0

%description
A header-only and compiled C++ logging library, designed to be as fast as possible.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}
Requires:       libstdc++-devel
Requires:       fmt-devel

%description    devel
This package contains C++ header files and development libraries for spdlog.

%files
%license LICENSE
%doc README.md
%{_libdir}/libspdlog.so*

%files devel
%doc example
%{_includedir}/spdlog
%{_libdir}/libspdlog.so
%{_libdir}/cmake/spdlog
%{_libdir}/pkgconfig/spdlog.pc

%changelog
%{?autochangelog}
