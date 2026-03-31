# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname bcrypt

Name:           python-%{srcname}
Version:        3.2.2
Release:        %autorelease
Summary:        Modern password hashing library
License:        Apache-2.0
URL:            https://github.com/pyca/bcrypt
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/b/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pytest
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
Bcrypt is a Python module which provides a password hashing method based
on the Blowfish password hashing algorithm, as described in
@url{http://static.usenix.org/events/usenix99/provos.html,"A Future-Adaptable
Password Scheme"} by Niels Provos and David Mazieres.

%generate_buildrequires
%pyproject_buildrequires

%check
%pytest

%files -f %{pyproject_files}
%doc README*

%changelog
%{?autochangelog}
