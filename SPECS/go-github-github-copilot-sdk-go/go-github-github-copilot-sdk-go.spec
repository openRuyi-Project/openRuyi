# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go
%define go_import_path  github.com/github/copilot-sdk/go
%define go_source_subdir go
%define go_test_exclude %{go_import_path}/internal/e2e

Name:           go-github-github-copilot-sdk-go
Version:        0.2.0
Release:        %autorelease
Summary:        Copilot CLI SDK for Go
License:        MIT
URL:            https://github.com/github/copilot-sdk
#!RemoteAsset:  sha256:741aa936b9a3aee71b8e1b4d1556a15dbdb61c98da754ea1774102533c4dd3b7
Source0:        https://github.com/github/copilot-sdk/archive/refs/tags/go/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n copilot-sdk-go-v%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/jsonschema-go)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.opentelemetry.io/otel/trace)

Provides:       go(github.com/github/copilot-sdk/go) = %{version}

Requires:       go(github.com/google/jsonschema-go)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/klauspost/compress)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(go.opentelemetry.io/otel/trace)

%description
A Go SDK for programmatic access to the GitHub Copilot CLI.

%prep -a
rm -rf go/samples

%install
pushd %{go_source_subdir}
%buildsystem_golangmodules_install
popd

%check
pushd %{go_source_subdir}
%buildsystem_golangmodules_check
popd

%files
%doc go/README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
