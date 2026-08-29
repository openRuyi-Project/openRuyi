# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname ml-dtypes
%global pypi_name ml_dtypes

Name:           python-%{srcname}
Version:        0.5.4
Release:        %autorelease
Summary:        A stand-alone implementation of several NumPy dtype extensions
License:        Apache-2.0
URL:            https://github.com/jax-ml/ml_dtypes
#!RemoteAsset:  sha256:8ab06a50fb9bf9666dd0fe5dfb4676fa2b0ac0f31ecff72a6c3af8e22c063453
Source0:        https://files.pythonhosted.org/packages/source/m/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildSystem:    pyproject

# https://github.com/jax-ml/ml_dtypes/pull/358
# Upstream not merge the PR, instead, changed the build backend.
Patch1000:      1000-Update-setuptools-requirement.patch

BuildOption(install):  -l %{pypi_name}

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(numpy)
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

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
