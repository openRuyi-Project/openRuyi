# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           openai-go
%define go_import_path  github.com/openai/openai-go/v3
# Skip generated API tests that require network access, which the isolated
# OBS/CI build environment does not provide.
%define go_test_exclude %{shrink:
    github.com/openai/openai-go/v3
    github.com/openai/openai-go/v3/conversations
    github.com/openai/openai-go/v3/realtime
    github.com/openai/openai-go/v3/responses
}

Name:           go-github-openai-openai-go-v3
Version:        3.22.0
Release:        %autorelease
Summary:        Go client library for the OpenAI REST API
License:        Apache-2.0
URL:            https://github.com/openai/openai-go
#!RemoteAsset:  sha256:57be417b0904fc46e8d56f140bfb925adb8709f514a1d247974b8da4192a2ae1
Source0:        https://github.com/openai/openai-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/Azure/azure-sdk-for-go)
BuildRequires:  go(github.com/invopop/jsonschema)
BuildRequires:  go(github.com/tidwall/gjson)
BuildRequires:  go(github.com/tidwall/sjson)

Provides:       go(github.com/openai/openai-go/v3) = %{version}

Requires:       go(github.com/Azure/azure-sdk-for-go)
Requires:       go(github.com/invopop/jsonschema)
Requires:       go(github.com/tidwall/gjson)
Requires:       go(github.com/tidwall/sjson)

%description
The OpenAI Go library provides convenient access to the OpenAI REST API from
applications written in Go.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
