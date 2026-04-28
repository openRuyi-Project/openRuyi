# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname python-utils
%global pypi_name python_utils

Name:           python-%{srcname}
Version:        3.9.1
Release:        %autorelease
Summary:        Library to provide visual progress to long running operations
License:        BSD-3-Clause
URL:            https://github.com/WoLpH/python-utils
#!RemoteAsset:  sha256:eb574b4292415eb230f094cbf50ab5ef36e3579b8f09e9f2ba74af70891449a0
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}
# No module named 'loguru'
BuildOption(check):  -e python_utils.loguru

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  pyproject-rpm-macros
# the follow is for test.
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(typing-extensions)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Python Utils is a collection of small Python functions and classes which
make common patterns shorter and easier. This module makes it easy to
execute common tasks in Python scripts such as converting text to numbers
and making sure a string is in unicode or bytes format.

%generate_buildrequires
%pyproject_buildrequires -r

%check -a
# Ignoring test_logger.py and python_utils/loguru.py - we don't have loguru
# and we don't have python3-pytest-cov yet.
%pytest -o "addopts=" --ignore _python_utils_tests/test_logger.py --ignore python_utils/loguru.py

%files -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
