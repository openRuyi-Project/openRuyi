# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname python-json-logger
%global pypi_name python_json_logger

Name:           python-%{srcname}
Version:        4.1.0
Release:        %autorelease
Summary:        JSON formatter for the Python logging package
License:        BSD-2-Clause
URL:            https://nhairs.github.io/python-json-logger
VCS:            git:https://github.com/nhairs/python-json-logger.git
#!RemoteAsset:  sha256:b396b9e3ed782b09ff9d6e4f1683d46c83ad0d35d2e407c09a9ebbf038f88195
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l pythonjsonlogger
BuildOption(check):  -e pythonjsonlogger.msgspec -e pythonjsonlogger.orjson

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
python-json-logger provides JSON formatters for the Python logging package.
It helps applications emit structured log records for machines and people.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md NOTICE
%license LICENSE

%changelog
%autochangelog
