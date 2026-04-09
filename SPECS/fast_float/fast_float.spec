# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           fast_float
Version:        8.1.0
Release:        %autorelease
Summary:        Re-implementation of std::from_chars for parsing strings into numbers
License:        Apache-2.0 OR BSL-1.0 OR MIT
URL:            https://github.com/fastfloat/fast_float
#!RemoteAsset
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DFASTFLOAT_TEST:BOOL=ON
BuildOption(conf):  -DFASTFLOAT_SUPPLEMENTAL_TESTS:BOOL=OFF
BuildOption(conf):  -DSYSTEM_DOCTEST:BOOL=ON

BuildRequires:  cmake
BuildRequires:  cmake(doctest)

Provides:       %{name}-devel = %{version}-%{release}

%description
The fast_float library provides fast header-only implementations for the C++
from_chars functions for float and double types as well as integer types.

%files
%license LICENSE-APACHE LICENSE-BOOST LICENSE-MIT
%doc README.md
%{_includedir}/fast_float
%{_datadir}/cmake/

%changelog
%autochangelog
