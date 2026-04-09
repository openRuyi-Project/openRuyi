# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           proto
%define go_import_path  go.opentelemetry.io/proto

Name:           go-opentelemetry-proto
Version:        1.9.0
Release:        %autorelease
Summary:        Generated code for OpenTelemetry protobuf data model
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-proto-go
#!RemoteAsset
Source0:        https://github.com/open-telemetry/opentelemetry-proto-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(github.com/grpc-ecosystem/grpc-gateway)

Provides:       go(go.opentelemetry.io/proto) = %{version}

%description
Generated Go code for the OpenTelemetry protobuf data model.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
