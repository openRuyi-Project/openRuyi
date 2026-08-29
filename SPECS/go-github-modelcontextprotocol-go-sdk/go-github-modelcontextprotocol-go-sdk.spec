# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-sdk
%define go_import_path  github.com/modelcontextprotocol/go-sdk

Name:           go-github-modelcontextprotocol-go-sdk
Version:        1.6.1
Release:        %autorelease
Summary:        Official Go SDK for the Model Context Protocol
License:        Apache-2.0 AND MIT AND CC-BY-4.0
URL:            https://github.com/modelcontextprotocol/go-sdk
VCS:            git:https://github.com/modelcontextprotocol/go-sdk.git
#!RemoteAsset:  sha256:a161e098e8fbcd4bede636837c6e2665eba6ef39b87436c19973e3584aaaf9bd
Source0:        https://github.com/modelcontextprotocol/go-sdk/archive/refs/tags/v%{version}.tar.gz#/go-sdk-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n go-sdk-%{version}
# Skip OAuth resource metadata test: expected success endpoint returns HTTP 404.
BuildOption(check):  -skip TestGetProtectedResourceMetadata

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/golang-jwt/jwt/v5)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/jsonschema-go)
BuildRequires:  go(github.com/segmentio/encoding)
BuildRequires:  go(github.com/yosida95/uritemplate/v3)
BuildRequires:  go(golang.org/x/oauth2)
BuildRequires:  go(golang.org/x/time)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/modelcontextprotocol/go-sdk) = %{version}

Requires:       go(github.com/google/jsonschema-go)
Requires:       go(github.com/segmentio/encoding)
Requires:       go(github.com/yosida95/uritemplate/v3)
Requires:       go(golang.org/x/oauth2)
Requires:       go(golang.org/x/time)

%description
The Model Context Protocol Go SDK provides client and server APIs for building
MCP integrations in Go.

%check -p
# synctest requires the modern timer channel implementation under GOPATH mode.
export GODEBUG=asynctimerchan=0

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
