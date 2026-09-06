# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-ordered-map
%define go_import_path  github.com/wk8/go-ordered-map/v2

Name:           go-github-wk8-go-ordered-map-v2
Version:        2.1.8
Release:        %autorelease
Summary:        Generic insertion-ordered map for Go
License:        Apache-2.0
URL:            https://github.com/wk8/go-ordered-map
#!RemoteAsset:  sha256:de9c9c67b7907d7a0714b4773585144aa0b4fdf7f36ab42d103cd2edc500eb20
Source0:        https://github.com/wk8/go-ordered-map/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/bahlo/generic-list-go)
BuildRequires:  go(github.com/buger/jsonparser)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/mailru/easyjson)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/bahlo/generic-list-go)
Requires:       go(github.com/buger/jsonparser)
Requires:       go(github.com/mailru/easyjson)
Requires:       go(gopkg.in/yaml.v3)

%description
Go-ordered-map provides a generic map that preserves insertion order and
supports JSON and YAML serialization.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
