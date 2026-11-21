# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Run the upstream solver interface tests.
%global _test_target test

Name:           coin-or-osi
Version:        0.108.12
Release:        %autorelease
Summary:        COIN-OR solver interface
License:        EPL-2.0
URL:            https://github.com/coin-or/Osi
#!RemoteAsset:  sha256:1d80d0b4275f2e1ceefc6dda66b8616e3a8c8b07a926ef4456db4a0d55249333
Source0:        %{url}/archive/refs/tags/releases/%{version}.tar.gz#/Osi-%{version}.tar.gz
# Upstream sample matrices for the solver and interface unit tests.
#!RemoteAsset:  sha256:4faae8f1ad54f342a49db0d7cd9cf8ab763349da2019a92d54d87b28ac1a7c21
Source1:        https://github.com/coin-or-tools/Data-Sample/archive/a75e56df8b3f44b09fcf7102546a3ca3cbf53a4f.tar.gz#/Data-Sample-a75e56df8b3f44b09fcf7102546a3ca3cbf53a4f.tar.gz
BuildSystem:    autotools

BuildOption(prep):  -n Osi-releases-%{version}

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconf
BuildRequires:  pkgconfig(coinutils)

%description
Osi defines a common C++ interface to linear programming solvers and
provides shared tests for validating solver implementations.

%package        devel
Summary:        Development files for Osi
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, linker files and pkg-config metadata for using Osi.

%prep -a
# Keep the upstream sample directory layout for the offline test suite.
mkdir -p Data/Sample
tar -xf %{SOURCE1} -C Data/Sample --strip-components=1

# The release configure script predates the standard --docdir option.
%conf
CFLAGS="%{build_cflags}" CXXFLAGS="%{build_cxxflags}" LDFLAGS="%{build_ldflags}" \
    ./configure --build=%{_build} --host=%{_host} --prefix=%{_prefix} --libdir=%{_libdir} --disable-static \
    --with-sample-datadir="$PWD/Data/Sample"

%files
%doc README.md
%license LICENSE
%{_libdir}/libOsi.so.*
%{_libdir}/libOsiCommonTests.so.*

%files devel
%{_includedir}/coin/
%{_libdir}/libOsi.so
%{_libdir}/libOsiCommonTests.so
%{_libdir}/pkgconfig/osi.pc
%{_libdir}/pkgconfig/osi-unittests.pc
%{_datadir}/coin/doc/Osi/

%changelog
%autochangelog
