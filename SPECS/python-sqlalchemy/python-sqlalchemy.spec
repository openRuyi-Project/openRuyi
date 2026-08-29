# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname sqlalchemy

Name:           python-%{srcname}
Version:        2.0.49
Release:        %autorelease
Summary:        Database Abstraction Library
License:        MIT
URL:            https://www.sqlalchemy.org
VCS:            git:https://github.com/sqlalchemy/sqlalchemy.git
#!RemoteAsset:  sha256:d15950a57a210e36dd4cec1aac22787e2a4d57ba9318233e2ef8b2daf9ff2d5f
Source:         https://files.pythonhosted.org/packages/source/s/sqlalchemy/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
BuildOption(check):  -e "%{srcname}.testing.plugin.*"

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(mypy)
BuildRequires:  python3dist(pytest)

Requires:       python3dist(typing-extensions)
Requires:       python3dist(greenlet)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives
application developers the full power and flexibility of SQL. It provides a
full suite of well known enterprise-level persistence patterns, designed for
efficient and high-performing database access, adapted into a simple and
Pythonic domain language.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst README.dialects.rst
%license LICENSE

%changelog
%autochangelog
