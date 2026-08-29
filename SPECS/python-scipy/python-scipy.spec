# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname scipy

%global _pyproject_wheeldir %{_builddir}/%{name}-%{version}-%{release}/pyproject-wheeldir

Name:           python-%{srcname}
Version:        1.17.1
Release:        %autorelease
Summary:        Scientific Tools for Python
License:        BSD-3-Clause AND LGPL-2.0-or-later AND BSL-1.0
URL:            https://www.scipy.org
#!RemoteAsset:  sha256:95d8e012d8cb8816c226aef832200b1d45109ed4464303e997c5b13122b297c0
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(build):  -Csetup-args=-Dblas=openblas
BuildOption(build):  -Csetup-args=-Dlapack=openblas
BuildOption(install):  -l %{srcname} -L
# We don't have python3dist(pooch)
BuildOption(check):  -e scipy.datasets.tests.test_data
# We have python3dist(hypothesis), but will it cause circular dependencies?
BuildOption(check):  -e scipy.integrate.tests.test_quadrature
BuildOption(check):  -e scipy.ndimage.tests.test_filters
BuildOption(check):  -e scipy.special.tests.test_support_alternative_backends
BuildOption(check):  -e scipy.stats.tests.test_continuous
BuildOption(check):  -e scipy.stats.tests.test_stats
# No module named 'marray'
BuildOption(check):  -e scipy.stats.tests.test_marray

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  gcc-fortran
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(meson-python)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pybind11)
BuildRequires:  python3dist(pythran)
BuildRequires:  python3dist(pip)
BuildRequires:  pkgconfig(openblas64)
# For tests
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Data validation using Python type hints.

%generate_buildrequires
%pyproject_buildrequires -R

%build -p
export FC=gfortran

%files -f %{pyproject_files}

%changelog
%autochangelog
