# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname mitogen

Name:           python-%{srcname}
Version:        0.3.47
Release:        %autorelease
Summary:        Distributed self-replicating programs in Python
License:        BSD-3-Clause
URL:            https://github.com/mitogen-hq/mitogen
#!RemoteAsset:  sha256:fcd678d5098ddbefc948a70cf72dc781f450702d78ce9beec83588a2cfa853cb
Source:         https://files.pythonhosted.org/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pip)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Mitogen is a Python library for writing distributed self-replicating programs.
There is no requirement for installing packages, copying files around, writing
shell snippets, upfront configuration, or providing any secondary link to a
remote machine aside from an SSH connection.

%generate_buildrequires
%pyproject_buildrequires

%check
# tests/README.md says the tests need:
#    - internet connection
#    - working docker daemon

%files -f %{pyproject_files}
%license LICENSE
%doc README.md
%{python3_sitelib}/ansible_%{srcname}

%changelog
%autochangelog
