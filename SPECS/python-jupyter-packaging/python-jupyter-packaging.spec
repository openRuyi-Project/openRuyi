# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname jupyter-packaging
%global pypi_name jupyter_packaging

Name:           python-%{srcname}
Version:        0.12.3
Release:        %autorelease
Summary:        Jupyter packaging utilities
License:        BSD-3-Clause
URL:            https://github.com/jupyter/jupyter-packaging
#!RemoteAsset:  sha256:9d9b2b63b97ffd67a8bc5391c32a421bc415b264a32c99e4d8d8dd31daae9cf4
Source0:        https://files.pythonhosted.org/packages/source/j/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l jupyter_packaging

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(deprecation)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(tomlkit)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Utilities for building and distributing Jupyter extensions.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
