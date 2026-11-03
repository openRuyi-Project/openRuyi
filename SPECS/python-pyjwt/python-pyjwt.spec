# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Zitao Zhou <zitao.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pyjwt

Name:           python-%{srcname}
Version:        2.15.1
Release:        %autorelease
Summary:        Implementation of JSON Web Token validation for Python
License:        MIT
URL:            https://github.com/jpadilla/pyjwt
#!RemoteAsset:  sha256:4f259e80cdfb6b3fc18a7de51fd1ef9ec79652f25019bae68975ca2468a34df8
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# Import as jwt
BuildOption(install):  -l jwt

BuildRequires:  python3dist(pytest)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(cryptography) >= 3.4

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
PyJWT is a Python implementation of JSON Web Token draft 01.
This library provides a means of representing signed content using JSON data
structures, including claims to be transferred between two parties encoded as
digitally signed and encrypted JSON objects.

%pyproject_extras_subpkg -n python-%{srcname} crypto

%generate_buildrequires
%pyproject_buildrequires

%check -a
# Exercise JWT decoding, algorithm selection and rejection of invalid signatures.
%pytest tests

%files -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
