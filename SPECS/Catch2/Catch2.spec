# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           Catch2
Version:        3.10.0
Release:        %autorelease
Summary:        A modern, C++-native test framework for TDD and BDD
License:        BSL-1.0
URL:            https://github.com/catchorg/Catch2
#!RemoteAsset
Source0:        https://github.com/catchorg/Catch2/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_SHARED_LIBS=ON
BuildOption(conf):  -DBUILD_TESTING=ON
BuildOption(conf):  -DCATCH_ENABLE_WERROR=OFF
BuildOption(conf):  -DCATCH_INSTALL_DOCS=OFF
BuildOption(conf):  -DCATCH_INSTALL_EXTRAS=ON

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  python3

%description
Catch2 is a modern, C++-native, multi-paradigm test framework.
This package contains the runtime shared libraries for Catch2.

%package        devel
Summary:        Development files for the Catch2 test framework
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains all necessary files to develop tests using Catch2,
including header files, CMake integration files, and pkg-config files.

%files
%license LICENSE.txt
# The main package owns only the versioned, runtime shared libraries.
%{_libdir}/libCatch2.so.*
%{_libdir}/libCatch2Main.so.*

%files devel
%doc README.md
%{_includedir}/catch2/
%{_libdir}/libCatch2.so
%{_libdir}/libCatch2Main.so
%{_libdir}/cmake/Catch2/
%{_datadir}/pkgconfig/catch2.pc
%{_datadir}/pkgconfig/catch2-with-main.pc
%{_datadir}/Catch2/

%changelog
%autochangelog
