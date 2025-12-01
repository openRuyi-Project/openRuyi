# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jingkun Zheng <zhengjingkun@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global _test_target test
Name:           openblas
Version:        0.3.30
Release:        %autorelease
Summary:        An optimized BLAS library based on GotoBLAS2 1.13 BSD version
License:        BSD-3-Clause
URL:            http://www.openmathlib.org/OpenBLAS/
#!RemoteAsset
Source0:        https://github.com/OpenMathLib/OpenBLAS/releases/download/v%{version}/OpenBLAS-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(build): BINARY=64
BuildOption(build): INTERFACE64=1
BuildOption(build): USE_THREAD=1
BuildOption(build): USE_OPENMP=0
BuildOption(build): NO_STATIC=1
BuildOption(build): DYNAMIC_ARCH=1
BuildOption(build): NO_TEST=1
BuildOption(install): PREFIX=%{_prefix}
BuildOption(install): OPENBLAS_LIBRARY_DIR=%{_libdir}
BuildOption(install): NO_STATIC=1
BuildRequires:  gcc perl-devel gcc-c++

%ifarch riscv64
BuildOption(build): TARGET=RISCV64_GENERIC
%endif

%description
OpenBLAS is an optimized BLAS library based on GotoBLAS2, providing a high-performance
implementation of Basic Linear Algebra Subprograms.

%package devel
Summary:        Development files for OpenBLAS
Requires:       %{name} = %{version}

%description devel
This package contains the development headers and libraries for OpenBLAS.

# No configure
%conf

%files
%license LICENSE
%doc Changelog.txt GotoBLAS_01Readme.txt
%{_libdir}/libopenblas*.so.*

%files devel
%{_includedir}/*
%{_libdir}/libopenblas*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/openblas/

%changelog
%{?autochangelog}
