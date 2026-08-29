# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname roman-numerals
%global pypi_name roman_numerals

Name:           python-%{srcname}
Version:        4.1.0
Release:        %autorelease
Summary:        Manipulate well-formed Roman numerals
License:        0BSD OR CC0-1.0
URL:            https://github.com/AA-Turner/roman-numerals
VCS:            git:https://github.com/AA-Turner/roman-numerals.git
#!RemoteAsset:  sha256:1af8b147eb1405d5839e78aeb93131690495fe9da5c91856cb33ad55a7f1e5b2
Source0:        https://files.pythonhosted.org/packages/source/r/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name} +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
A library for manipulating well-formed Roman numerals.  Roman numerals
between 1 and 3,999 (inclusive) are supported, and arithmetic operations
between numerals as well as conversion to and from integers are
provided.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENCE.rst

%changelog
%autochangelog
