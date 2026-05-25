# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           otlp
%define go_import_path  go.opentelemetry.io/proto/slim/otlp

Name:           go-opentelemetry-proto-slim-otlp
Version:        1.10.0
Release:        %autorelease
Summary:        Go library for go.opentelemetry.io/proto/slim/otlp
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-proto-go
#!RemoteAsset:  sha256:a45f9695391b26e304a1d9d54abf8effbfb6d5866c07ca48243680beb1abfcbc
Source0:        https://github.com/open-telemetry/opentelemetry-proto-go/archive/refs/tags/slim/otlp/v1.10.0.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n opentelemetry-proto-go-slim-otlp-v1.10.0/slim/otlp
# The import path is a Go module below the repository root; keep %check scoped
# to this module so GOPATH-mode tests do not scan sibling modules from the archive.
%define go_test_include %{go_import_path}

BuildRequires:  go
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go-rpm-macros

Provides:       go(go.opentelemetry.io/proto/slim/otlp) = %{version}
Provides:       go(go.opentelemetry.io/proto/slim/otlp/common/v1) = %{version}
Provides:       go(go.opentelemetry.io/proto/slim/otlp/resource/v1) = %{version}

Requires:       go(google.golang.org/protobuf)

%description
This package provides the Go library go.opentelemetry.io/proto/slim/otlp.

%files
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
