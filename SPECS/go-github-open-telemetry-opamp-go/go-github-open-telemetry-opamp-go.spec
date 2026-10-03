# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           opamp-go
%define go_import_path  github.com/open-telemetry/opamp-go

Name:           go-github-open-telemetry-opamp-go
Version:        0.23.0
Release:        %autorelease
Summary:        Open Agent Management Protocol implementation in Go
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opamp-go
#!RemoteAsset:  sha256:927a66a872c8a8305406b19b4a1d8683968d573608f2f29437243492d93a2a1c
Source0:        https://github.com/open-telemetry/opamp-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# https://github.com/open-telemetry/opamp-go/pull/514
Patch1:         0001-fix-resolve-test-data-race-and-flaky-server-test-514.patch
# https://github.com/open-telemetry/opamp-go/pull/564
Patch2:         0002-Fix-redirect-test-564.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/cenkalti/backoff/v4)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/gorilla/websocket)
BuildRequires:  go(github.com/knadh/koanf)
BuildRequires:  go(github.com/knadh/koanf/parsers/yaml)
BuildRequires:  go(github.com/knadh/koanf/providers/file)
BuildRequires:  go(github.com/knadh/koanf/providers/rawbytes)
BuildRequires:  go(github.com/madflojo/testcerts)
BuildRequires:  go(github.com/michel-laterman/proxy-connect-dialer-go)
BuildRequires:  go(github.com/oklog/ulid/v2)
BuildRequires:  go(github.com/shirou/gopsutil/process)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.opentelemetry.io/collector/config/configopaque)
BuildRequires:  go(go.opentelemetry.io/collector/config/configtls)
BuildRequires:  go(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.opentelemetry.io/otel/attribute)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetrichttp)
BuildRequires:  go(go.opentelemetry.io/otel/metric)
BuildRequires:  go(go.opentelemetry.io/otel/sdk)
BuildRequires:  go(go.opentelemetry.io/otel/sdk/metric)
BuildRequires:  go(go.opentelemetry.io/otel/sdk/resource)
BuildRequires:  go(go.opentelemetry.io/otel/semconv/v1.4.0)
BuildRequires:  go(go.opentelemetry.io/otel/trace)
BuildRequires:  go(google.golang.org/protobuf/proto)
BuildRequires:  go(google.golang.org/protobuf/reflect)
BuildRequires:  go(google.golang.org/protobuf/runtime)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/cenkalti/backoff/v4)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/gorilla/websocket)
Requires:       go(github.com/knadh/koanf)
Requires:       go(github.com/knadh/koanf/parsers/yaml)
Requires:       go(github.com/knadh/koanf/providers/file)
Requires:       go(github.com/knadh/koanf/providers/rawbytes)
Requires:       go(github.com/oklog/ulid/v2)
Requires:       go(github.com/shirou/gopsutil/process)
Requires:       go(go.opentelemetry.io/collector/config/configopaque)
Requires:       go(go.opentelemetry.io/collector/config/configtls)
Requires:       go(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(go.opentelemetry.io/otel/attribute)
Requires:       go(go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetrichttp)
Requires:       go(go.opentelemetry.io/otel/metric)
Requires:       go(go.opentelemetry.io/otel/sdk)
Requires:       go(go.opentelemetry.io/otel/sdk/metric)
Requires:       go(go.opentelemetry.io/otel/sdk/resource)
Requires:       go(go.opentelemetry.io/otel/semconv/v1.4.0)
Requires:       go(go.opentelemetry.io/otel/trace)
Requires:       go(github.com/michel-laterman/proxy-connect-dialer-go)

%description
This package implements the Open Agent Management Protocol for Go agents and
servers.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
