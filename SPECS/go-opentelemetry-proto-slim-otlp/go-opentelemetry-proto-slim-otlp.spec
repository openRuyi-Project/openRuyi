# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           proto-slim-otlp
%define go_import_path  go.opentelemetry.io/proto/slim/otlp
# Keep %check scoped to this module so GOPATH-mode tests do not scan sibling
# modules from the archive. - HNO3Miracle
%define go_test_include %{go_import_path}

Name:           go-opentelemetry-proto-slim-otlp
Version:        1.10.0
Release:        %autorelease
Summary:        Slim OpenTelemetry protocol protobufs for Go
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-proto-go
#!RemoteAsset:  sha256:a45f9695391b26e304a1d9d54abf8effbfb6d5866c07ca48243680beb1abfcbc
Source0:        https://github.com/open-telemetry/opentelemetry-proto-go/archive/refs/tags/slim/otlp/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go-rpm-macros

Provides:       go(go.opentelemetry.io/proto/slim/otlp) = %{version}

Requires:       go(google.golang.org/protobuf)

%description
This package provides the Go library go.opentelemetry.io/proto/slim/otlp.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
