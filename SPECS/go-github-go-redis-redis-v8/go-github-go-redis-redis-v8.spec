# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           redis
%define go_import_path  github.com/go-redis/redis/v8
# Skip optional OpenTelemetry example: missing go.opentelemetry.io/otel.
# Skip scan-struct example: missing github.com/davecgh/go-spew/spew.
# Skip optional tracing integrations: missing go.opencensus.io/trace and
# go.opentelemetry.io/otel.
# Skip integration suite: dial tcp :6379: connect: connection refused.
%define go_test_exclude %{shrink:
    %{go_import_path}
    %{go_import_path}/example/otel
    %{go_import_path}/example/scan-struct
    %{go_import_path}/extra/rediscensus
    %{go_import_path}/extra/redisotel
}

Name:           go-github-go-redis-redis-v8
Version:        8.11.4
Release:        %autorelease
Summary:        Redis client for Go
License:        BSD-2-Clause
URL:            https://github.com/go-redis/redis
#!RemoteAsset:  sha256:e3cfdf1e21616fadc17014f22cc6f4259cbd2c2d4e5a1c1643c66b677bbdb55d
Source0:        https://github.com/go-redis/redis/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Go 1.26 vet rejects upstream mismatched format strings.
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/dgryski/go-rendezvous)
BuildRequires:  go(github.com/onsi/ginkgo)
BuildRequires:  go(github.com/onsi/gomega)

Provides:       go(github.com/go-redis/redis/v8) = %{version}

Requires:       go(github.com/cespare/xxhash/v2)
Requires:       go(github.com/dgryski/go-rendezvous)

%description
Go-redis is a Redis client library for Go with support for standalone servers,
Sentinel, clusters, pipelines, transactions, scripting, and Pub/Sub.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
