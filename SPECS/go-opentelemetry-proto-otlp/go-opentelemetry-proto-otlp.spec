# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           otlp
%define go_import_path  go.opentelemetry.io/proto/otlp

Name:           go-opentelemetry-proto-otlp
Version:        1.10.0
Release:        %autorelease
Summary:        OpenTelemetry protocol protobuf module for Go
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-proto-go
#!RemoteAsset:  sha256:0fc8783b5b46d393a0d0f9328f5c78797601d751e9df051e4b09fed31fb8b601
Source0:        https://github.com/open-telemetry/opentelemetry-proto-go/archive/refs/tags/otlp/v1.10.0.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n opentelemetry-proto-go-otlp-v1.10.0/otlp
# The import path is a Go module below the repository root; keep %check scoped
# to this module so GOPATH-mode tests do not scan sibling modules from the archive.
%define go_test_include %{go_import_path}

BuildRequires:  go
BuildRequires:  go(github.com/grpc-ecosystem/grpc-gateway/v2)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(google.golang.org/genproto/googleapis/api)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go-rpm-macros

Provides:       go(go.opentelemetry.io/proto/otlp) = %{version}
Provides:       go(go.opentelemetry.io/proto/otlp/common/v1) = %{version}

Requires:       go(github.com/grpc-ecosystem/grpc-gateway/v2)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/text)
Requires:       go(google.golang.org/genproto/googleapis/api)
Requires:       go(google.golang.org/genproto/googleapis/rpc)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)

%description
This package provides OpenTelemetry protocol protobuf module for Go.

%files
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
