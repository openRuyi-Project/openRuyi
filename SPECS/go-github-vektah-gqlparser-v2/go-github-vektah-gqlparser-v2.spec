# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gqlparser
%define go_import_path  github.com/vektah/gqlparser/v2

Name:           go-github-vektah-gqlparser-v2
Version:        2.5.27
Release:        %autorelease
Summary:        GraphQL parser for Go
License:        MIT
URL:            https://github.com/vektah/gqlparser
#!RemoteAsset:  sha256:ab9b96b82d1b46319a7aa5eedac78cadf867aaaf1d081926e32fb1eb34fbd1ca
Source0:        https://github.com/vektah/gqlparser/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/agnivade/levenshtein)
BuildRequires:  go(github.com/andreyvit/diff)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(github.com/vektah/gqlparser/v2) = %{version}

Requires:       go(github.com/agnivade/levenshtein)
Requires:       go(github.com/andreyvit/diff)
Requires:       go(gopkg.in/yaml.v3)

%description
gqlparser is a GraphQL parser for Go that closely follows the graphql-js reference implementation.

%files
%doc readme.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
