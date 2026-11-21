# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Run the upstream linear solver and OsiClp interface tests.
%global _test_target test

Name:           coin-or-clp
Version:        1.17.11
Release:        %autorelease
Summary:        COIN-OR linear programming solver
License:        EPL-2.0
URL:            https://github.com/coin-or/Clp
#!RemoteAsset:  sha256:2c078e174dc1a7a308e091b6256fb34b4017897fc140ea707ba207b2913ea46d
Source0:        %{url}/archive/refs/tags/releases/%{version}.tar.gz#/Clp-%{version}.tar.gz
# Upstream sample matrices for the solver and interface unit tests.
#!RemoteAsset:  sha256:4faae8f1ad54f342a49db0d7cd9cf8ab763349da2019a92d54d87b28ac1a7c21
Source1:        https://github.com/coin-or-tools/Data-Sample/archive/a75e56df8b3f44b09fcf7102546a3ca3cbf53a4f.tar.gz#/Data-Sample-a75e56df8b3f44b09fcf7102546a3ca3cbf53a4f.tar.gz
BuildSystem:    autotools

BuildOption(prep):  -n Clp-releases-%{version}

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconf
BuildRequires:  pkgconfig(coinutils)
BuildRequires:  pkgconfig(osi)
BuildRequires:  pkgconfig(osi-unittests)

%description
Clp implements simplex and barrier methods for continuous linear
programs. It includes a command-line solver and an Osi adapter.

%package        devel
Summary:        Development files for Clp
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, linker files and pkg-config metadata for using Clp.

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
%doc AUTHORS README.md
%license LICENSE
%{_bindir}/clp
%{_libdir}/libClp*.so.*
%{_libdir}/libOsiClp.so.*

%files devel
%{_includedir}/coin/
%{_libdir}/libClp*.so
%{_libdir}/libOsiClp.so
%{_libdir}/pkgconfig/clp.pc
%{_libdir}/pkgconfig/osi-clp.pc
%{_datadir}/coin/doc/Clp/

%changelog
%autochangelog
