# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname paramiko

Name:           python-%{srcname}
Version:        4.0.0
Release:        %autorelease
Summary:        SSH2 protocol library for python
License:        LGPL-2.1-or-later
URL:            https://github.com/paramiko/paramiko
#!RemoteAsset
Source:         https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l paramiko

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  pytest
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
Paramiko is a module for python 2.3 or greater that implements the SSH2
protocol for secure (encrypted and authenticated) connections to remote
machines.

%generate_buildrequires
%pyproject_buildrequires

# TODO: enable tests.
%check

%files -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%{?autochangelog}
