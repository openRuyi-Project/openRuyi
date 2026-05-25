# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           sdk
%define go_import_path  go.opentelemetry.io/auto/sdk
%define go_source_subdir sdk
# The sdk tag archive is the repository root; the explicit %install/%check
# sections below enter %{go_source_subdir} so only the sdk module is packaged. - HNO3Miracle
%define go_test_include %{go_import_path}

Name:           go-opentelemetry-auto-sdk
Version:        1.2.1
Release:        %autorelease
Summary:        Instrumentation SDK for OpenTelemetry Go
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-go-instrumentation
#!RemoteAsset:  sha256:7556703696704f18af8de85e4b545cd7e92329ecfd98d11bf4bcb700497d9192
Source0:        https://github.com/open-telemetry/opentelemetry-go-instrumentation/archive/refs/tags/sdk/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/kr/pretty)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/rogpeppe/go-internal)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.opentelemetry.io/otel/trace)
BuildRequires:  go(gopkg.in/check.v1)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go-rpm-macros

Provides:       go(go.opentelemetry.io/auto/sdk) = %{version}

Requires:       go(go.opentelemetry.io/otel)

%description
This package provides the Go library go.opentelemetry.io/auto/sdk.

%install
pushd %{go_source_subdir}
%buildsystem_golangmodules_install
popd

%check
pushd %{go_source_subdir}
%buildsystem_golangmodules_check
popd

%files
%doc CONTRIBUTING.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
