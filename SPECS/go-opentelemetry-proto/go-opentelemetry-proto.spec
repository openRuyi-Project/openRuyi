# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           proto
%define go_import_path  go.opentelemetry.io/proto

Name:           go-opentelemetry-proto
Version:        1.10.0
Release:        %autorelease
Summary:        Generated code for OpenTelemetry protobuf data model
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-proto-go
#!RemoteAsset:  sha256:2d39f83c69410c481293b005abfc2c2b259b1281179687099384aa948666d501
Source0:        https://github.com/open-telemetry/opentelemetry-proto-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/grpc-ecosystem/grpc-gateway/v2)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(go.opentelemetry.io/proto) = %{version}
Provides:       go(go.opentelemetry.io/proto/internal/tools) = %{version}
Provides:       go(go.opentelemetry.io/proto/otlp) = %{version}
Provides:       go(go.opentelemetry.io/proto/otlp/collector/profiles/v1development) = %{version}
Provides:       go(go.opentelemetry.io/proto/otlp/profiles/v1development) = %{version}
Provides:       go(go.opentelemetry.io/proto/slim/otlp) = %{version}
Provides:       go(go.opentelemetry.io/proto/slim/otlp/collector/profiles/v1development) = %{version}
Provides:       go(go.opentelemetry.io/proto/slim/otlp/profiles/v1development) = %{version}

Requires:       go(github.com/grpc-ecosystem/grpc-gateway/v2)
Requires:       go(google.golang.org/genproto/googleapis/rpc)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)

%description
Generated Go code for the OpenTelemetry protobuf data model.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
