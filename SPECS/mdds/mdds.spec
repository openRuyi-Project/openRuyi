# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           mdds
Version:        3.2.1
Release:        %autorelease
Summary:        Header-only C++ data structures for multidimensional data
License:        MIT
URL:            https://gitlab.com/mdds/mdds
#!RemoteAsset:  sha256:673f5bb94612dbba581fc92b99b5e5dd1a53e29496a5dbc936432f6b0687c112
Source0:        https://gitlab.com/api/v4/projects/mdds%2Fmdds/packages/generic/source/%{version}/%{name}-%{version}.tar.xz
BuildArch:      noarch
BuildSystem:    autotools

BuildOption(conf):  CXXFLAGS="%{optflags} -std=c++17"

BuildRequires:  boost-devel
BuildRequires:  dejagnu
BuildRequires:  gcc-c++
BuildRequires:  gdb
BuildRequires:  make
BuildRequires:  pkgconfig(tbb)

%description
mdds provides C++ templates for segment trees, mixed-type vectors and
matrices, spatial indexes, tries and other data structures.

%package        devel
Summary:        C++ template headers and build metadata for %{name}
Requires:       boost-devel

%description    devel
C++ headers and pkg-config metadata for applications using mdds.

%files devel
%doc %{_docdir}/mdds/
%license LICENSE
%{_datadir}/pkgconfig/mdds-3.0.pc
%{_includedir}/mdds-3.0/

%changelog
%autochangelog
