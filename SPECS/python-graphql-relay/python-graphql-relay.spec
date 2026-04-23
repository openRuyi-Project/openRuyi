# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname graphql-relay
%global pypi_name graphql_relay

Name:           python-%{srcname}
Version:        3.2.0
Release:        %autorelease
Summary:        A library to help construct a graphql-py server supporting react-relay
License:        MIT
URL:            https://github.com/graphql-python/graphql-relay-py
#!RemoteAsset:  sha256:1ff1c51298356e481a0be009ccdff249832ce53f30559c1338f22a0e0d17250c
Source0:        https://files.pythonhosted.org/packages/source/g/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name} -L

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
GraphQL-relay-py is the Relay library for GraphQL-core.
It allows the easy creation of Relay-compliant servers using GraphQL-core.

%prep -a
sed -i 's/poetry_core>=1,<2/poetry-core/g; s/setuptools>=59,<70/setuptools/g' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
