# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname text-unidecode

Name:           python-%{srcname}
Version:        1.3
Release:        %autorelease
Summary:        Python module to deal with unicode slugs
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://github.com/kmike/text-unidecode
#!RemoteAsset:  sha256:bad6603bb14d279193107714b288be206cac565dfa49aa5b105294dd5c4aab93
Source:         https://files.pythonhosted.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l text_unidecode

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
text-unidecode is the most basic port of the Text::Unidecode Perl library.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}

%changelog
%autochangelog
