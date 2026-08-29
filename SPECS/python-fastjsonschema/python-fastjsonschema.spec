# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname fastjsonschema

Name:           python-%{srcname}
Version:        2.21.2
Release:        %autorelease
Summary:        Fastest Python implementation of JSON schema
License:        BSD-3-Clause
URL:            https://github.com/horejsek/python-fastjsonschema
#!RemoteAsset:  sha256:b1eb43748041c880796cd077f1a07c3d94e93ae84bba5ed36800a33554ae05de
Source:         https://files.pythonhosted.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
fastjsonschema implements validation of JSON documents by JSON schema.
The library implements JSON schema drafts 04, 06 and 07.
The main purpose is to have a really fast implementation.

%generate_buildrequires
%pyproject_buildrequires

%check -a
%pytest -m "not benchmark"

%files -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
