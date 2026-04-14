# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pydantic-settings
%global pypi_name pydantic_settings

Name:           python-%{srcname}
Version:        2.13.1
Release:        %autorelease
Summary:        Settings management using Pydantic
License:        MIT
URL:            https://github.com/pydantic/pydantic-settings
VCS:            git:https://github.com/pydantic/pydantic-settings.git
#!RemoteAsset:  sha256:b4c11847b15237fb0171e1462bf540e294affb9b86db4d9aa5c01730bdbe4025
Source:         https://files.pythonhosted.org/packages/source/p/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(hatchling)

Requires:       python3dist(pydantic)
Requires:       python3dist(python-dotenv)
Requires:       python3dist(typing-inspection)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
pydantic-settings provides settings management for Python applications using
Pydantic models. It supports reading configuration from environment variables,
dotenv files, and other sources.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
