# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           plog
Version:        1.1.11
Release:        %autorelease
Summary:        Development files for plog, a C++ logging library
License:        MIT
URL:            https://github.com/SergiusTheBest/plog
#!RemoteAsset
Source:         https://github.com/SergiusTheBest/plog/archive/refs/tags/%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DPLOG_BUILD_TESTS:BOOL=OFF
BuildOption(conf):  -DPLOG_BUILD_SAMPLES:BOOL=OFF

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
Plog is a C++ logging library that is designed to be as simple,
small and flexible as possible. It is created as an alternative
to existing large libraries and provides some unique features
as CSV log format and wide string support.

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files devel
%license LICENSE
%doc %{_docdir}/%{name}
%doc README.md doc
%{_includedir}/plog/
%{_libdir}/cmake/plog/

%changelog
%autochangelog
