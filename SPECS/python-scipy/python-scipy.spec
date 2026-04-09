# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname scipy

%global _pyproject_wheeldir %{_builddir}/%{name}-%{version}-%{release}/pyproject-wheeldir

Name:           python-%{srcname}
Version:        1.17.0
Release:        %autorelease
Summary:        Scientific Tools for Python
License:        BSD-3-Clause AND LGPL-2.0-or-later AND BSL-1.0
URL:            https://www.scipy.org
#!RemoteAsset:  sha256:2591060c8e648d8b96439e111ac41fd8342fdeff1876be2e19dea3fe8930454e
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(build):  -Csetup-args=-Dblas=openblas64
BuildOption(build):  -Csetup-args=-Dlapack=openblas64
BuildOption(install):  -l %{srcname} -L

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

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
Data validation using Python type hints.

%generate_buildrequires
%pyproject_buildrequires -R

%build -p
export FC=gfortran

%check
# skip tests as some deps we don't have yet.

%files -f %{pyproject_files}

%changelog
%autochangelog
