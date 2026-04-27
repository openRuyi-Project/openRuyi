# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pytest-order
%global pypi_name pytest_order

Name:           python-%{srcname}
Version:        1.3.0
Release:        %autorelease
Summary:        Run pytest tests in a specific order
License:        MIT
URL:            https://github.com/pytest-dev/pytest-order
VCS:            git:https://github.com/pytest-dev/pytest-order.git
#!RemoteAsset:  sha256:51608fec3d3ee9c0adaea94daa124a5c4c1d2bb99b00269f098f414307f23dde
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l pytest_order

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
pytest-order is a pytest plugin that lets tests run in a user-defined order.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md CHANGELOG.md
%license LICENSE

%changelog
%autochangelog
