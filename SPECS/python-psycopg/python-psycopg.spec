# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname psycopg

Name:           python-%{srcname}
Version:        3.3.4
Release:        %autorelease
Summary:        PostgreSQL database adapter for Python
License:        LGPL-3.0-only
URL:            https://psycopg.org
VCS:            git:https://github.com/psycopg/psycopg.git
#!RemoteAsset:  sha256:e21207764952cff81b6b8bdacad9a3939f2793367fdac2987b3aac36a651b5bc
Source:         https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
# Skip import check for modules requiring libpq or optional deps at import time
BuildOption(check):  -e "%{srcname}.pq" -e "%{srcname}.types.shapely" -e "%{srcname}.crdb*"

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(libpq)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(numpy)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
psycopg is a PostgreSQL database adapter for the Python programming language.
It is a complete rewrite of the psycopg2 package, designed for Python 3 and
based on the libpq PostgreSQL client library. psycopg 3 supports both
synchronous and asynchronous operation.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst

%changelog
%autochangelog
