# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           suitesparse
Version:        7.14.1
Release:        %autorelease
Summary:        Column ordering and configuration libraries from SuiteSparse
License:        BSD-3-Clause
URL:            https://github.com/DrTimothyAldenDavis/SuiteSparse
#!RemoteAsset:  sha256:81e560e1f74546df139edb765b3f5bc865866da23062312ffe8fd821063c8397
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/SuiteSparse-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(prep):  -n SuiteSparse-%{version}
BuildOption(conf):  -DSUITESPARSE_ENABLE_PROJECTS="suitesparse_config;colamd"
BuildOption(conf):  -DSUITESPARSE_REQUIRE_BLAS=OFF
BuildOption(conf):  -DBLA_VENDOR=Generic
BuildOption(conf):  -DBUILD_STATIC_LIBS=OFF
BuildOption(conf):  -DSUITESPARSE_DEMOS=ON

BuildRequires:  cmake

Provides:       %{name}-colamd = %{version}-%{release}
Provides:       %{name}-colamd%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-colamd < %{version}-%{release}

%description
SuiteSparse_config provides allocation, timing and version routines used
by sparse matrix libraries. COLAMD orders sparse matrix columns to reduce
fill during factorization, with C APIs for 32-bit and 64-bit indices.

%package        devel
Summary:        Headers and build metadata for SuiteSparse_config and COLAMD
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, CMake modules and pkg-config metadata for building applications
against COLAMD and SuiteSparse_config.

%install -a
install -Dpm 0644 SuiteSparse_config/README.txt %{buildroot}%{_docdir}/%{name}/README.SuiteSparse_config
install -Dpm 0644 COLAMD/README.txt %{buildroot}%{_docdir}/%{name}/README.COLAMD

%check -a
# Run upstream's COLAMD/SYMAMD demos, which report ordering failures for both index widths.
%{_vpath_builddir}/COLAMD/colamd_example
%{_vpath_builddir}/COLAMD/colamd_l_example

%files
%doc %{_docdir}/suitesparse/
%license LICENSE.txt
%{_libdir}/libsuitesparseconfig.so.*
%{_libdir}/libcolamd.so.*

%files devel
%{_includedir}/suitesparse/
%{_libdir}/libsuitesparseconfig.so
%{_libdir}/libcolamd.so
%{_libdir}/cmake/
%{_libdir}/pkgconfig/COLAMD.pc
%{_libdir}/pkgconfig/SuiteSparse_config.pc

%changelog
%autochangelog
