# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zitao Zhou <zitao.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname joserfc

Name:           python-%{srcname}
Version:        1.8.0
Release:        %autorelease
Summary:        The ultimate Python library for JOSE RFCs (JWS, JWE, JWK, JWA, JWT)
License:        BSD-3-Clause
URL:            https://github.com/authlib/joserfc
#!RemoteAsset:  sha256:cbf03cb2c6db8cc5289f1ef8718842e53dba244b4c0de5fefa0c0eaee4bde8db
Source0:        https://files.pythonhosted.org/packages/source/j/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  python3dist(pytest)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(cryptography)
BuildRequires:  python3dist(pycryptodome)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
A comprehensive Python implementation of several essential JSON Object Signing
and Encryption (JOSE) standards, including JWS, JWE, JWK, JWA, and JWT.

%generate_buildrequires
%pyproject_buildrequires

%check -a
# Exercise JOSE key handling, signature verification and encrypted-message round trips.
%pytest tests

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
