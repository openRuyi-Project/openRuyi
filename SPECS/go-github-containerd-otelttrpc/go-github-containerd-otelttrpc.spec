# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           otelttrpc
%define go_import_path  github.com/containerd/otelttrpc

Name:           go-github-containerd-otelttrpc
Version:        0.1.0
Release:        %autorelease
Summary:        Package otelttrpc implements Opentelemetry instrumentation support for ttRPC
License:        Apache-2.0
URL:            https://github.com/containerd/otelttrpc
#!RemoteAsset:  sha256:bb499eb9dd84538da195b75453896780d29238f0956fa801546d628f81f0bf97
Source0:        https://github.com/containerd/otelttrpc/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/containerd/ttrpc)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/otel/metric)
BuildRequires:  go(go.opentelemetry.io/otel/sdk)
BuildRequires:  go(go.opentelemetry.io/otel/trace)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(github.com/containerd/otelttrpc) = %{version}

Requires:       go(github.com/containerd/ttrpc)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(go.opentelemetry.io/otel/metric)
Requires:       go(go.opentelemetry.io/otel/sdk)
Requires:       go(go.opentelemetry.io/otel/trace)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)

%description
This golang package implements OpenTelemetry instrumentation support for
ttrpc. It can be used to automatically generate OpenTelemetry trace
spans for RPC methods called on the ttrpc client side and served on the
ttrpc server side.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
