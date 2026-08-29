# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# error: lto-wrapper failed,so disable it.
%define _lto_cflags %{nil}

Name:           highway
Version:        1.4.0
Release:        %autorelease
Summary:        Efficient and performance-portable SIMD
License:        Apache-2.0
URL:            https://github.com/google/highway
#!RemoteAsset:  sha256:e72241ac9524bb653ae52ced768b508045d4438726a303f10181a38f764a453c
Source0:        https://github.com/google/highway/archive/%{version}/highway-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DHWY_CMAKE_RVV=OFF
BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
Highway is a C++ library for SIMD (Single Instruction, Multiple Data), i.e.
applying the same operation to 'lanes'.

%package        devel
Summary:        Development files for Highway
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for Highway.

%files
%license LICENSE
%{_libdir}/libhwy.so.1*
%{_libdir}/libhwy_contrib.so.1*
%{_libdir}/libhwy_test.so.1*

%files devel
%license LICENSE
%{_includedir}/hwy/
%{_libdir}/cmake/hwy/
%{_libdir}/libhwy.so
%{_libdir}/libhwy_contrib.so
%{_libdir}/libhwy_test.so
%{_libdir}/pkgconfig/libhwy.pc
%{_libdir}/pkgconfig/libhwy-contrib.pc
%{_libdir}/pkgconfig/libhwy-test.pc

%changelog
%autochangelog
