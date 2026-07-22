# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname sparse

Name:           python-%{srcname}
Version:        0.19.0
Release:        %autorelease
Summary:        Sparse n-dimensional arrays for the PyData ecosystem
License:        BSD-3-Clause
URL:            https://sparse.pydata.org/
VCS:            git:https://github.com/pydata/sparse.git
#!RemoteAsset:  sha256:a95a52c63b45e2071df014d3f60080d36d160288131533a3b844021450677430
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l sparse
# Skip test: No module named 'finch' (missing julia)
BuildOption(check):  -e 'sparse.finch_backend*'
# Skip test: No module named 'mlir_finch' (missing julia)
BuildOption(check):  -e 'sparse.mlir_backend*'
# Skip test: No module named 'dask' (circular dependency)
BuildOption(check):  -e 'sparse.numba_backend.tests.test_dask_interop'

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(numba)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(scipy)
BuildRequires:  python3dist(setuptools-scm)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Sparse implements sparse multidimensional arrays for the PyData ecosystem. It
supports NumPy-like operations while storing only nonzero values.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
