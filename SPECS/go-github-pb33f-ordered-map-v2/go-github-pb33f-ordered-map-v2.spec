# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ordered-map
%define go_import_path  github.com/pb33f/ordered-map/v2

Name:           go-github-pb33f-ordered-map-v2
Version:        2.3.1
Release:        %autorelease
Summary:        Optimal implementation of ordered maps for Golang - ie maps that remember the order in which keys were inserted.
License:        Apache-2.0
URL:            https://github.com/pb33f/ordered-map
#!RemoteAsset:  sha256:0e2ebc963cff791da1bbacb386614a0a1a5cbfcfeff439d4ba11e824cd54e608
Source0:        https://github.com/pb33f/ordered-map/archive/refs/tags/v2.3.1.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n ordered-map-2.3.1
# With packaged go.yaml.in/yaml/v4, YAML round-trip tests fail with
# "pipeline must contain YAML mapping, has 1"; keep the rest of %check enabled.
BuildOption(check):  -skip TestYAMLRoundTrip

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/bahlo/generic-list-go)
BuildRequires:  go(github.com/buger/jsonparser)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/stretchr/testify/assert)
BuildRequires:  go(github.com/stretchr/testify/require)
BuildRequires:  go(go.yaml.in/yaml/v4)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(github.com/pb33f/ordered-map/v2) = %{version}

Requires:       go(github.com/bahlo/generic-list-go)
Requires:       go(github.com/buger/jsonparser)
Requires:       go(go.yaml.in/yaml/v4)


%description
Ordered Maps

This repo was forked from wk8/go-ordered-map (https://github.com/wk8/go-
ordered-map) because of this:
(https://github.com/pb33f/libopenapi/issues/446)

The easyjson (https://github.com/mailru/easyjson) library which the
wk8/go-ordered-map project depends on is now considered a **security
risk** to pb33f.

So we forked it and removed the dependency on easyjson.

%files
%doc README.md
%doc CHANGELOG.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
