# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pythran

Name:           python-%{srcname}
Version:        0.18.1
Release:        %autorelease
Summary:        Scientific Tools for Python
License:        BSD-3-Clause
URL:            https://github.com/serge-sans-paille/pythran
#!RemoteAsset:  sha256:8803ed948bf841a11bbbb10472a8ff6ea24ebd70e67c3f77b77be3db900eccfe
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} omp

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(ply)
BuildRequires:  python3dist(gast)
BuildRequires:  python3dist(beniget)
# For tests
BuildRequires:  python3dist(ipython)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Data validation using Python type hints.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%{_bindir}/pythran
%{_bindir}/pythran-config

%changelog
%autochangelog
