# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname smmap

Name:           python-%{srcname}
Version:        5.0.3
Release:        %autorelease
Summary:        Sliding window memory map manager
License:        BSD-3-Clause
URL:            https://github.com/gitpython-developers/smmap
#!RemoteAsset:  sha256:4d9debb8b99007ae47165abc08670bd74cb74b5227dda7f643eccc4e9eb5642c
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Smmap wraps an interface around mmap and tracks the mapped files as well as
the amount of clients who use it. If the system runs out of resources,
or if a memory limit is reached, it will automatically unload unused maps
to allow continued operation.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
