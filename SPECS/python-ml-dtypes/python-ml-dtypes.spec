# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname ml-dtypes
%global pypi_name ml_dtypes

Name:           python-%{srcname}
Version:        0.6.0
Release:        %autorelease
Summary:        A stand-alone implementation of several NumPy dtype extensions
License:        Apache-2.0
URL:            https://github.com/jax-ml/ml_dtypes
#!RemoteAsset:  sha256:5e60251d32ced5598972e4d5e06a2f044341f9291402551a3f6f0ec44f9299b0
Source0:        https://files.pythonhosted.org/packages/source/m/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(scikit-build-core)
BuildRequires:  python3dist(cmake)
BuildRequires:  python3dist(ninja)
BuildRequires:  gcc-c++

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
ml_dtypes is a stand-alone implementation of several NumPy dtype extensions
used in machine learning libraries, including:
* bfloat16
* float8 (e4m3, e5m2)
* int4

# TODO: For some reason, Open Build Service does not like this and will cause build loop. - 251
#generate_buildrequires
#pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
