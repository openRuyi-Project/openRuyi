# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname jaraco-text
%global pypi_name jaraco_text

Name:           python-%{srcname}
Version:        4.2.0
Release:        %autorelease
Summary:        Module for text manipulation
License:        MIT
URL:            https://github.com/jaraco/jaraco.text
VCS:            git:https://github.com/jaraco/jaraco.text.git
#!RemoteAsset:  sha256:194e386aa5b15a6616019df87a6b29c00fd3c9c8b0475731b64633ca7afd495b
Source0:        https://files.pythonhosted.org/packages/source/j/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l jaraco +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Text manipulation utilities collected in the jaraco namespace.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
