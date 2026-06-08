# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname jaraco-context
%global pypi_name jaraco_context

Name:           python-%{srcname}
Version:        6.1.2
Release:        %autorelease
Summary:        Useful decorators and context managers
License:        MIT
URL:            https://github.com/jaraco/jaraco.context
VCS:            git:https://github.com/jaraco/jaraco.context.git
#!RemoteAsset:  sha256:f1a6c9d391e661cc5b8d39861ff077a7dc24dc23833ccee564b234b81c82dfe3
Source0:        https://files.pythonhosted.org/packages/source/j/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l jaraco +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Context managers and decorators collected in the jaraco namespace.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
