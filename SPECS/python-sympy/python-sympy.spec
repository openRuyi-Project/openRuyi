# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname sympy

Name:           python-%{srcname}
Version:        1.14.0
Release:        %autorelease
Summary:        A Python library for symbolic mathematics
License:        BSD-3-Clause AND MIT
URL:            https://www.sympy.org
#!RemoteAsset:  sha256:d3d3fe8df1e5a0b42f0e7bdf50541697dbe7d23746e894990c030e2b05e72517
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  isympy sympy
# We don't have python3dist(pyglet)
BuildOption(check):  -e 'sympy.plotting.pygletplot.*'
# And some upstream related errors.
BuildOption(check):  -e sympy.galgebra

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(mpmath)
BuildRequires:  python3dist(hypothesis)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)

Recommends:     python3dist(scipy)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
SymPy aims to become a full-featured computer algebra system (CAS) while
keeping the code as simple as possible in order to be comprehensible and
easily extensible.  SymPy is written entirely in Python and does not require
any external libraries.

%files -f %{pyproject_files}
%doc AUTHORS README.md
%{_bindir}/isympy
%{_mandir}/man1/isympy.1*

%changelog
%autochangelog
