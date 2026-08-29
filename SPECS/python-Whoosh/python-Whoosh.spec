# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname Whoosh

Name:           python-%{srcname}
Version:        2.7.4
Release:        %autorelease
Summary:        Pure-Python full text indexing, search, and spell checking library
License:        BSD-2-Clause
URL:            http://bitbucket.org/mchaput/whoosh
#!RemoteAsset:  sha256:7ca5633dbfa9e0e0fa400d3151a8a0c4bec53bd2ecedc0a67705b17565c31a83
Source0:        https://files.pythonhosted.org/packages/source/w/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  whoosh
BuildOption(check):  -e whoosh.filedb.gae
BuildOption(check):  -e whoosh.support.bench
BuildOption(check):  -e whoosh.automata.nfa

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Whoosh is a pure-Python indexing and search library. It can be used
to add search functionality to applications and websites. Every part
of how Whoosh works can be extended or replaced to meet specific
needs.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.txt
%license LICENSE.txt

%changelog
%autochangelog
