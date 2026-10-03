# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           opentelemetry-operations-go
%define go_import_path  github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/collector

Name:           go-github-googlecloudplatform-opentelemetry-operations-go-exporter-collector
Version:        0.57.0
Release:        %autorelease
Summary:        Google Cloud exporters for OpenTelemetry Collector data
License:        Apache-2.0
URL:            https://github.com/GoogleCloudPlatform/opentelemetry-operations-go
#!RemoteAsset:  sha256:b48b83c968c53c192b88ec7886a420efbd8f0d71dfcad8685cc39be6848661f0
Source0:        https://github.com/GoogleCloudPlatform/opentelemetry-operations-go/archive/refs/tags/exporter/collector/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go(cloud.google.com/go/auth)
BuildRequires:  go(cloud.google.com/go/compute/metadata)
BuildRequires:  go(cloud.google.com/go/logging)
BuildRequires:  go(cloud.google.com/go/monitoring)
BuildRequires:  go(cloud.google.com/go/trace)
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/felixge/httpsnoop)
BuildRequires:  go(github.com/fsnotify/fsnotify)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/go-viper/mapstructure/v2)
BuildRequires:  go(github.com/gobwas/glob)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/s2a-go)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/googleapis/enterprise-certificate-proxy)
BuildRequires:  go(github.com/googleapis/gax-go/v2)
BuildRequires:  go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/metric)
BuildRequires:  go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/trace)
BuildRequires:  go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/resourcemapping)
BuildRequires:  go(github.com/hashicorp/go-version)
BuildRequires:  go(github.com/json-iterator/go)
BuildRequires:  go(github.com/knadh/koanf/maps)
BuildRequires:  go(github.com/knadh/koanf/providers/confmap)
BuildRequires:  go(github.com/knadh/koanf/v2)
BuildRequires:  go(github.com/mitchellh/copystructure)
BuildRequires:  go(github.com/mitchellh/reflectwalk)
BuildRequires:  go(github.com/modern-go/concurrent)
BuildRequires:  go(github.com/modern-go/reflect2)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/prometheus/otlptranslator)
BuildRequires:  go(github.com/shirou/gopsutil/v4)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/tidwall/gjson)
BuildRequires:  go(github.com/tidwall/match)
BuildRequires:  go(github.com/tidwall/pretty)
BuildRequires:  go(github.com/tidwall/tinylru)
BuildRequires:  go(github.com/tidwall/wal)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/collector)
BuildRequires:  go(go.opentelemetry.io/contrib)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.uber.org/atomic)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(go.uber.org/zap)
BuildRequires:  go(go.yaml.in/yaml/v3)
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

Requires:       go(cloud.google.com/go/logging)
Requires:       go(cloud.google.com/go/monitoring)
Requires:       go(cloud.google.com/go/trace)
Requires:       go(github.com/fsnotify/fsnotify)
Requires:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/trace)
Requires:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/resourcemapping)
Requires:       go(github.com/tidwall/wal)
Requires:       go(go.opentelemetry.io/collector)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(go.uber.org/atomic)
Requires:       go(go.uber.org/zap)
Requires:       go(golang.org/x/oauth2)
Requires:       go(google.golang.org/api)
Requires:       go(google.golang.org/genproto)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)
Requires:       go(gopkg.in/yaml.v3)

%description
This package converts OpenTelemetry Collector metrics, logs, and traces for
export to Google Cloud services.

%install
pushd exporter/collector
%buildsystem_golangmodules_install
popd

%check
pushd exporter/collector
export GO111MODULE=off
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
rm -rf "%{_builddir}/go/src/github.com/GoogleCloudPlatform/opentelemetry-operations-go"
mkdir -p "%{_builddir}/go/src/github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter"
cp -a . "%{_builddir}/go/src/%{go_import_path}"
cp -a ../metric "%{_builddir}/go/src/github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/"
cp -a ../trace "%{_builddir}/go/src/github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/"
mkdir -p "%{_builddir}/go/src/github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal"
cp -a ../../internal/cloudmock "%{_builddir}/go/src/github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/"
cp -a ../../internal/resourcemapping "%{_builddir}/go/src/github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/"
cd "%{_builddir}/go/src/%{go_import_path}"
go test -v ./...
popd

%files
%doc exporter/collector/README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
