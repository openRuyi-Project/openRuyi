# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           sdk
%define go_import_path  go.opentelemetry.io/auto

Name:           go-opentelemetry-auto-sdk
Version:        1.2.1
Release:        %autorelease
Summary:        Go library for go.opentelemetry.io/auto/sdk
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-go-instrumentation
#!RemoteAsset:  sha256:7556703696704f18af8de85e4b545cd7e92329ecfd98d11bf4bcb700497d9192
Source0:        https://github.com/open-telemetry/opentelemetry-go-instrumentation/archive/refs/tags/sdk/v1.2.1.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n opentelemetry-go-instrumentation-sdk-v1.2.1
# go.opentelemetry.io/auto/sdk imports go.opentelemetry.io/auto/internal/...
# from the repository root, so install the full source tree but keep %check
# scoped to the public sdk module.
%define go_test_include go.opentelemetry.io/auto/sdk

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
Provides:       go(go.opentelemetry.io/auto/sdk/internal/telemetry) = %{version}

Requires:       go(github.com/davecgh/go-spew)
Requires:       go(github.com/kr/pretty)
Requires:       go(github.com/pmezard/go-difflib)
Requires:       go(github.com/rogpeppe/go-internal)
Requires:       go(github.com/stretchr/testify)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(go.opentelemetry.io/otel/trace)
Requires:       go(gopkg.in/check.v1)
Requires:       go(gopkg.in/yaml.v3)

%description
This package provides the Go library go.opentelemetry.io/auto/sdk.

%files
%doc CONTRIBUTING.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
