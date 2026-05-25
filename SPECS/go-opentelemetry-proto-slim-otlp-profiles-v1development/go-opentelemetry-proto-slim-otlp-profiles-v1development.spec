# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           proto-slim-otlp-profiles-v1development
%define go_import_path  go.opentelemetry.io/proto/slim/otlp/profiles/v1development
# Keep %check scoped to this module so GOPATH-mode tests do not scan sibling
# modules from the archive. - HNO3Miracle
%define go_test_include %{go_import_path}

Name:           go-opentelemetry-proto-slim-otlp-profiles-v1development
Version:        0.3.0
Release:        %autorelease
Summary:        Slim OTLP profile protobufs for Go
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-proto-go
#!RemoteAsset:  sha256:0761255324a3924f5ca7a42de22b1da5d013c54a1d7295492c3d8a73526d6913
Source0:        https://github.com/open-telemetry/opentelemetry-proto-go/archive/refs/tags/slim/otlp/profiles/v1development/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go(go.opentelemetry.io/proto/slim/otlp)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go-rpm-macros

Provides:       go(go.opentelemetry.io/proto/slim/otlp/profiles/v1development) = %{version}

Requires:       go(go.opentelemetry.io/proto/slim/otlp)
Requires:       go(google.golang.org/protobuf)

%description
This package provides the Go library go.opentelemetry.io/proto/slim/otlp/profiles/v1development.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
