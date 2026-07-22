# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname eccodes

Name:           python-%{srcname}
Version:        2.47.0
Release:        %autorelease
Summary:        Python interface to the ecCodes GRIB and BUFR library
License:        Apache-2.0
URL:            https://github.com/ecmwf/eccodes-python
#!RemoteAsset:  sha256:ae9207ef27c67656d068aab97f172abeb85fc3620f56faa22fdac5b1be75de69
Source0:        https://files.pythonhosted.org/packages/source/e/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l eccodes gribapi

BuildRequires:  pkgconfig(eccodes)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(attrs)
BuildRequires:  python3dist(cffi)
BuildRequires:  python3dist(findlibs)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

Requires:       eccodes

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This package exposes the ecCodes GRIB and BUFR decoder and encoder to Python.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
