# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           shurcooL-graphql
%define go_import_path  github.com/cli/shurcooL-graphql

Name:           go-github-cli-shurcool-graphql
Version:        0.0.4
Release:        %autorelease
Summary:        GraphQL client implementation for Go
License:        MIT
URL:            https://github.com/cli/shurcooL-graphql
#!RemoteAsset:  sha256:05c6bb6bb17d663cd9bd133627c2a9ed718966a0963615abed6345f8321427fc
Source0:        https://github.com/cli/shurcooL-graphql/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/cli/shurcooL-graphql) = %{version}

%description
shurcooL-graphql provides a Go client for constructing and executing GraphQL
queries and mutations using typed structures.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
