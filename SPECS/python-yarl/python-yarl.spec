# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname yarl

Name:           python-%{srcname}
Version:        1.25.1
Release:        %autorelease
Summary:        Python module to handle URLs
License:        Apache-2.0
URL:            https://github.com/aio-libs/yarl
#!RemoteAsset:  sha256:03dd38de09bc213e9a8b29761eec33ee1d5318dac0e49d8af36e4d27830e23a7
Source0:        https://files.pythonhosted.org/packages/source/y/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(hypothesis)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(expandvars)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(idna)
BuildRequires:  python3dist(multidict)
BuildRequires:  python3dist(propcache)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
The module provides handy URL class for URL parsing and changing.

%generate_buildrequires
%pyproject_buildrequires

%check -a
# Benchmark fixtures and Pydantic 2.13 integration are outside the packaged test dependencies.
%pytest -o addopts='' \
    --ignore=tests/test_query_benchmarks.py \
    --ignore=tests/test_url_benchmarks.py \
    --ignore=tests/test_quoting_benchmarks.py \
    --ignore=tests/test_pydantic.py

%files -f %{pyproject_files}
%doc CHANGES.rst README.rst

%changelog
%autochangelog
