# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname nanobind

Name:           python-%{srcname}
Version:        2.12.0
Release:        %autorelease
Summary:        Tiny and efficient C++/Python bindings
License:        BSD-3-Clause
URL:            https://nanobind.readthedocs.org/
#!RemoteAsset:  sha256:0ae77c1a88f27153fa57045ee00f7b0a7b06b1cd3df942e95a34b38c5d0a5bee
Source:         https://files.pythonhosted.org/packages/source/n/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} -L

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(scikit-build-core)
BuildRequires:  python3dist(pip)
BuildRequires:  cmake
BuildRequires:  ninja

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
nanobind is a small binding library that exposes C++ types in Python and vice
versa. It is reminiscent of Boost.Python and pybind11.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
