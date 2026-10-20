# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go.uuid
%define go_import_path  github.com/satori/go.uuid
%global commit_id b2ce2384e17bbe0c6d34077efa39dbab3e09123b

Name:           go-github-satori-go.uuid
Version:        1.2.0+git20261020.b2ce238
Release:        %autorelease
Summary:        UUID generation and parsing for Go
License:        MIT
URL:            https://github.com/satori/go.uuid
#!RemoteAsset:  sha256:4fdef9b17d3d51e1c81207b7b8862098262d955d27924240cea7b37c1d7c23ad
Source0:        https://github.com/satori/go.uuid/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(gopkg.in/check.v1)

Provides:       go(github.com/satori/go.uuid) = %{version}

%description
This package implements UUID generation and parsing in Go, including UUID
versions 1 through 5.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
