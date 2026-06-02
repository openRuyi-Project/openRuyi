# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname xarray

Name:           python-%{srcname}
Version:        2026.4.0
Release:        %autorelease
Summary:        N-D labeled arrays and datasets in Python
License:        Apache-2.0
URL:            https://xarray.dev/
VCS:            git:https://github.com/pydata/xarray.git
#!RemoteAsset:  sha256:c4ac9a01a945d90d5b1628e2af045099a9d4943536d4f2ee3ae963c3b222d15b
Source0:        https://files.pythonhosted.org/packages/source/x/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
# skip tests: No module named 'cupy'
BuildOption(check):  -e 'xarray.tests.test_cupy'
# skip tests: No module named 'sparse'
BuildOption(check):  -e 'xarray.tests.test_sparse'
# skip tests: circular dependency with python-pint
BuildOption(check):  -e 'xarray.tests.test_units'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(array-api-strict)
BuildRequires:  python3dist(cftime)
BuildRequires:  python3dist(dask)
BuildRequires:  python3dist(distributed)
BuildRequires:  python3dist(hypothesis)
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pandas)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pyarrow)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytz)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
xarray is a Python package for working with labeled multi-dimensional
arrays, providing a pandas-like API for N-dimensional data.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
