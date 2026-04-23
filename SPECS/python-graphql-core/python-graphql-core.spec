# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname graphql-core
%global pypi_name graphql_core

Name:           python-%{srcname}
Version:        3.2.8
Release:        %autorelease
Summary:        A Python 3 port of the GraphQL.js reference implementation of GraphQL
License:        MIT
URL:            https://github.com/graphql-python/graphql-core
#!RemoteAsset:  sha256:015457da5d996c924ddf57a43f4e959b0b94fb695b85ed4c29446e508ed65cf3
Source0:        https://files.pythonhosted.org/packages/source/g/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l graphql -L

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
GraphQL-core 3 is a Python 3.7+ port of GraphQL.js,
the JavaScript reference implementation for GraphQL,
a query language for APIs created by Facebook.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
