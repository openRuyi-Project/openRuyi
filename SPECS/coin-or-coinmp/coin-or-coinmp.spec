# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Run the upstream C API tests.
%global _test_target test

Name:           coin-or-coinmp
Version:        1.8.4
Release:        %autorelease
Summary:        C interface to COIN-OR optimization solvers
License:        CPL-1.0
URL:            https://github.com/coin-or/CoinMP
#!RemoteAsset:  sha256:ec03a5110d9d79da950669e3400f3b81c4391747b14821d8997f9f8755873150
Source0:        %{url}/archive/refs/tags/releases/%{version}.tar.gz#/CoinMP-%{version}.tar.gz
BuildSystem:    autotools

# Apply DESTDIR once when installing examples and linker metadata.
Patch2000:      2000-stage-examples-and-linker-metadata-once.patch

BuildOption(prep):  -n CoinMP-releases-%{version}

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconf
BuildRequires:  pkgconfig(cbc)
BuildRequires:  pkgconfig(clp)
BuildRequires:  pkgconfig(osi-clp)

%description
CoinMP exposes a C API for creating linear and mixed-integer models and
solving them through the COIN-OR solver libraries.

%package        devel
Summary:        Development files for CoinMP
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, linker files and pkg-config metadata for using CoinMP.

# The release configure script predates the standard --docdir option.
%conf
CFLAGS="%{build_cflags}" CXXFLAGS="%{build_cxxflags}" LDFLAGS="%{build_ldflags}" \
    ./configure --build=%{_build} --host=%{_host} --prefix=%{_prefix} --libdir=%{_libdir} --disable-static

%files
%doc AUTHORS README
%license CoinMP/LICENSE
%{_libdir}/libCoinMP.so.*

%files devel
%{_includedir}/coin/
%{_libdir}/libCoinMP.so
%{_libdir}/pkgconfig/coinmp.pc
%{_datadir}/coin/doc/CoinMP/

%changelog
%autochangelog
