# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pytest-random-order
%global pypi_name pytest_random_order

Name:           python-%{srcname}
Version:        1.2.0
Release:        %autorelease
Summary:        Randomize the order of pytest tests
License:        MIT
URL:            https://github.com/jbasko/pytest-random-order
VCS:            git:https://github.com/jbasko/pytest-random-order.git
#!RemoteAsset:  sha256:12b2d4ee977ec9922b5e3575afe13c22cbdb06e3d03e550abc43df137b90439a
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l random_order

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm) >= 8

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
pytest-random-order randomizes test execution order while keeping controls for
bucketed and repeatable runs.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.rst CHANGELOG.rst

%changelog
%autochangelog
