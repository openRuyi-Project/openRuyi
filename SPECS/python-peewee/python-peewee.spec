# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname peewee

Name:           python-%{srcname}
Version:        4.0.5
Release:        %autorelease
Summary:        Small and expressive ORM
License:        MIT
URL:            https://github.com/coleifer/peewee
#!RemoteAsset:  sha256:b43a21493f19f205a016cb4a9e29c7eca3500576d29447a89732022d193450ba
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} playhouse pwiz

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(apsw)
BuildRequires:  python3dist(cysqlite)
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(flask)
BuildRequires:  python3dist(greenlet)
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pydantic)
BuildRequires:  python3dist(pysqlcipher3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Peewee is a small and expressive ORM for Python applications.

%generate_buildrequires
%pyproject_buildrequires

%build -p
export NO_SQLITE=1

%files -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.rst
%license LICENSE
%{_bindir}/pwiz

%changelog
%autochangelog
