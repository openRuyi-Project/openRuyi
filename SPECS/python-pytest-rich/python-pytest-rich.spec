# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pytest-rich
%global pypi_name pytest_rich

Name:           python-%{srcname}
Version:        0.2.0
Release:        %autorelease
Summary:        Rich terminal output for pytest sessions
License:        MIT
URL:            https://github.com/nicoddemus/pytest-rich
VCS:            git:https://github.com/nicoddemus/pytest-rich.git
#!RemoteAsset:  sha256:a5cf6c83497de65788c8a609f616fafedac50295c48f2eb3184bc08b67a9893e
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l pytest_rich

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools) >= 42
BuildRequires:  python3dist(setuptools-scm)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
pytest-rich uses Rich to render more readable and colorful pytest session
output.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst CHANGELOG.md
%license LICENSE

%changelog
%autochangelog
