# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname python_utils

Name:           python-utils
Version:        3.9.1
Release:        %autorelease
Summary:        Library to provide visual progress to long running operations
License:        BSD-3-Clause
URL:            https://github.com/WoLpH/python-utils
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/p/%{name}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  pyproject-rpm-macros
# the follow is for test.
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(typing-extensions)

Provides:       python3-utils
%python_provide python3-utils

%description
Python Utils is a collection of small Python functions and classes which
make common patterns shorter and easier. This module makes it easy to
execute common tasks in Python scripts such as converting text to numbers
and making sure a string is in unicode or bytes format.

%generate_buildrequires
%pyproject_buildrequires -r

%check
# Ignoring test_logger.py and python_utils/loguru.py - we don't have loguru
# and we don't have python3-pytest-cov yet.
%pytest -o "addopts=" --ignore _python_utils_tests/test_logger.py --ignore python_utils/loguru.py

%files -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
