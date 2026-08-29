# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname marisa-trie
%global pypi_name marisa_trie

Name:           python-%{srcname}
Version:        1.3.1
Release:        %autorelease
Summary:        Static memory-efficient Trie-like structures for Python
License:        MIT
URL:            https://github.com/pytries/marisa-trie
#!RemoteAsset:  sha256:97107fd12f30e4f8fea97790343a2d2d9a79d93697fe14e1b6f6363c984ff85b
Source0:        https://files.pythonhosted.org/packages/source/m/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(cython)
BuildRequires:  gcc-c++

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Static memory-efficient Trie-like structures for Python (based on marisa-trie C++ library).

String data in a MARISA-trie may take up to 50x-100x less space than in a standard
Python dict; the raw lookup speed is comparable; trie also provides fast advanced
methods like prefix search.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
