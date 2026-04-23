# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pytest-dotenv

Name:           python-%{srcname}
Version:        0.5.2
Release:        %autorelease
Summary:        Automatically detect and load a .env file before running tests
License:        MIT
URL:            https://github.com/quiqua/pytest-dotenv
#!RemoteAsset:  sha256:2dc6c3ac6d8764c71c6d2804e902d0ff810fa19692e95fe138aefc9b1aa73732
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l pytest_dotenv +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This Pytest plugin automatically detects and loads environment variables
from a .env file before running tests.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README*

%changelog
%autochangelog
