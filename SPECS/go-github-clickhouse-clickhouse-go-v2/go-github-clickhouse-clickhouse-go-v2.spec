# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           clickhouse-go
%define go_import_path  github.com/ClickHouse/clickhouse-go/v2

Name:           go-github-clickhouse-clickhouse-go-v2
Version:        2.48.0
Release:        %autorelease
Summary:        ClickHouse client for Go
License:        Apache-2.0
URL:            https://github.com/ClickHouse/clickhouse-go
#!RemoteAsset:  sha256:42700c08c7347b9069c3c6213d89b430ce97c66ac659b9302e948965aea3b1ce
Source0:        https://github.com/ClickHouse/clickhouse-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  tzdata
BuildRequires:  go(dario.cat/mergo)
BuildRequires:  go(github.com/andybalholm/brotli)
BuildRequires:  go(github.com/Azure/go-ansiterm)
BuildRequires:  go(github.com/Microsoft/go-winio)
BuildRequires:  go(github.com/cenkalti/backoff/v4)
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/ClickHouse/ch-go)
BuildRequires:  go(github.com/containerd/errdefs)
BuildRequires:  go(github.com/containerd/log)
BuildRequires:  go(github.com/containerd/platforms)
BuildRequires:  go(github.com/cpuguy83/dockercfg)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/distribution/reference)
BuildRequires:  go(github.com/docker/go-connections)
BuildRequires:  go(github.com/docker/go-units)
BuildRequires:  go(github.com/ebitengine/purego)
BuildRequires:  go(github.com/felixge/httpsnoop)
BuildRequires:  go(github.com/go-faster/city)
BuildRequires:  go(github.com/go-faster/errors)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/go-ole/go-ole)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/gorilla/websocket)
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/lufia/plan9stats)
BuildRequires:  go(github.com/magiconair/properties)
BuildRequires:  go(github.com/mkevac/debugcharts)
BuildRequires:  go(github.com/moby/docker-image-spec)
BuildRequires:  go(github.com/moby/go-archive)
BuildRequires:  go(github.com/moby/moby/api)
BuildRequires:  go(github.com/moby/moby/client)
BuildRequires:  go(github.com/moby/patternmatcher)
BuildRequires:  go(github.com/moby/sys/sequential)
BuildRequires:  go(github.com/moby/sys/user)
BuildRequires:  go(github.com/moby/sys/userns)
BuildRequires:  go(github.com/moby/term)
BuildRequires:  go(github.com/opencontainers/go-digest)
BuildRequires:  go(github.com/opencontainers/image-spec)
BuildRequires:  go(github.com/paulmach/orb)
BuildRequires:  go(github.com/pierrec/lz4/v4)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/power-devops/perfstat)
BuildRequires:  go(github.com/segmentio/asm)
BuildRequires:  go(github.com/shirou/gopsutil)
BuildRequires:  go(github.com/shirou/gopsutil/v4)
BuildRequires:  go(github.com/shopspring/decimal)
BuildRequires:  go(github.com/sirupsen/logrus)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/testcontainers/testcontainers-go)
BuildRequires:  go(github.com/tklauser/go-sysconf)
BuildRequires:  go(github.com/tklauser/numcpus)
BuildRequires:  go(github.com/yusufpapurcu/wmi)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/contrib)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/andybalholm/brotli)
Requires:       go(github.com/ClickHouse/ch-go)
Requires:       go(github.com/docker/go-units)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/mkevac/debugcharts)
Requires:       go(github.com/moby/moby/api)
Requires:       go(github.com/moby/moby/client)
Requires:       go(github.com/paulmach/orb)
Requires:       go(github.com/shopspring/decimal)
Requires:       go(github.com/stretchr/testify)
Requires:       go(github.com/testcontainers/testcontainers-go)
Requires:       go(go.opentelemetry.io/otel)

%description
ClickHouse Go implements the database/sql and native ClickHouse client APIs,
including typed columns, compression, batching, tracing, and connection pools.

%check
unset TZ
export GODEBUG=asynctimerchan=0
%buildsystem_golangmodules_check

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
