# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           otel
%define go_import_path  go.opentelemetry.io/otel

Name:           go-opentelemetry-otel
Version:        1.43.0
Release:        %autorelease
Summary:        Go module dependency for Prometheus
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-go
#!RemoteAsset:  sha256:f8ce59f6705b718114124b234a5761a9e9141261faa9b31d4a2a86b14e988e52
Source0:        https://github.com/open-telemetry/opentelemetry-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n opentelemetry-go-1.43.0
# go.opentelemetry.io/otel/internal/global imports go.opentelemetry.io/auto/sdk,
# while auto/sdk imports otel APIs. Limit bootstrap %check to leaf API packages
# that do not require auto/sdk so the BuildRequires cycle can be resolved.
%define go_test_include %{shrink:
    %{go_import_path}/attribute
    %{go_import_path}/baggage
    %{go_import_path}/codes
}

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
Provides:       go(go.opentelemetry.io/otel/attribute) = %{version}
Provides:       go(go.opentelemetry.io/otel/attribute/internal) = %{version}
Provides:       go(go.opentelemetry.io/otel/attribute/internal/xxhash) = %{version}
Provides:       go(go.opentelemetry.io/otel/baggage) = %{version}
Provides:       go(go.opentelemetry.io/otel/codes) = %{version}
Provides:       go(go.opentelemetry.io/otel/internal/baggage) = %{version}
Provides:       go(go.opentelemetry.io/otel/internal/errorhandler) = %{version}
Provides:       go(go.opentelemetry.io/otel/internal/global) = %{version}
Provides:       go(go.opentelemetry.io/otel/internal/internaltest) = %{version}
Provides:       go(go.opentelemetry.io/otel/propagation) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/internal) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/internal/v2) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/internal/v3) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/internal/v4) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.10.0) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.11.0) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.12.0) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.13.0) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.13.0/httpconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.13.0/netconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.14.0) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.14.0/httpconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.14.0/netconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.15.0) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.15.0/httpconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.15.0/netconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.16.0) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.16.0/httpconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.16.0/netconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.17.0) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.17.0/httpconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.17.0/netconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.18.0) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.18.0/httpconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.18.0/netconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.19.0) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.19.0/httpconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.19.0/netconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.20.0) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.20.0/httpconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.20.0/netconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.21.0) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.22.0) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.23.0) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.23.1) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.24.0) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.25.0) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.26.0) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.27.0) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.28.0) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.30.0) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.31.0) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.32.0) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.32.0/azureconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.32.0/cicdconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.32.0/containerconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.32.0/cpuconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.32.0/dbconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.32.0/dnsconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.32.0/faasconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.32.0/genaiconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.32.0/goconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.32.0/httpconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.32.0/hwconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.32.0/k8sconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.32.0/messagingconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.32.0/otelconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.32.0/processconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.32.0/rpcconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.32.0/signalrconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.32.0/systemconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.32.0/vcsconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.33.0) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.33.0/azureconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.33.0/cicdconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.33.0/containerconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.33.0/cpuconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.33.0/dbconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.33.0/dnsconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.33.0/faasconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.33.0/genaiconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.33.0/goconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.33.0/httpconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.33.0/hwconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.33.0/k8sconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.33.0/messagingconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.33.0/otelconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.33.0/processconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.33.0/rpcconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.33.0/signalrconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.33.0/systemconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.33.0/vcsconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.34.0) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.34.0/azureconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.34.0/cicdconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.34.0/containerconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.34.0/cpuconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.34.0/dbconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.34.0/dnsconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.34.0/faasconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.34.0/genaiconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.34.0/goconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.34.0/httpconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.34.0/hwconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.34.0/k8sconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.34.0/messagingconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.34.0/otelconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.34.0/processconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.34.0/rpcconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.34.0/signalrconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.34.0/systemconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.34.0/vcsconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.36.0) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.36.0/azureconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.36.0/cicdconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.36.0/containerconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.36.0/dbconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.36.0/dnsconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.36.0/faasconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.36.0/genaiconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.36.0/goconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.36.0/httpconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.36.0/hwconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.36.0/k8sconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.36.0/messagingconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.36.0/otelconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.36.0/processconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.36.0/rpcconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.36.0/signalrconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.36.0/systemconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.36.0/vcsconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.37.0) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.37.0/azureconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.37.0/cicdconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.37.0/containerconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.37.0/dbconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.37.0/dnsconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.37.0/faasconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.37.0/genaiconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.37.0/goconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.37.0/httpconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.37.0/hwconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.37.0/k8sconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.37.0/messagingconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.37.0/otelconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.37.0/processconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.37.0/rpcconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.37.0/signalrconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.37.0/systemconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.37.0/vcsconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.38.0) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.38.0/azureconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.38.0/cicdconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.38.0/containerconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.38.0/dbconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.38.0/dnsconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.38.0/faasconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.38.0/genaiconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.38.0/goconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.38.0/httpconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.38.0/hwconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.38.0/k8sconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.38.0/messagingconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.38.0/nfsconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.38.0/openshiftconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.38.0/otelconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.38.0/processconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.38.0/rpcconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.38.0/signalrconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.38.0/systemconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.38.0/vcsconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.39.0) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.39.0/azureconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.39.0/cicdconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.39.0/containerconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.39.0/dbconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.39.0/dnsconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.39.0/faasconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.39.0/genaiconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.39.0/goconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.39.0/httpconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.39.0/hwconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.39.0/k8sconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.39.0/mcpconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.39.0/messagingconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.39.0/nfsconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.39.0/openshiftconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.39.0/otelconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.39.0/processconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.39.0/rpcconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.39.0/signalrconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.39.0/systemconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.39.0/vcsconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.4.0) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.40.0) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.40.0/azureconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.40.0/cicdconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.40.0/containerconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.40.0/dbconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.40.0/dnsconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.40.0/faasconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.40.0/genaiconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.40.0/goconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.40.0/httpconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.40.0/hwconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.40.0/k8sconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.40.0/mcpconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.40.0/messagingconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.40.0/nfsconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.40.0/openshiftconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.40.0/otelconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.40.0/processconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.40.0/rpcconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.40.0/signalrconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.40.0/systemconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.40.0/vcsconv) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.5.0) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.6.1) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.7.0) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.8.0) = %{version}
Provides:       go(go.opentelemetry.io/otel/semconv/v1.9.0) = %{version}
Requires:       go(github.com/cespare/xxhash/v2)
Requires:       go(github.com/go-logr/logr)
Requires:       go(github.com/go-logr/stdr)
# Do not add Requires: go(go.opentelemetry.io/auto/sdk) here: auto/sdk
# imports otel APIs, and OBS expands runtime Requires while resolving
# BuildRequires, which would make the bootstrap cycle unbuildable.

%description
Go module dependency for Prometheus. Generated by go2spec.

%files
%doc README.md
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}
# Nested Go modules are packaged separately; do not let the root module own
# their source directories, otherwise BuildRequires that install both packages
# will hit RPM file conflicts.
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
%exclude %{go_sys_gopath}/%{go_import_path}/exporters/stdout/stdoutmetric
%exclude %{go_sys_gopath}/%{go_import_path}/exporters/stdout/stdouttrace
%exclude %{go_sys_gopath}/%{go_import_path}/exporters/zipkin
%exclude %{go_sys_gopath}/%{go_import_path}/internal/tools
%exclude %{go_sys_gopath}/%{go_import_path}/log
%exclude %{go_sys_gopath}/%{go_import_path}/log/logtest
%exclude %{go_sys_gopath}/%{go_import_path}/metric
%exclude %{go_sys_gopath}/%{go_import_path}/schema
%exclude %{go_sys_gopath}/%{go_import_path}/sdk
%exclude %{go_sys_gopath}/%{go_import_path}/sdk/log
%exclude %{go_sys_gopath}/%{go_import_path}/sdk/log/logtest
%exclude %{go_sys_gopath}/%{go_import_path}/sdk/metric
%exclude %{go_sys_gopath}/%{go_import_path}/trace
%exclude %{go_sys_gopath}/%{go_import_path}/trace/internal/telemetry/test

%changelog
%autochangelog
