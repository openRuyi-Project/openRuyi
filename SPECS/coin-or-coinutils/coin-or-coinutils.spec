# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Run the upstream numerical and matrix tests.
%global _test_target test

Name:           coin-or-coinutils
Version:        2.11.13
Release:        %autorelease
Summary:        Utilities for COIN-OR optimization libraries
License:        EPL-2.0
URL:            https://github.com/coin-or/CoinUtils
#!RemoteAsset:  sha256:ddfea48e10209215748bc9f90a8c04abbb912b662c1aefaf280018d0a181ef79
Source0:        %{url}/archive/refs/tags/releases/%{version}.tar.gz#/CoinUtils-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(prep):  -n CoinUtils-releases-%{version}

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconf

%description
CoinUtils supplies matrices, factorization routines and file readers for
COIN-OR mathematical programming software.

%package        devel
Summary:        Development files for CoinUtils
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, linker files and pkg-config metadata for using CoinUtils.

# The release configure script predates the standard --docdir option.
%conf
CFLAGS="%{build_cflags}" CXXFLAGS="%{build_cxxflags}" LDFLAGS="%{build_ldflags}" \
    ./configure --build=%{_build} --host=%{_host} --prefix=%{_prefix} --libdir=%{_libdir} --disable-static

%files
%doc AUTHORS README.md
%license LICENSE
%{_libdir}/libCoinUtils.so.*

%files devel
%{_includedir}/coin/
%{_libdir}/libCoinUtils.so
%{_libdir}/pkgconfig/coinutils.pc
%{_datadir}/coin/doc/CoinUtils/

%changelog
%autochangelog
