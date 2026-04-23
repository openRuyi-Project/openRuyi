# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname platformdirs

Name:           python-%{srcname}
Version:        4.4.0
Release:        %autorelease
Summary:        Determine the appropriate platform-specific directories
License:        MIT
URL:            https://github.com/platformdirs/platformdirs
#!RemoteAsset:  sha256:ca753cf4d81dc309bc67b0ea38fd15dc97bc30ce419a7f58d13eb3bf14c4febf
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
When writing applications, finding the right location to
store user data and configuration varies per platform.  Even for
single-platform apps, there may by plenty of nuances in figuring out the right
location.  This small Python module determines the appropriate
platform-specific directories, e.g. the ``user data dir''.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README*

%changelog
%autochangelog
