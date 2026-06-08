# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname jaraco-collections
%global pypi_name jaraco_collections

Name:           python-%{srcname}
Version:        5.2.1
Release:        %autorelease
Summary:        Collection objects similar to those in stdlib by jaraco
License:        MIT
URL:            https://github.com/jaraco/jaraco.collections
VCS:            git:https://github.com/jaraco/jaraco.collections.git
#!RemoteAsset:  sha256:dab81970bad6f0ab53b20745f1b01da37926e4c0fcd425046aa45e0d8efa18ed
Source0:        https://files.pythonhosted.org/packages/source/j/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l jaraco +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Collection objects similar to those in the standard library, collected in the
jaraco namespace.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
