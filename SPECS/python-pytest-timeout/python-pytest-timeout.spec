# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pytest-timeout
%global pypi_name pytest_timeout

Name:           python-%{srcname}
Version:        2.4.0
Release:        %autorelease
Summary:        Abort hanging pytest tests
License:        MIT
URL:            https://github.com/pytest-dev/pytest-timeout
VCS:            git:https://github.com/pytest-dev/pytest-timeout.git
#!RemoteAsset:  sha256:7e68e90b01f9eff71332b25001f85c75495fc4e3a836701876183c4bcfd0540a
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l pytest_timeout

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
pytest-timeout adds timeout handling for hanging pytest tests and sessions.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
