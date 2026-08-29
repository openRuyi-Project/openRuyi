# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pg8000

Name:           python-%{srcname}
Version:        1.31.5
Release:        %autorelease
Summary:        A Pure-Python PostgreSQL Driver
License:        BSD-3-Clause
URL:            https://github.com/tlocke/pg8000
#!RemoteAsset:  sha256:46ebb03be52b7a77c03c725c79da2ca281d6e8f59577ca66b17c9009618cae78
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(python-dateutil)
BuildRequires:  python3dist(scramp)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
pg8000 is a pure-Python PostgreSQL driver, compatible with the
standard DB-API 2.0 interface.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
