# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# the name gsl is occupied
Name:           guidelines-support-library
Version:        4.2.1
Release:        %autorelease
Summary:        Guidelines Support Library
License:        MIT
URL:            https://github.com/microsoft/GSL
#!RemoteAsset
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    cmake

# use C++17 or build will fail
Patch0:         0001-use-c++17.patch

BuildOption(conf):  -GNinja
BuildOption(conf):  -DGSL_INSTALL:BOOL=ON
BuildOption(conf):  -DGSL_TEST:BOOL=ON

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  pkgconfig(gtest)
BuildRequires:  ninja

%description
The Guidelines Support Library (GSL) contains functions and types that are
suggested for use by the C++ Core Guidelines maintained by the Standard C++
Foundation. This repo contains Microsoft's implementation of GSL.

The entire implementation is provided inline in the headers under the gsl
directory. The implementation generally assumes a platform that implements
C++14 support.

While some types have been broken out into their own headers (e.g. gsl/span),
it is simplest to just include gsl/gsl and gain access to the entire library.

%files
%doc README.md CONTRIBUTING.md
%license LICENSE ThirdPartyNotices.txt
%{_datadir}/cmake/Microsoft.GSL/
%{_includedir}/gsl/

%changelog
%autochangelog
