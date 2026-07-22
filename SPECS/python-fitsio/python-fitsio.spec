# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname fitsio

Name:           python-%{srcname}
Version:        1.4.2
Release:        %autorelease
Summary:        Python interface to CFITSIO
License:        GPL-2.0-or-later
URL:            https://github.com/esheldon/fitsio
#!RemoteAsset:  sha256:92a02f0e63d539d85ca5a185ae0cc8d40029270858275964ee2539ee0136f0c3
Source0:        https://files.pythonhosted.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l fitsio

BuildRequires:  pkgconfig(cfitsio)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Fitsio is a Python interface for reading and writing FITS files using CFITSIO.

%generate_buildrequires
%pyproject_buildrequires

%build -p
export FITSIO_USE_SYSTEM_FITSIO=1

%check -a
cd ..
%pytest -v --pyargs fitsio.tests

%files -f %{pyproject_files}
%doc CHANGES.md README.md
%license LICENSE.txt

%changelog
%autochangelog
