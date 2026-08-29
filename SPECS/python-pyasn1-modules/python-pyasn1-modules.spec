# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pyasn1-modules

Name:           python-%{srcname}
Version:        0.4.2
Release:        %autorelease
Summary:        Collection of protocols modules written in ASN.1 language
License:        BSD-2-Clause
URL:            https://github.com/pyasn1/pyasn1-modules
#!RemoteAsset:  sha256:677091de870a80aae844b1ca6134f54652fa2c8c5a52aa396440ac3106e941e6
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/pyasn1_modules-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  pyasn1_modules

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

Requires:       python3dist(pyasn1)

%description
This is an implementation of ASN.1 types and codecs in Python programming
language.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
