# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname scikit-learn

Name:           python-%{srcname}
Version:        1.8.0
Release:        %autorelease
Summary:        A set of python modules for machine learning and data mining
License:        BSD-3-Clause
URL:            https://scikit-learn.org
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/scikit_learn-%{version}.tar.gz
Patch0:         0001-relax-numpy-scipy-build-upper-bounds.patch
BuildSystem:    pyproject

BuildOption(install):  sklearn
BuildOption(check):  -e 'sklearn.tests.test_docstrings' -e 'sklearn.externals.array_api_compat.cupy*' -e 'sklearn.externals.array_api_compat.dask*' -e 'sklearn.externals.array_api_compat.torch*'

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(meson-python)
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(scipy)
BuildRequires:  python3dist(joblib)
BuildRequires:  python3dist(threadpoolctl)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
Scikit-learn is a Python module for machine learning built on top of SciPy.
It provides simple and efficient tools for data mining and data analysis,
accessible to everybody and reusable in various contexts.

%generate_buildrequires
%pyproject_buildrequires -p

%files -f %{pyproject_files}
%license COPYING

%changelog
%{?autochangelog}
