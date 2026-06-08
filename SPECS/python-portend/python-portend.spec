# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname portend

Name:           python-%{srcname}
Version:        3.2.1
Release:        %autorelease
Summary:        TCP port monitoring and discovery
License:        MIT
URL:            https://github.com/jaraco/portend
VCS:            git:https://github.com/jaraco/portend.git
#!RemoteAsset:  sha256:aa9d40ab1f9e14bdb7d401f42210df35d017c9b97991baeb18568cedfb8c6489
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l portend +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
portend monitors TCP ports for bound or unbound states, useful for waiting
until a service is ready or has shut down.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
