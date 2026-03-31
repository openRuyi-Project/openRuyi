# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname resolvelib

Name:           python-%{srcname}
Version:        1.1.0
Release:        %autorelease
Summary:        Abstract dependencies resolver
License:        ISC
URL:            https://github.com/sarugaku/resolvelib
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/r/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
The ResolveLib library provides a @code{Resolver} class that includes
dependency resolution logic.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README*

%changelog
%{?autochangelog}
