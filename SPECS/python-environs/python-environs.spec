# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname environs

Name:           python-%{srcname}
Version:        14.5.0
Release:        %autorelease
Summary:        Python library for parsing environment variables
License:        MIT
URL:            https://github.com/sloria/environs
#!RemoteAsset:  sha256:f7b8f6fcf3301bc674bc9c03e39b5986d116126ffb96764efd34c339ed9464ee
Source0:        https://files.pythonhosted.org/packages/source/e/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(flit-core)
BuildRequires:  python3dist(python-dotenv)
BuildRequires:  python3dist(marshmallow)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
Environs is a Python library for parsing environment variables.
It allows you to store configuration separate from your code, as per
The Twelve-Factor App methodology.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.md CHANGELOG.md

%changelog
%{?autochangelog}
