# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname cftime

Name:           python-%{srcname}
Version:        1.6.5
Release:        %autorelease
Summary:        Time-handling functionality from netcdf4-python
License:        MIT
URL:            https://github.com/Unidata/cftime
#!RemoteAsset:  sha256:8225fed6b9b43fb87683ebab52130450fc1730011150d3092096a90e54d1e81e
Source0:        https://files.pythonhosted.org/packages/source/c/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
cftime is a Python library for handling time in netCDF files. It provides
the num2date and date2num functions for converting between datetime objects
and numeric time values.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
