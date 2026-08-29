# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname mercantile

Name:           python-%{srcname}
Version:        1.2.1
Release:        %autorelease
Summary:        Web mercator XYZ tile utilities
License:        BSD-3-Clause
URL:            https://github.com/mapbox/mercantile
#!RemoteAsset:  sha256:fa3c6db15daffd58454ac198b31887519a19caccee3f9d63d17ae7ff61b3b56b
Source0:        https://files.pythonhosted.org/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(click)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Mercantile is a Python library for working with Web Mercator XYZ tile
coordinates and spherical mercator tile coordinate systems.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt
%{_bindir}/mercantile

%changelog
%autochangelog
