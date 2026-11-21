# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Run the upstream cut-generator tests.
%global _test_target test

Name:           coin-or-cgl
Version:        0.60.10
Release:        %autorelease
Summary:        Cut generators for COIN-OR integer programming solvers
License:        EPL-2.0
URL:            https://github.com/coin-or/Cgl
#!RemoteAsset:  sha256:41b7ac9402db883d9c487eb7101e59eb513cefd726e6e7a669dc94664d9385e6
Source0:        %{url}/archive/refs/tags/releases/%{version}.tar.gz#/Cgl-%{version}.tar.gz
# Upstream sample matrices for the solver and interface unit tests.
#!RemoteAsset:  sha256:4faae8f1ad54f342a49db0d7cd9cf8ab763349da2019a92d54d87b28ac1a7c21
Source1:        https://github.com/coin-or-tools/Data-Sample/archive/a75e56df8b3f44b09fcf7102546a3ca3cbf53a4f.tar.gz#/Data-Sample-a75e56df8b3f44b09fcf7102546a3ca3cbf53a4f.tar.gz
BuildSystem:    autotools

BuildOption(prep):  -n Cgl-releases-%{version}

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconf
BuildRequires:  pkgconfig(coinutils)
BuildRequires:  pkgconfig(osi)
BuildRequires:  pkgconfig(clp)
BuildRequires:  pkgconfig(osi-clp)

%description
Cgl generates cutting planes used by COIN-OR solvers to tighten linear
relaxations of mixed-integer problems.

%package        devel
Summary:        Development files for Cgl
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, linker files and pkg-config metadata for using Cgl.

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
%{_libdir}/libCgl.so.*

%files devel
%{_includedir}/coin/
%{_libdir}/libCgl.so
%{_libdir}/pkgconfig/cgl.pc
%{_datadir}/coin/doc/Cgl/

%changelog
%autochangelog
