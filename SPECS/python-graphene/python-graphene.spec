# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname graphene

Name:           python-%{srcname}
Version:        3.4.3
Release:        %autorelease
Summary:        GraphQL framework for Python
License:        MIT
URL:            https://graphene-python.org/
VCS:            git:https://github.com/graphql-python/graphene.git
#!RemoteAsset:  sha256:2a3786948ce75fe7e078443d37f609cbe5bb36ad8d6b828740ad3b95ed1a0aaa
Source0:        https://files.pythonhosted.org/packages/source/g/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Graphene is an opinionated Python library
for building GraphQL schemas/types fast and easily.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
