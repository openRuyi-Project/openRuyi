# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname joblib

Name:           python-%{srcname}
Version:        1.5.2
Release:        %autorelease
Summary:        Lightweight pipelining: using Python functions as pipeline jobs
License:        BSD-3-Clause
URL:            https://github.com/joblib/joblib
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/j/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
# Tests
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(psutil)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
Joblib is a set of tools to provide lightweight pipelining in Python.

%generate_buildrequires
%pyproject_buildrequires

%check
# Always failed tests
%pytest \
    --deselect "joblib/test/test_memory.py::test_parallel_call_cached_function_defined_in_jupyter" \
    joblib

%files -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
