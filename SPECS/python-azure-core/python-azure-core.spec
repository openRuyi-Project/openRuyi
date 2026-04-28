# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname azure-core
%global pypi_name azure_core

Name:           python-%{srcname}
Version:        1.38.0
Release:        %autorelease
Summary:        Azure Core shared client library for Python
License:        MIT
URL:            https://pypi.org/project/azure-core/
#!RemoteAsset:  sha256:8194d2682245a3e4e3151a667c686464c3786fed7918b394d035bdcd61bb5993
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l azure

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pip)
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(typing-extensions)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Azure Core shared client library for Python.

%generate_buildrequires
%pyproject_buildrequires

%check
# skip tests as there are some deps we don't have yet.

%files -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md CLIENT_LIBRARY_DEVELOPER.md README.md

%changelog
%autochangelog
