# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname platformdirs

Name:           python-%{srcname}
Version:        4.4.0
Release:        %autorelease
License:        MIT
URL:            https://github.com/platformdirs/platformdirs
Summary:        Determine the appropriate platform-specific directories
Provides:       python3-%{srcname}
%python_provide python3-%{srcname}
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildSystem:    pyproject
BuildOption(install): -l %{srcname} +auto
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
