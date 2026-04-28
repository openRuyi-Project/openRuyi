# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname apscheduler

Name:           python-%{srcname}
Version:        3.11.2
Release:        %autorelease
Summary:        In-process task scheduler with Cron-like capabilities
License:        MIT
URL:            https://github.com/agronholm/apscheduler
#!RemoteAsset:  sha256:2a9966b052ec805f020c8c4c3ae6e6a06e24b1bf19f2e11d91d8cca0473eef41
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(tzlocal)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Advanced Python Scheduler (APScheduler) is an in-process task
scheduler that lets you schedule jobs (functions or any python callables) to be
executed at any time of your choosing.

This can be an alternative to externally run cron scripts for
long-running applications (e.g. web applications), as it is platform neutral
and can access the application's variables and functions.

APscheduler provides multiple job stores.

* Configurable scheduling mechanisms (triggers):
  * Cron-like scheduling
  * Delayed scheduling of single run jobs (like the UNIX "at" command)
  * Interval-based (run a job at specified time intervals)
* Multiple, simultaneously active job stores:
  * RAM
  * File-based simple database (shelve)
  * SQLAlchemy (any supported RDBMS works)
  * MongoDB

%generate_buildrequires
%pyproject_buildrequires

%check
# skip tests as some deps we don't have yet.

%files -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
