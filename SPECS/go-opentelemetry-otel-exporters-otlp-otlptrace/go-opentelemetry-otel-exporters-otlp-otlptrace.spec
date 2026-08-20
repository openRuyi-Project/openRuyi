# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           otlptrace
%define go_import_path  go.opentelemetry.io/otel/exporters/otlp/otlptrace

Name:           go-opentelemetry-otel-exporters-otlp-otlptrace
Version:        1.43.0
Release:        %autorelease
Summary:        OTLP trace exporter abstractions for OpenTelemetry Go
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-go
#!RemoteAsset:  sha256:971b31afdf0b97356433390927df0ac7f16220a625468b9259d3762e87084899
Source0:        https://github.com/open-telemetry/opentelemetry-go/archive/refs/tags/exporters/otlp/otlptrace/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/cenkalti/backoff/v5)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.opentelemetry.io/otel/metric)
BuildRequires:  go(go.opentelemetry.io/otel/sdk)
BuildRequires:  go(go.opentelemetry.io/otel/sdk/metric)
BuildRequires:  go(go.opentelemetry.io/otel/trace)
BuildRequires:  go(go.opentelemetry.io/proto)
BuildRequires:  go(go.uber.org/goleak)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(github.com/grpc-ecosystem/grpc-gateway/v2)

Provides:       go(go.opentelemetry.io/otel/exporters/otlp/otlptrace) = %{version}
Provides:       go(go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc) = %{version}
Provides:       go(go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp) = %{version}

Requires:       go(github.com/cenkalti/backoff/v5)
Requires:       go(github.com/go-logr/logr)
Requires:       go(github.com/grpc-ecosystem/grpc-gateway/v2)
Requires:       go(go.opentelemetry.io/auto/sdk)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(go.opentelemetry.io/otel/metric)
Requires:       go(go.opentelemetry.io/otel/sdk)
Requires:       go(go.opentelemetry.io/otel/sdk/metric)
Requires:       go(go.opentelemetry.io/otel/trace)
Requires:       go(go.opentelemetry.io/proto)
Requires:       go(google.golang.org/genproto/googleapis/rpc)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)

%description
OTLP trace exporter abstractions and gRPC and HTTP exporters for OpenTelemetry Go.

%install
# The parent source directory contains all three nested modules.
install -d %{buildroot}%{go_sys_gopath}/%{go_import_path}
cp -a exporters/otlp/otlptrace/. %{buildroot}%{go_sys_gopath}/%{go_import_path}/

%check
export GO111MODULE=off
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
mkdir -p %{_builddir}/go/src/go.opentelemetry.io
cp -a . %{_builddir}/go/src/go.opentelemetry.io/otel
cd %{_builddir}/go/src/%{go_import_path}
go test -v ./...

%files
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
