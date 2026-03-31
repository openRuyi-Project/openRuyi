# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname gssapi

Name:           python-%{srcname}
Version:        1.11.1
Release:        %autorelease
Summary:        Python GSSAPI Wrapper
License:        ISC
URL:            https://github.com/pythongssapi/python-gssapi
#!RemoteAsset:  sha256:2049ee4b1d0c363163a1344b7282a363f9f4094e51d2c36de0cf01d4735e0ae2
Source0:        https://files.pythonhosted.org/packages/source/g/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  %{srcname}
BuildOption(check):  -e "gssapi.tests.*"

BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(decorator)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
Python-GSSAPI provides both low-level and high level wrappers around the GSSAPI C libraries.
While it focuses on the Kerberos mechanism, it should also be useable with other GSSAPI mechanisms.

%generate_buildrequires
%pyproject_buildrequires

%prep -a
cd %{_builddir}/%{name}-%{version}

%files -f %{pyproject_files}
%doc README.txt
%license LICENSE.txt

%changelog
%{?autochangelog}
