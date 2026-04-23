# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pyjwt

Name:           python-%{srcname}
Version:        2.10.1
Release:        %autorelease
Summary:        Implementation of JSON Web Token validation for Python
License:        MIT
URL:            https://github.com/jpadilla/pyjwt
#!RemoteAsset:  sha256:3cc5772eb20009233caf06e9d8a0577824723b44e6648ee0a2aedb6cf9381953
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# Import as jwt
BuildOption(install):  jwt

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
jsonschema is a Python implementation of JSON Web Token draft 01.
This library provides a means of representing signed content using JSON data
structures, including claims to be transferred between two parties encoded as
digitally signed and encrypted JSON objects.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
