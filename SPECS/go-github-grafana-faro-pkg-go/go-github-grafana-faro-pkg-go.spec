# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           faro
%define go_import_path  github.com/grafana/faro/pkg/go
%define commit_id       bb5f9417df83f79eb88449cff5ab1b7ca65531f4

Name:           go-github-grafana-faro-pkg-go
Version:        0+git20260819.bb5f941
Release:        %autorelease
Summary:        Go models for Grafana Faro telemetry
License:        Apache-2.0
URL:            https://github.com/grafana/faro
#!RemoteAsset:  sha256:b6e76f4aa0fef747e393bc8430fc9f2912f354e7161244ac1a959ee3206d2a82
Source0:        https://github.com/grafana/faro/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules
BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/apapsch/go-jsonmerge/v2)
BuildRequires:  go(github.com/gogo/protobuf)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/json-iterator/go)
BuildRequires:  go(github.com/modern-go/concurrent)
BuildRequires:  go(github.com/modern-go/reflect2)
BuildRequires:  go(github.com/oapi-codegen/runtime)
BuildRequires:  go(go.opentelemetry.io/collector)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/oapi-codegen/runtime)
Requires:       go(go.opentelemetry.io/collector)

%description
This package provides generated Go models and OpenTelemetry conversion code
for Grafana Faro frontend telemetry.

%install
pushd pkg/go
%buildsystem_golangmodules_install
popd

%check
pushd pkg/go
%buildsystem_golangmodules_check
popd

%files
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
