# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name             otlptrace
%define go_import_path    go.opentelemetry.io/otel/exporters/otlp/otlptrace
%define otlp_import_path  go.opentelemetry.io/otel/exporters/otlp

Name:           go-opentelemetry-otel-exporters-otlp-otlptrace
Version:        1.46.0
Release:        %autorelease
Summary:        OTLP trace, metric, and log exporters for OpenTelemetry Go
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-go
#!RemoteAsset:  sha256:5da7830e37741e46606c10b65f15f16481c2c7f83ee31bb8e833d76376f6331b
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
BuildRequires:  go(go.opentelemetry.io/otel/log)
BuildRequires:  go(go.opentelemetry.io/otel/metric)
BuildRequires:  go(go.opentelemetry.io/otel/sdk)
BuildRequires:  go(go.opentelemetry.io/otel/sdk/log)
BuildRequires:  go(go.opentelemetry.io/otel/sdk/log/logtest)
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
# The same upstream snapshot contains the metric and experimental log modules.
Provides:       go(%{otlp_import_path}/otlplog/otlploggrpc) = 0.22.0
Provides:       go(%{otlp_import_path}/otlplog/otlploghttp) = 0.22.0
Provides:       go(%{otlp_import_path}/otlpmetric/otlpmetricgrpc) = %{version}
Provides:       go(%{otlp_import_path}/otlpmetric/otlpmetrichttp) = %{version}

Requires:       go(github.com/cenkalti/backoff/v5)
Requires:       go(github.com/go-logr/logr)
Requires:       go(github.com/grpc-ecosystem/grpc-gateway/v2)
Requires:       go(go.opentelemetry.io/auto/sdk)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(go.opentelemetry.io/otel/log)
Requires:       go(go.opentelemetry.io/otel/metric)
Requires:       go(go.opentelemetry.io/otel/sdk)
Requires:       go(go.opentelemetry.io/otel/sdk/log)
Requires:       go(go.opentelemetry.io/otel/sdk/metric)
Requires:       go(go.opentelemetry.io/otel/trace)
Requires:       go(go.opentelemetry.io/proto)
Requires:       go(google.golang.org/genproto/googleapis/rpc)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)

%description
OTLP trace exporter abstractions and gRPC and HTTP exporters for OpenTelemetry
Go traces, metrics, and logs.

%install
# Core otel excludes these modules; this RPM owns all OTLP exporters together.
install -d %{buildroot}%{go_sys_gopath}/%{otlp_import_path}/otlplog
install -d %{buildroot}%{go_sys_gopath}/%{otlp_import_path}/otlpmetric
cp -a exporters/otlp/otlplog/otlploggrpc exporters/otlp/otlplog/otlploghttp \
    %{buildroot}%{go_sys_gopath}/%{otlp_import_path}/otlplog/
cp -a exporters/otlp/otlpmetric/otlpmetricgrpc exporters/otlp/otlpmetric/otlpmetrichttp \
    %{buildroot}%{go_sys_gopath}/%{otlp_import_path}/otlpmetric/
cp -a exporters/otlp/otlptrace %{buildroot}%{go_sys_gopath}/%{otlp_import_path}/

%check
export GO111MODULE=off
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
mkdir -p %{_builddir}/go/src/go.opentelemetry.io
cp -a . %{_builddir}/go/src/go.opentelemetry.io/otel
# GOPATH discovery covers all seven modules, including nested HTTP/gRPC tests.
cd %{_builddir}/go/src/%{otlp_import_path}
go test -v ./...

%files
%license LICENSE
%{go_sys_gopath}/%{go_import_path}
%{go_sys_gopath}/%{otlp_import_path}/otlplog/otlploggrpc
%{go_sys_gopath}/%{otlp_import_path}/otlplog/otlploghttp
%{go_sys_gopath}/%{otlp_import_path}/otlpmetric/otlpmetricgrpc
%{go_sys_gopath}/%{otlp_import_path}/otlpmetric/otlpmetrichttp

%changelog
%autochangelog
