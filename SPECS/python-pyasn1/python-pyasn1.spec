# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pyasn1

Name:           python-%{srcname}
Version:        0.6.1
Release:        %autorelease
Summary:        ASN.1 tools for Python
License:        BSD-2-Clause
URL:            https://github.com/pyasn1/pyasn1
#!RemoteAsset:  sha256:6f580d2bdd84365380830acf45550f2511469f673cb4a5ae3857a3170128b034
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This is an implementation of ASN.1 types and codecs in Python programming
language.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE.rst

%changelog
%autochangelog
