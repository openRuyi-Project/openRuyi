# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global date 2025-11-05

Name:           re2
Version:        2025.11.05
Release:        %autorelease
Summary:        A fast, safe, and thread-friendly regular expression engine
License:        BSD-3-Clause
URL:            https://github.com/google/re2
VCS:            git:https://github.com/google/re2
#!RemoteAsset:  sha256:87f6029d2f6de8aa023654240a03ada90e876ce9a4676e258dd01ea4c26ffd67
Source0:        https://github.com/google/re2/releases/download/%{date}/re2-%{date}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DRE2_TEST:BOOL=ON
BuildOption(conf):  -DRE2_BENCHMARK:BOOL=OFF
BuildOption(conf):  -DRE2_USE_ICU:BOOL=ON

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja
BuildRequires:  abseil-cpp-devel
BuildRequires:  icu4c-devel
BuildRequires:  pkgconfig(gtest)

%description
RE2 is a fast, safe, thread-friendly alternative to backtracking regular
expression engines like those used in PCRE, Perl, and Python. It is a C++ library.

%package        devel
Summary:        Development files for the re2 library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the C++ header files, libraries, and build system files
needed to develop applications that use the re2 library.

%files
%doc README.md
%license LICENSE
%{_libdir}/libre2.so.*

%files devel
%{_includedir}/re2
%{_libdir}/libre2.so
%{_libdir}/cmake/re2
%{_libdir}/pkgconfig/re2.pc

%changelog
%autochangelog
