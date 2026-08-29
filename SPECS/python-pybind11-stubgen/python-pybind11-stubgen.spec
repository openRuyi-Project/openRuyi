# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pybind11-stubgen
%global pypi_name pybind11_stubgen

Name:           python-%{srcname}
Version:        2.5.5
Release:        %autorelease
Summary:        PEP 561 type stubs generator for pybind11 modules
License:        BSD-3-Clause
URL:            https://github.com/pybind/pybind11-stubgen
#!RemoteAsset:  sha256:758d6d6bbeefc62ad7f78d5e5bbf357ccf6af83cd4504f5f549403f452942708
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(parso)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Static analysis tools and IDE usually struggle to
understand python binary extensions. pybind11-stubgen
generates stubs for python extensions to make them less opaque.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/pybind11-stubgen

%changelog
%autochangelog
