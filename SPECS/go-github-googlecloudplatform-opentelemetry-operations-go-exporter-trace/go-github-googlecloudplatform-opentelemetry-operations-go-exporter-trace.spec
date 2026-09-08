# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           opentelemetry-operations-go
%define go_import_path  github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/trace

Name:           go-github-googlecloudplatform-opentelemetry-operations-go-exporter-trace
Version:        1.33.0
Release:        %autorelease
Summary:        Google Cloud Trace exporter for OpenTelemetry
License:        Apache-2.0
URL:            https://github.com/GoogleCloudPlatform/opentelemetry-operations-go
#!RemoteAsset:  sha256:615dee3fddd7afae36956622b8e8b6c829a5f2dfc8d36907e3afcfda8faff7ca
Source0:        https://github.com/GoogleCloudPlatform/opentelemetry-operations-go/archive/refs/tags/exporter/trace/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go(cloud.google.com/go/auth)
BuildRequires:  go(cloud.google.com/go/compute/metadata)
BuildRequires:  go(cloud.google.com/go/logging)
BuildRequires:  go(cloud.google.com/go/monitoring)
BuildRequires:  go(cloud.google.com/go/trace)
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/felixge/httpsnoop)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/google/s2a-go)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/googleapis/enterprise-certificate-proxy)
BuildRequires:  go(github.com/googleapis/gax-go/v2)
BuildRequires:  go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/cloudmock)
BuildRequires:  go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/resourcemapping)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/contrib)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/oauth2)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/time)
BuildRequires:  go(google.golang.org/api)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(cloud.google.com/go/trace)
Requires:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/resourcemapping)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(golang.org/x/oauth2)
Requires:       go(google.golang.org/api)
Requires:       go(google.golang.org/genproto)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)

%description
This package provides an OpenTelemetry span exporter for Google Cloud Trace.

%install
pushd exporter/trace
%buildsystem_golangmodules_install
popd

%check
pushd exporter/trace
export GO111MODULE=off
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
rm -rf "%{_builddir}/go/src/github.com/GoogleCloudPlatform/opentelemetry-operations-go"
mkdir -p "%{_builddir}/go/src/github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter"
cp -a . "%{_builddir}/go/src/%{go_import_path}"
mkdir -p "%{_builddir}/go/src/github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal"
cp -a ../../internal/cloudmock "%{_builddir}/go/src/github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/"
cp -a ../../internal/resourcemapping "%{_builddir}/go/src/github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/"
cd "%{_builddir}/go/src/%{go_import_path}"
go test -v -vet=off ./...
popd

%files
%doc exporter/trace/README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
