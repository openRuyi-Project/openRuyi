# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-ordered-map
%define go_import_path  github.com/wk8/go-ordered-map/v2

Name:           go-github-wk8-go-ordered-map-v2
Version:        2.1.8
Release:        %autorelease
Summary:        Optimal implementation of ordered maps for Golang - ie maps that remember the order in which keys were inserted.
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
BuildRequires:  go(github.com/mailru/easyjson)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(github.com/wk8/go-ordered-map/v2) = %{version}

Requires:       go(github.com/bahlo/generic-list-go)
Requires:       go(github.com/buger/jsonparser)
Requires:       go(github.com/mailru/easyjson)
Requires:       go(github.com/stretchr/testify)
Requires:       go(gopkg.in/yaml.v3)

%description
go-ordered-map is a generic ordered map for Go that preserves insertion order.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
