# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           anthropic-sdk-go
%define go_import_path  github.com/anthropics/anthropic-sdk-go
# Root package tests require a local Prism mock server on localhost:4010.
%define go_test_exclude %{go_import_path}

Name:           go-github-anthropics-anthropic-sdk-go
Version:        1.26.0
Release:        %autorelease
Summary:        Go library for accessing the Anthropic REST API
License:        MIT
URL:            https://github.com/anthropics/anthropic-sdk-go
#!RemoteAsset:  sha256:bb12620d3824dbc573fa6b9f461aee10938bc1fe523e78e90a43248703d23cfb
Source0:        https://github.com/anthropics/anthropic-sdk-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/aws/aws-sdk-go-v2)
BuildRequires:  go(github.com/aws/smithy-go)
BuildRequires:  go(github.com/dnaeon/go-vcr)
BuildRequires:  go(github.com/invopop/jsonschema)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/tidwall/gjson)
BuildRequires:  go(github.com/tidwall/sjson)
BuildRequires:  go(golang.org/x/oauth2)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(google.golang.org/api/option)
BuildRequires:  go(google.golang.org/api/transport)

Provides:       go(github.com/anthropics/anthropic-sdk-go) = %{version}

Requires:       go(github.com/aws/aws-sdk-go-v2)
Requires:       go(github.com/aws/smithy-go)
Requires:       go(github.com/dnaeon/go-vcr)
Requires:       go(github.com/invopop/jsonschema)
Requires:       go(github.com/tidwall/gjson)
Requires:       go(github.com/tidwall/sjson)
Requires:       go(golang.org/x/oauth2)
Requires:       go(golang.org/x/sync)
Requires:       go(google.golang.org/api/option)
Requires:       go(google.golang.org/api/transport)

%description
The Anthropic Go library provides convenient access to the Anthropic REST API from applications written in Go.

%files
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
