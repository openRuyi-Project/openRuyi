# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname toolz

Name:           python-%{srcname}
Version:        1.1.0
Release:        %autorelease
Summary:        List processing tools and functional utilities
License:        BSD-3-Clause
URL:            https://github.com/pytoolz/toolz
#!RemoteAsset:  sha256:27a5c770d068c110d9ed9323f24f1543e83b2f300a687b7891c1a6d56b697b5b
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} tlz
# skip tests: toolz.compatibility raises DeprecationWarning
BuildOption(check):  -e 'toolz.tests.test_compatibility'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-git-versioning)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Toolz provides a set of utility functions for iterators, functions, and
dictionaries. These functions interoperate well and form the building blocks
of common data analytic operations. They extend the standard library modules
itertools and functools.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt

%changelog
%autochangelog
