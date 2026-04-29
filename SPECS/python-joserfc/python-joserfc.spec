# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname joserfc

Name:           python-%{srcname}
Version:        1.6.4
Release:        %autorelease
Summary:        The ultimate Python library for JOSE RFCs (JWS, JWE, JWK, JWA, JWT)
License:        BSD-3-Clause
URL:            https://github.com/authlib/joserfc
#!RemoteAsset:  sha256:34ce5f499bfcc5e9ad4cc75077f9278ab3227b71da9aaf28f9ab705f8a560d3c
Source0:        https://files.pythonhosted.org/packages/source/j/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

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

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
