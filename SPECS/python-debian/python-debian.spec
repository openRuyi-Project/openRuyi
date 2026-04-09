# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global file_name python-debian

%global srcname debian

Name:           python-%{srcname}
Version:        1.0.1
Release:        %autorelease
Summary:        Modules for Debian-related data formats
License:        GPL-2.0-or-later AND GPL-3.0-or-later
URL:            https://salsa.debian.org/python-debian-team/python-debian
#!RemoteAsset
Source:         https://files.pythonhosted.org/packages/source/p/%{file_name}/%{file_name}-%{version}.tar.gz
BuildSystem:    pyproject

# set version to build.
Patch:          0001-fix-version.patch

BuildOption(install):  -l %{srcname} -L

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
# for tests.
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
This package provides Python modules that abstract many formats of Debian
related files. Currently handled are:
* Debtags information (debian.debtags module)
* debian/changelog (debian.changelog module)
* Packages files, pdiffs (debian.debian_support module)
* Control files of single or multiple RFC822-style paragraphs, e.g.
  debian/control, .changes, .dsc, Packages, Sources, Release, etc.
  (debian.deb822 module)
* Raw .deb and .ar files, with (read-only) access to contained
  files and meta-information

%generate_buildrequires
%pyproject_buildrequires

%check
# skip some tests as we don't have dpkg.
%pytest --ignore=src/debian/_arch_table.py

%files -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
