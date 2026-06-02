# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname dask

Name:           python-%{srcname}
Version:        2026.3.0
Release:        %autorelease
Summary:        Parallel PyData with Task Scheduling
License:        BSD-3-Clause
URL:            https://github.com/dask/dask
#!RemoteAsset:  sha256:f7d96c8274e8a900d217c1ff6ea8d1bbf0b4c2c21e74a409644498d925eb8f85
Source0:        https://files.pythonhosted.org/packages/source/d/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
# skip tests: No module named 'distributed' (circular dependency)
BuildOption(check):  -e 'dask.tests.test_distributed'
BuildOption(check):  -e 'dask.distributed'
BuildOption(check):  -e 'dask.tests.test_layers'
BuildOption(check):  -e 'dask.dataframe.dask_expr.tests.test_distributed'
BuildOption(check):  -e 'dask.dataframe.dask_expr.io.tests.test_distributed'
BuildOption(check):  -e 'dask.dataframe.dask_expr.tests.test_diagnostics'
# skip tests: No module named 'cupy'
BuildOption(check):  -e 'dask.array.tests.test_cupy*'
# skip tests: No module named 'skimage'
BuildOption(check):  -e 'dask.array.tests.test_image'
# skip tests: No module named 'sparse'
BuildOption(check):  -e 'dask.array.tests.test_sparse'
# skip tests: No module named 'xarray' (circular dependency)
BuildOption(check):  -e 'dask.array.tests.test_xarray'
# skip tests: No module named 'ipycytoscape'
BuildOption(check):  -e 'dask.tests.test_dot'
# skip tests: No module named 'pyspark'
BuildOption(check):  -e 'dask.tests.test_spark_compat'
# skip tests: pyarrow ORC support not available (No module named 'pyarrow._orc')
BuildOption(check):  -e 'dask.dataframe.io.orc.arrow'
BuildOption(check):  -e 'dask.dataframe.io.tests.test_orc'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3dist(boto3)
BuildRequires:  python3dist(cachey)
BuildRequires:  python3dist(click)
BuildRequires:  python3dist(cloudpickle)
BuildRequires:  python3dist(fastavro)
BuildRequires:  python3dist(flask)
BuildRequires:  python3dist(fsspec)
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(moto)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pandas)
BuildRequires:  python3dist(partd)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pyarrow)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(s3fs)
BuildRequires:  python3dist(scipy)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(sqlalchemy)
BuildRequires:  python3dist(toolz)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Dask is a flexible library for parallel computing in Python, providing
parallel arrays, dataframes and task scheduling.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt
%{_bindir}/dask

%changelog
%autochangelog
