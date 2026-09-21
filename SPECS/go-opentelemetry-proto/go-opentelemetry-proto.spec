# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           proto
%define go_import_path  go.opentelemetry.io/proto/otlp
%define go_source_subdir otlp

Name:           go-opentelemetry-proto
Version:        1.9.0
Release:        %autorelease
Summary:        Generated code for OpenTelemetry protobuf data model
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-proto-go
#!RemoteAsset:  sha256:87b9d9dab8f5f4ceae467fe7c277cac4804621d052e39b82c06ff96b54c9961e
Source0:        https://github.com/open-telemetry/opentelemetry-proto-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/grpc-ecosystem/grpc-gateway/v2)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(go.opentelemetry.io/proto/otlp) = %{version}
# Compatibility provide for existing consumers of the historical package.
Provides:       go(go.opentelemetry.io/proto) = %{version}

Requires:       go(github.com/grpc-ecosystem/grpc-gateway/v2)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)

%description
Generated Go code for the OpenTelemetry protobuf data model.

%install
pushd %{go_source_subdir}
%buildsystem_golangmodules_install
popd

%check
pushd %{go_source_subdir}
%buildsystem_golangmodules_check
popd

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
