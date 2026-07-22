# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname cfgrib

Name:           python-%{srcname}
Version:        0.9.15.1
Release:        %autorelease
Summary:        Map GRIB files to the CF data model with ecCodes
License:        Apache-2.0
URL:            https://github.com/ecmwf/cfgrib
#!RemoteAsset:  sha256:d959d8b97e55a63646fa86686b297905ff7f2918a91e3a11d6292dab09598e4d
Source0:        https://files.pythonhosted.org/packages/source/c/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l cf2cdm cfgrib

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(attrs)
BuildRequires:  python3dist(click)
BuildRequires:  python3dist(eccodes)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(xarray)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
cfgrib maps GRIB files to the NetCDF Common Data Model following the CF
Convention using ecCodes.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/cfgrib

%changelog
%autochangelog
