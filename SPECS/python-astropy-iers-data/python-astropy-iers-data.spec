# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname astropy-iers-data
%global pypi_name astropy_iers_data

Name:           python-%{srcname}
Version:        0.2026.7.13.0.54.2
Release:        %autorelease
Summary:        IERS Earth rotation and leap second data for Astropy
License:        BSD-3-Clause
URL:            https://github.com/astropy/astropy-iers-data
#!RemoteAsset:  sha256:d86e32e95e98a86f83b5b073627442924a0f45cf61a7828da4f565a17d726c2f
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l astropy_iers_data

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(hatch-vcs)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(pip)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This package provides IERS Earth rotation and leap second tables used by
Astropy.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE.rst

%changelog
%autochangelog
