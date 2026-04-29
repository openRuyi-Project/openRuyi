# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname scikit-learn
%global pypi_name scikit_learn

Name:           python-%{srcname}
Version:        1.8.0
Release:        %autorelease
Summary:        A set of Python modules for machine learning and data mining
License:        BSD-3-Clause
URL:            https://scikit-learn.org
VCS:            git:https://github.com/scikit-learn/scikit-learn.git
#!RemoteAsset:  sha256:9bccbb3b40e3de10351f8f5068e105d0f4083b1a65fa07b6634fbc401a6287fd
Source:         https://files.pythonhosted.org/packages/source/s/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l sklearn
BuildOption(check):  -e "sklearn.*.tests*" -e "sklearn.tests*" -e "sklearn.conftest" -e "sklearn.externals.array_api_compat.cupy*" -e "sklearn.externals.array_api_compat.dask*"

BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(meson-python)
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(scipy)
BuildRequires:  python3dist(torch)

Requires:       python3dist(numpy)
Requires:       python3dist(scipy)
Requires:       python3dist(joblib)
Requires:       python3dist(threadpoolctl)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
scikit-learn is a Python module for machine learning built on top of SciPy
and is distributed under the 3-Clause BSD license. It features various
classification, regression and clustering algorithms including support vector
machines, random forests, gradient boosting, k-means and DBSCAN, and is
designed to interoperate with the Python numerical and scientific libraries
NumPy and SciPy.

%prep -a
# Relax upper bounds on numpy and scipy for openRuyi
sed -i 's/"numpy>=2,<2.4.0"/"numpy>=2"/' pyproject.toml
sed -i 's/"scipy>=1.10.0,<1.17.0"/"scipy>=1.10.0"/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -p

%files -f %{pyproject_files}
%doc README.rst
%license COPYING

%changelog
%autochangelog
