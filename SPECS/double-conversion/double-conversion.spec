# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           double-conversion
Version:        3.3.1
Release:        %autorelease
Summary:        Library for binary-decimal conversions of IEEE doubles
License:        BSD-3-Clause
URL:            https://github.com/google/double-conversion
#!RemoteAsset
Source:         https://github.com/google/double-conversion/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING:BOOL=ON
BuildOption(conf):  -DCMAKE_POLICY_VERSION_MINIMUM=3.5

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake

%description
Provides binary-decimal and decimal-binary routines for IEEE doubles.
The library consists of efficient conversion routines that have been
extracted from the V8 JavaScript engine.

%package        devel
Summary:        Development files for the %{name} library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Contains header files and CMake configuration for developing applications
that use the double-conversion library.

%files
%license LICENSE
%doc README.md AUTHORS Changelog
%{_libdir}/libdouble-conversion.so.3
%{_libdir}/libdouble-conversion.so.3.*

%files devel
%{_libdir}/libdouble-conversion.so
%dir %{_libdir}/cmake/double-conversion
%{_libdir}/cmake/double-conversion/*
%{_includedir}/double-conversion/

%changelog
%autochangelog
