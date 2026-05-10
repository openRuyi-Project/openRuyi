# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname gast

Name:           python-%{srcname}
Version:        0.7.0
Release:        %autorelease
Summary:        Python AST that abstracts the underlying Python version
License:        BSD-3-Clause
URL:            https://github.com/serge-sans-paille/gast/
#!RemoteAsset:  sha256:0bb14cd1b806722e91ddbab6fb86bba148c22b40e7ff11e248974e04c8adfdae
Source0:        https://files.pythonhosted.org/packages/source/g/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
A generic AST to represent Python2 and Python3's Abstract Syntax Tree(AST).

GAST provides a compatibility layer between the AST of various Python
versions, as produced by ast.parse from the standard ast module.

%build -p
rm %{_builddir}/%{name}-%{version}/gast/ast2.py # No use of Python 2.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
