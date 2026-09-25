# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           influxdb-observability
%define go_import_path  github.com/influxdata/influxdb-observability
# Tests use collector-contrib pdatatest, which would create a clean-build cycle.
%define go_test_exclude %{go_import_path}/influx2otel

Name:           go-github-influxdata-influxdb-observability
Version:        0.5.12
Release:        %autorelease
Summary:        OpenTelemetry conversion libraries for InfluxDB
License:        MIT
URL:            https://github.com/influxdata/influxdb-observability
#!RemoteAsset:  sha256:90c5682b6d7609c04e2751d61579017439c56c112ca19787b4389d5c6aca1ad4
Source0:        https://github.com/influxdata/influxdb-observability/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Break the runtime dependency cycle with Collector contrib.
# https://github.com/influxdata/influxdb-observability/pull/353
Patch2000:      2000-influx2otel-avoid-runtime-dependency-on-pdatautil.patch

BuildRequires:  go
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/gogo/protobuf)
BuildRequires:  go(github.com/json-iterator/go)
BuildRequires:  go(github.com/modern-go/concurrent)
BuildRequires:  go(github.com/modern-go/reflect2)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.opentelemetry.io/collector)
BuildRequires:  go(go.opentelemetry.io/collector/semconv)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(golang.org/x/exp)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}/common) = %{version}
Provides:       go(%{go_import_path}/influx2otel) = %{version}
Provides:       go(%{go_import_path}/otel2influx) = %{version}

Requires:       go(github.com/gogo/protobuf)
Requires:       go(github.com/json-iterator/go)
Requires:       go(go.opentelemetry.io/collector)
Requires:       go(go.opentelemetry.io/collector/semconv)
Requires:       go(go.uber.org/multierr)
Requires:       go(golang.org/x/exp)
Requires:       go(google.golang.org/genproto)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)

%description
This package provides the common, influx2otel, and otel2influx modules from
the InfluxDB observability repository.

%install
install -d "%{buildroot}%{go_sys_gopath}/%{go_import_path}"
for module in common influx2otel otel2influx; do
    cp -a "${module}" "%{buildroot}%{go_sys_gopath}/%{go_import_path}/"
done

%check
export GO111MODULE=off
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
mkdir -p "%{_builddir}/go/src/%{go_import_path}"
for module in common influx2otel otel2influx; do
    cp -a "${module}" "%{_builddir}/go/src/%{go_import_path}/"
done
for module in common otel2influx; do
    pushd "%{_builddir}/go/src/%{go_import_path}/${module}"
    go test -v ./...
    popd
done
go build %{go_test_exclude}/...

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
