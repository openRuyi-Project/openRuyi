# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname language_data

Name:           python-language-data
Version:        1.4.0
Release:        %autorelease
Summary:        Library for language data
License:        MIT
URL:            https://github.com/rspeer/language_data
#!RemoteAsset:  sha256:800e6457e7beda781c156e02d7707e38db2ded026472e07e2c055dc8446ee574
Source0:        https://files.pythonhosted.org/packages/source/l/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(marisa-trie)

Provides:       python3-language-data = %{version}-%{release}
%python_provide python3-language-data

%description
This package provides language data and functions for working with it.
It is a dependency for other libraries like langcodes.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
