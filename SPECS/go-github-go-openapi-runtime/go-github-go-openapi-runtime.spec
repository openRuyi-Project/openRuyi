# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           runtime
%define go_import_path  github.com/go-openapi/runtime

Name:           go-github-go-openapi-runtime
Version:        0.29.4
Release:        %autorelease
Summary:        Runtime client and server components for go-openapi
License:        Apache-2.0
URL:            https://github.com/go-openapi/runtime
#!RemoteAsset:  sha256:03bdf4c2e67a920ada0adfea67512b299af05c2f5b960d0a8d3020fd997c5c59
Source0:        https://github.com/go-openapi/runtime/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/docker/go-units)
BuildRequires:  go(github.com/go-openapi/analysis)
BuildRequires:  go(github.com/go-openapi/errors)
BuildRequires:  go(github.com/go-openapi/loads)
BuildRequires:  go(github.com/go-openapi/spec)
BuildRequires:  go(github.com/go-openapi/strfmt)
BuildRequires:  go(github.com/go-openapi/swag)
BuildRequires:  go(github.com/go-openapi/testify/v2)
BuildRequires:  go(github.com/go-openapi/validate)
BuildRequires:  go(github.com/opentracing/opentracing-go)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go(golang.org/x/sync)

Provides:       go(github.com/go-openapi/runtime) = %{version}

Requires:       go(github.com/docker/go-units)
Requires:       go(github.com/go-openapi/analysis)
Requires:       go(github.com/go-openapi/errors)
Requires:       go(github.com/go-openapi/loads)
Requires:       go(github.com/go-openapi/spec)
Requires:       go(github.com/go-openapi/strfmt)
Requires:       go(github.com/go-openapi/swag)
Requires:       go(github.com/go-openapi/testify/v2)
Requires:       go(github.com/go-openapi/validate)
Requires:       go(github.com/opentracing/opentracing-go)
Requires:       go(go.opentelemetry.io/auto/sdk)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(go.yaml.in/yaml/v3)
Requires:       go(golang.org/x/sync)

%description
Runtime provides client, server, middleware, authentication, content
negotiation, serialization, and tracing components for generated go-openapi
code.

%files
%doc README.md
%license LICENSE NOTICE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
