# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname rsa

Name:           python-%{srcname}
Version:        4.9.1
Release:        %autorelease
Summary:        Pure-Python RSA implementation
License:        Apache-2.0
URL:            https://github.com/sybrenstuvel/python-rsa
#!RemoteAsset:  sha256:e7bdbfdb5497da4c07dfd35530e1a902659db6ff241e39d9953cad06ebd0ae75
Source0:        https://files.pythonhosted.org/packages/source/r/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pyasn1)
BuildRequires:  python3dist(poetry-core)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Pure-Python RSA implementation. Supports encryption, decryption, signing,
verification, and key generation with PKCS#1 v1.5 and PKCS#1 OAEP.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{_bindir}/pyrsa-decrypt
%{_bindir}/pyrsa-encrypt
%{_bindir}/pyrsa-keygen
%{_bindir}/pyrsa-priv2pub
%{_bindir}/pyrsa-sign
%{_bindir}/pyrsa-verify

%changelog
%autochangelog
