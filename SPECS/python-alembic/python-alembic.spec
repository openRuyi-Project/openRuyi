# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname alembic

Name:           python-%{srcname}
Version:        1.18.4
Release:        %autorelease
Summary:        A database migration tool for SQLAlchemy
License:        MIT
URL:            https://alembic.sqlalchemy.org
VCS:            git:https://github.com/sqlalchemy/alembic.git
#!RemoteAsset:  sha256:cb6e1fd84b6174ab8dbb2329f86d631ba9559dd78df550b57804d607672cedbc
Source:         https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
BuildOption(check):  -e "%{srcname}.templates.*" -e "%{srcname}.testing.suite*"

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)

Requires:       python3dist(sqlalchemy)
Requires:       python3dist(mako)
Requires:       python3dist(typing-extensions)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Alembic is a database migration tool written by the author of SQLAlchemy.
It provides a full suite of well-known database migration patterns including
emission of ALTER statements, automatic generation of migration scripts,
and support for multiple databases.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/alembic

%changelog
%autochangelog
