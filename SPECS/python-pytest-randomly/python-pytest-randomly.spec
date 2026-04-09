# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global pypi_name pytest_randomly

%global srcname pytest-randomly

%bcond tests 0

Name:           python-%{srcname}
Version:        4.0.1
Release:        %autorelease
Summary:        Pytest plugin to randomly order tests and control random.seed
License:        MIT
URL:            https://github.com/pytest-dev/pytest-randomly
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
%if %{with tests}
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(factory-boy)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pytest-xdist)
%endif

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
Pytest plugin to randomly order tests and control random.seed.

%generate_buildrequires
%pyproject_buildrequires

%check
%if %{with tests}
%pytest -p no:randomly -k 'not test_it_runs_before_stepwise and not test_model_bakery'
%endif

%files -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
