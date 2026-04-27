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
#!RemoteAsset:  sha256:b68591ef748f58c1e2a2ac28d0961b3586ae8b25f60b0ba9a5e4f3d87c1d6a79
Source0:        https://files.pythonhosted.org/packages/source/r/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
The ResolveLib library provides a Resolver class that includes
dependency resolution logic.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README*

%changelog
%autochangelog
