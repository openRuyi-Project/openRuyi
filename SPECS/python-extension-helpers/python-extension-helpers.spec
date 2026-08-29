# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname extension-helpers
%global pypi_name extension_helpers

Name:           python-%{srcname}
Version:        1.4.0
Release:        %autorelease
Summary:        Utilities for building Python extension modules
License:        BSD-3-Clause
URL:            https://github.com/astropy/extension-helpers
#!RemoteAsset:  sha256:78d04185f196e3e0bc5fd8418ce298b014c46f7ac609f6a8c10bf70e8c978324
Source0:        https://files.pythonhosted.org/packages/source/e/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l extension_helpers

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Extension helpers provides utilities for building Python extension modules.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE.rst

%changelog
%autochangelog
