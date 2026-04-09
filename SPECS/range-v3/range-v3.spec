# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           range-v3
Summary:        Experimental range library for C++11/14/17
Version:        0.12.0
Release:        %autorelease
License:        BSL-1.0
URL:            https://github.com/ericniebler/range-v3
#!RemoteAsset
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -G Ninja
BuildOption(conf):  -DRANGES_ENABLE_WERROR:BOOL=OFF
BuildOption(conf):  -DRANGES_MODULES:BOOL=OFF
BuildOption(conf):  -DRANGES_NATIVE:BOOL=OFF
BuildOption(conf):  -DRANGE_V3_DOCS:BOOL=OFF
BuildOption(conf):  -DRANGE_V3_EXAMPLES:BOOL=OFF
BuildOption(conf):  -DRANGE_V3_PERF:BOOL=OFF
BuildOption(conf):  -DRANGE_V3_TESTS:BOOL=OFF

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ninja

%description
Header-only %{summary}.

%package        devel
Summary:        Development files for %{name}

%description    devel
%{summary}.

%files devel
%doc README.md CREDITS.md TODO.md
%license LICENSE.txt
%exclude %{_includedir}/module.modulemap
%{_includedir}/{meta,range,concepts,std}
%{_libdir}/cmake/range-v3

%changelog
%autochangelog
