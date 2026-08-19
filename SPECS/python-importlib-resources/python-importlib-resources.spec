# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname importlib-resources
%global pypi_name importlib_resources

Name:           python-%{srcname}
Version:        7.1.0
Release:        %autorelease
Summary:        Read resources from Python packages
License:        Apache-2.0
URL:            https://github.com/python/importlib_resources
#!RemoteAsset:  sha256:0722d4c6212489c530f2a145a34c0a7a3b4721bc96a15fada5930e2a0b760708
Source0:        https://files.pythonhosted.org/packages/source/i/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}
# Skip upstream test modules: ModuleNotFoundError: No module named 'jaraco'.
BuildOption(check):  -e 'importlib_resources.tests.compat.py*' -e 'importlib_resources.tests.test_*' -e 'importlib_resources.tests.util'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(coherent-licensed)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm[toml])
BuildRequires:  python3dist(zipp)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
importlib_resources is a backport of Python's standard-library
importlib.resources module for older Python versions.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
