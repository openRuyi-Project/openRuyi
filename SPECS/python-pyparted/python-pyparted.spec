# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pyparted

Name:           python-pyparted
Version:        3.13.0
Release:        %autorelease
Summary:        Python bindings for GNU parted
License:        GPL-2.0-or-later
URL:            https://github.com/dcantrell/pyparted
#!RemoteAsset:  sha256:443b59eb9ac63b8ca87094e02376646e172c7ea075f955f105889ca3485b06fd
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  make
BuildRequires:  pkgconfig(libparted)
BuildRequires:  e2fsprogs
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
The python-pyparted package is used for manipulating
partition tables.

%generate_buildrequires
%pyproject_buildrequires

# No configure
%conf

%check
make test

%files
%doc AUTHORS HACKING NEWS README.md RELEASE TODO
%license LICENSE
%{python3_sitearch}/_ped.*.so
%{python3_sitearch}/parted
%{python3_sitearch}/%{srcname}-%{version}-*.egg-info

%changelog
%autochangelog
