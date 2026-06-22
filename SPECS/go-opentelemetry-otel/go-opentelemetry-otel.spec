# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           otel
%define go_import_path  go.opentelemetry.io/otel
# go.opentelemetry.io/otel/internal/global imports go.opentelemetry.io/auto/sdk,
# while auto/sdk imports otel APIs. Limit bootstrap %check to leaf API packages
# that do not require auto/sdk so the BuildRequires cycle can be resolved. - HNO3Miracle
%define go_test_include %{shrink:
    %{go_import_path}/attribute
    %{go_import_path}/baggage
    %{go_import_path}/codes
}

Name:           go-opentelemetry-otel
Version:        1.44.0
Release:        %autorelease
Summary:        OpenTelemetry API for Go
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-go
#!RemoteAsset:  sha256:fc1c8d58df26300576a8acbc6d53d07477784c656fd22018e86540a4392407d4
Source0:        https://github.com/open-telemetry/opentelemetry-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Current Go vet rejects %%q with a uint64 value in codes.UnmarshalJSON.
# Use the numeric format that matches the parsed value. - HNO3Miracle
Patch2000:      2000-fix-invalid-code-format-for-go-vet.patch

BuildRequires:  go
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go-rpm-macros

Provides:       go(go.opentelemetry.io/otel) = %{version}
Provides:       go(go.opentelemetry.io/otel/exporters/stdout/stdoutmetric) = %{version}
Provides:       go(go.opentelemetry.io/otel/exporters/stdout/stdouttrace) = %{version}
Provides:       go(go.opentelemetry.io/otel/metric) = %{version}
Provides:       go(go.opentelemetry.io/otel/sdk) = %{version}
Provides:       go(go.opentelemetry.io/otel/sdk/metric) = %{version}
Provides:       go(go.opentelemetry.io/otel/sdk/metric/metricdata) = %{version}
Provides:       go(go.opentelemetry.io/otel/trace) = %{version}

Requires:       go(github.com/cespare/xxhash/v2)
Requires:       go(github.com/go-logr/logr)
Requires:       go(github.com/go-logr/stdr)
Requires:       go(github.com/google/uuid)
Requires:       go(golang.org/x/sys)
# Do not add Requires: go(go.opentelemetry.io/auto/sdk) here: auto/sdk
# imports otel APIs, and OBS expands runtime Requires while resolving
# BuildRequires, which would make the bootstrap cycle unbuildable.

%description
This package provides the core OpenTelemetry API module for Go.

%files
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}
# Nested Go modules are packaged separately; do not let the root module own
# their source directories, otherwise BuildRequires that install both packages
# will hit RPM file conflicts. - HNO3Miracle
%exclude %{go_sys_gopath}/%{go_import_path}/bridge/opencensus
%exclude %{go_sys_gopath}/%{go_import_path}/bridge/opentracing
%exclude %{go_sys_gopath}/%{go_import_path}/exporters/otlp/otlplog/otlploggrpc
%exclude %{go_sys_gopath}/%{go_import_path}/exporters/otlp/otlplog/otlploghttp
%exclude %{go_sys_gopath}/%{go_import_path}/exporters/otlp/otlpmetric/otlpmetricgrpc
%exclude %{go_sys_gopath}/%{go_import_path}/exporters/otlp/otlpmetric/otlpmetrichttp
%exclude %{go_sys_gopath}/%{go_import_path}/exporters/otlp/otlptrace
%exclude %{go_sys_gopath}/%{go_import_path}/exporters/otlp/otlptrace/otlptracegrpc
%exclude %{go_sys_gopath}/%{go_import_path}/exporters/otlp/otlptrace/otlptracehttp
%exclude %{go_sys_gopath}/%{go_import_path}/exporters/prometheus
%exclude %{go_sys_gopath}/%{go_import_path}/exporters/stdout/stdoutlog
%exclude %{go_sys_gopath}/%{go_import_path}/exporters/zipkin
%exclude %{go_sys_gopath}/%{go_import_path}/internal/tools
%exclude %{go_sys_gopath}/%{go_import_path}/log
%exclude %{go_sys_gopath}/%{go_import_path}/log/logtest
%exclude %{go_sys_gopath}/%{go_import_path}/schema
%exclude %{go_sys_gopath}/%{go_import_path}/sdk/log
%exclude %{go_sys_gopath}/%{go_import_path}/sdk/log/logtest
%exclude %{go_sys_gopath}/%{go_import_path}/trace/internal/telemetry/test

%changelog
%autochangelog
