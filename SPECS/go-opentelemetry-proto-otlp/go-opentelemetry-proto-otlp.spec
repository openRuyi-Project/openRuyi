# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           proto-otlp
%define go_import_path  go.opentelemetry.io/proto/otlp
%define go_source_subdir otlp
# The collector gateway bindings import grpc-gateway, whose dependency chain
# cycles back to this OTLP module through envoyproxy/go-control-plane. Package
# the core protobuf types here and leave collector bindings for a later split. - HNO3Miracle
%define go_test_include %{shrink:
    %{go_import_path}/common/v1
    %{go_import_path}/logs/v1
    %{go_import_path}/metrics/v1
    %{go_import_path}/profiles/v1development
    %{go_import_path}/resource/v1
    %{go_import_path}/trace/v1
}

Name:           go-opentelemetry-proto-otlp
Version:        1.10.0
Release:        %autorelease
Summary:        OpenTelemetry protocol protobuf module for Go
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-proto-go
#!RemoteAsset:  sha256:0fc8783b5b46d393a0d0f9328f5c78797601d751e9df051e4b09fed31fb8b601
Source0:        https://github.com/open-telemetry/opentelemetry-proto-go/archive/refs/tags/otlp/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go-rpm-macros

Provides:       go(go.opentelemetry.io/proto/otlp) = %{version}

Requires:       go(google.golang.org/protobuf)

%description
This package provides OpenTelemetry protocol protobuf module for Go.

%install
pushd %{go_source_subdir}
%buildsystem_golangmodules_install
popd

%check
pushd %{go_source_subdir}
%buildsystem_golangmodules_check
popd

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}
%exclude %{go_sys_gopath}/%{go_import_path}/collector*

%changelog
%autochangelog
