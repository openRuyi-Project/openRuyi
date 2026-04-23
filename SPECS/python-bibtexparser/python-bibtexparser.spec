# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname bibtexparser

Name:           python-%{srcname}
Version:        1.4.4
Release:        %autorelease
Summary:        A BibTeX parsing library
License:        BSD-3-Clause OR LGPL-3.0-or-later
URL:            https://github.com/sciunto-org/python-bibtexparser
#!RemoteAsset:  sha256:093b6c824f7a71d3a748867c4057b71f77c55b8dbc07efc993b781771520d8fb
Source0:        https://files.pythonhosted.org/packages/source/b/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pyparsing)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
BibtexParser is a python library to parse BibTeX files. The code relies
on pyparsing and is tested with unit tests.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license COPYING

%changelog
%autochangelog
