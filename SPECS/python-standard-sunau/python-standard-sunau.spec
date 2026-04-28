# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname standard-sunau
%global pypi_name standard_sunau

Name:           python-%{srcname}
Version:        3.13.0
Release:        %autorelease
Summary:        Provide an interface to the Sun AU sound format.
License:        PSF-2.0
URL:            https://github.com/youknowone/python-deadlib
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  sunau

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
The :mod:`sunau` module provides a convenient interface to the Sun AU sound format.
Note that this module is interface-compatible with the modules :mod:`aifc` and
:mod:`wave`.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
