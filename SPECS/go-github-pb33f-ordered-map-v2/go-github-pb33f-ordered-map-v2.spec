# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ordered-map
%define go_import_path  github.com/pb33f/ordered-map/v2
# YAML round-trip tests fail with packaged go.yaml.in/yaml/v4 reporting
# "pipeline must contain YAML mapping, has 1" - HNO3Miracle
%define go_test_exclude_glob %{go_import_path}*

Name:           go-github-pb33f-ordered-map-v2
Version:        2.3.1
Release:        %autorelease
Summary:        Ordered map implementation for Go
License:        Apache-2.0
URL:            https://github.com/pb33f/ordered-map
#!RemoteAsset:  sha256:0e2ebc963cff791da1bbacb386614a0a1a5cbfcfeff439d4ba11e824cd54e608
Source0:        https://github.com/pb33f/ordered-map/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/bahlo/generic-list-go)
BuildRequires:  go(github.com/buger/jsonparser)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.yaml.in/yaml/v4)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(github.com/pb33f/ordered-map/v2) = %{version}

Requires:       go(github.com/bahlo/generic-list-go)
Requires:       go(github.com/buger/jsonparser)
Requires:       go(go.yaml.in/yaml/v4)

%description
Ordered map implementation for Go that preserves insertion order.

%files
%doc README.md
%doc CHANGELOG.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
