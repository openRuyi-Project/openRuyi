# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname mpmath

Name:           python-%{srcname}
Version:        1.3.0
Release:        %autorelease
Summary:        Arbitrary-precision floating-point arithmetic in python
License:        BSD-3-Clause
URL:            https://mpmath.org
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  pytest
BuildRequires:  python3dist(setuptools) >= 40.8
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pip)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
@code{mpmath} can be used as an arbitrary-precision substitute for
Python's float/complex types and math/cmath modules, but also does much
more advanced mathematics.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst

%changelog
%{?autochangelog}
