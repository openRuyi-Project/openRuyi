# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname google-auth
%global pypi_name google_auth

Name:           python-%{srcname}
Version:        2.49.2
Release:        %autorelease
Summary:        Google Authentication Library
License:        Apache-2.0
URL:            https://github.com/googleapis/google-auth-library-python
#!RemoteAsset:  sha256:c1ae38500e73065dcae57355adb6278cf8b5c8e391994ae9cbadbcb9631ab409
Source0:        https://files.pythonhosted.org/packages/source/g/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  google

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3dist(grpcio)
BuildRequires:  python3dist(pyasn1-modules)
BuildRequires:  python3dist(cryptography)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(urllib3)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Google Auth Python Library provides authentication support for Google APIs
and services. It simplifies using various server-to-server authentication
mechanisms.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
