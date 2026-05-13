# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jingkun Zheng <zhengjingkun@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global _test_target test

Name:           openblas
Version:        0.3.31
Release:        %autorelease
Summary:        An optimized BLAS library based on GotoBLAS2 1.13 BSD version
License:        BSD-3-Clause
URL:            http://www.openmathlib.org/OpenBLAS/
VCS:            git:https://github.com/OpenMathLib/OpenBLAS
#!RemoteAsset:  sha256:6dd2a63ac9d32643b7cc636eab57bf4e57d0ed1fff926dfbc5d3d97f2d2be3a6
Source0:        https://github.com/OpenMathLib/OpenBLAS/releases/download/v%{version}/OpenBLAS-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(build):  BINARY=64
BuildOption(build):  INTERFACE64=0
BuildOption(build):  USE_THREAD=1
BuildOption(build):  USE_OPENMP=0
BuildOption(build):  NO_STATIC=1
BuildOption(build):  DYNAMIC_ARCH=1
BuildOption(build):  NO_TEST=1
%ifarch riscv64
BuildOption(build):  TARGET=RISCV64_GENERIC
%endif
BuildOption(install):  PREFIX=%{_prefix}
BuildOption(install):  OPENBLAS_LIBRARY_DIR=%{_libdir}
BuildOption(install):  NO_STATIC=1

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  perl-devel

%description
OpenBLAS is an optimized BLAS library based on GotoBLAS2, providing a high-performance
implementation of Basic Linear Algebra Subprograms.

%package        devel
Summary:        Development files for OpenBLAS
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the development headers and libraries for OpenBLAS.

# No configure
%conf

# Parallel ILP64 build for consumers that BR pkgconfig(openblas64).
%prep -a
cp -al . ../ilp64

%build -a
%make_build -C ../ilp64 \
%ifarch riscv64
  TARGET=RISCV64_GENERIC \
%endif
  BINARY=64 INTERFACE64=1 LIBNAMESUFFIX=64 \
  USE_THREAD=1 USE_OPENMP=0 NO_STATIC=1 DYNAMIC_ARCH=1 NO_TEST=1

%install -a
%make_install -C ../ilp64 \
  PREFIX=%{_prefix} \
  OPENBLAS_LIBRARY_DIR=%{_libdir} \
  OPENBLAS_INCLUDE_DIR=%{_includedir}/openblas64 \
  OPENBLAS_CMAKE_DIR=%{_libdir}/cmake/openblas64 \
  INTERFACE64=1 LIBNAMESUFFIX=64 NO_STATIC=1

%files
%license LICENSE
%doc Changelog.txt GotoBLAS_01Readme.txt
%{_libdir}/libopenblas*.so.*

%files devel
%{_includedir}/*
%{_libdir}/libopenblas*.so
%{_libdir}/pkgconfig/openblas.pc
%{_libdir}/pkgconfig/openblas64.pc
%{_libdir}/cmake/openblas/
%{_libdir}/cmake/openblas64/

%changelog
%autochangelog
