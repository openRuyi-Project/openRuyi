# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Run the upstream mixed-integer solver and OsiCbc interface tests.
%global _test_target test

Name:           coin-or-cbc
Version:        2.10.13
Release:        %autorelease
Summary:        COIN-OR mixed-integer linear programming solver
License:        EPL-2.0
URL:            https://github.com/coin-or/Cbc
#!RemoteAsset:  sha256:62fde44dcf6f3d05c5cd291d7435cdd1b7e8acd3c78ec481dd39fe49cbc40399
Source0:        %{url}/archive/refs/tags/releases/%{version}.tar.gz#/Cbc-%{version}.tar.gz
# Upstream sample matrices for the solver and interface unit tests.
#!RemoteAsset:  sha256:4faae8f1ad54f342a49db0d7cd9cf8ab763349da2019a92d54d87b28ac1a7c21
Source1:        https://github.com/coin-or-tools/Data-Sample/archive/a75e56df8b3f44b09fcf7102546a3ca3cbf53a4f.tar.gz#/Data-Sample-a75e56df8b3f44b09fcf7102546a3ca3cbf53a4f.tar.gz
BuildSystem:    autotools

BuildOption(prep):  -n Cbc-releases-%{version}

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconf
BuildRequires:  pkgconfig(coinutils)
BuildRequires:  pkgconfig(osi)
BuildRequires:  pkgconfig(cgl)
BuildRequires:  pkgconfig(clp)
BuildRequires:  pkgconfig(osi-clp)
BuildRequires:  pkgconfig(osi-unittests)

%description
Cbc solves mixed-integer programs using branch and cut. It includes a
command-line solver and an Osi adapter.

%package        devel
Summary:        Development files for Cbc
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, linker files and pkg-config metadata for using Cbc.

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
%{_bindir}/cbc*
%{_libdir}/libCbc*.so.*
%{_libdir}/libOsiCbc.so.*

%files devel
%{_includedir}/coin/
%{_libdir}/libCbc*.so
%{_libdir}/libOsiCbc.so
%{_libdir}/pkgconfig/cbc.pc
%{_libdir}/pkgconfig/osi-cbc.pc
%{_datadir}/coin/doc/Cbc/

%changelog
%autochangelog
