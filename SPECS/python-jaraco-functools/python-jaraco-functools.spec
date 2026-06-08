# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname jaraco-functools
%global pypi_name jaraco_functools

Name:           python-%{srcname}
Version:        4.5.0
Release:        %autorelease
Summary:        Functools like those found in stdlib
License:        MIT
URL:            https://github.com/jaraco/jaraco.functools
VCS:            git:https://github.com/jaraco/jaraco.functools.git
#!RemoteAsset:  sha256:3bb5665ea4a020cf78a7040e89154c77edadb3ca74f366479669c5999aa70b03
Source0:        https://files.pythonhosted.org/packages/source/j/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l jaraco +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Additional functools in the spirit of stdlib's functools, collected in the
jaraco namespace.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
