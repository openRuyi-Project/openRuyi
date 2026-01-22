# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           fmt
Version:        12.0.0
Release:        %autorelease
Summary:        Small, safe and fast formatting library for C++
License:        MIT
URL:            https://github.com/fmtlib/fmt
#!RemoteAsset
Source0:        https://github.com/fmtlib/fmt/archive/%{version}/fmt-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf): -DCMAKE_BUILD_TYPE=RelWithDebInfo
BuildOption(conf): -DCMAKE_POSITION_INDEPENDENT_CODE:BOOL=ON
BuildOption(conf): -DFMT_CMAKE_DIR:STRING=%{_libdir}/cmake/%{name}
BuildOption(conf): -DFMT_LIB_DIR:STRING=%{_libdir}

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ninja

%description
fmt is an open-source formatting library for C++. It can be used as a
safe alternative to printf or as a fast alternative to IOStreams.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files, libraries, and CMake/pkg-config files
for developing applications that use the fmt library.

%files
%{_libdir}/libfmt.so*

%files devel
%{_includedir}/fmt/
%{_libdir}/libfmt.so
%{_libdir}/cmake/fmt/
%{_libdir}/pkgconfig/fmt.pc

%changelog
%{?autochangelog}
