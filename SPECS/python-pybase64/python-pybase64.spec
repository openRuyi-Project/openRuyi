# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pybase64

Name:           python-%{srcname}
Version:        1.4.3
Release:        %autorelease
Summary:        Fast Base64 encoding and decoding for Python
License:        BSD-2-Clause
URL:            https://github.com/mayeut/pybase64
VCS:            git:https://github.com/mayeut/pybase64.git
#!RemoteAsset:  sha256:c2ed274c9e0ba9c8f9c4083cfe265e66dd679126cd9c2027965d807352f3f053
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} -L

BuildRequires:  cmake
BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
pybase64 provides fast Base64 encoding and decoding for Python with an
optimized native extension and a compatible Python interface.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.rst
%{_bindir}/pybase64

%changelog
%autochangelog
