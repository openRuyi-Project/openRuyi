# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           sdbus-cpp
Version:        2.1.0
Release:        %autorelease
Summary:        A C++ D-Bus library for Linux
License:        LGPL-2.1-or-later WITH LGPL-3.0-linking-exception
URL:            https://github.com/Kistler-Group/sdbus-cpp
#!RemoteAsset
Source0:        https://github.com/Kistler-Group/sdbus-cpp/archive/refs/tags/v%{version}.tar.gz

BuildSystem:    cmake

BuildOption(conf): -DBUILD_TESTING:BOOL=OFF
BuildOption(conf): -DBUILD_EXAMPLES:BOOL=OFF
BuildOption(conf): -DBUILD_DOC:BOOL=OFF

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libxml-2.0)
# BuildRequires:  doxygen graphviz

%description
sdbus-cpp is a modern C++ D-Bus library for Linux, designed as a lightweight
wrapper around sd-bus, the D-Bus API of systemd.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}

%description devel
This package contains the header files, pkg-config file, and CMake configuration
files needed to develop applications that use the sdbus-cpp library.

%files
%license COPYING COPYING-LGPL-Exception
%doc README.md
%doc %{_docdir}/sdbus-c++
%{_libdir}/libsdbus-c++.so.*

%files devel
%{_includedir}/sdbus-c++/
%{_libdir}/libsdbus-c++.so
%{_libdir}/pkgconfig/sdbus-c++.pc
%dir %{_libdir}/cmake/sdbus-c++
%{_libdir}/cmake/sdbus-c++/*

%changelog
%{?autochangelog}
