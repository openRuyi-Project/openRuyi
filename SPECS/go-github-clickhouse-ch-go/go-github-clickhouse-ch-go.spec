# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ch-go
%define go_import_path  github.com/ClickHouse/ch-go

Name:           go-github-clickhouse-ch-go
Version:        0.74.0
Release:        %autorelease
Summary:        Low-level ClickHouse client for Go
License:        Apache-2.0
URL:            https://github.com/ClickHouse/ch-go
#!RemoteAsset:  sha256:ad9499a11634f1096d4833105d616da7df9c0b8b70dab10058aedff232d77b9f
Source0:        https://github.com/ClickHouse/ch-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/cenkalti/backoff/v4)
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/dmarkham/enumer)
BuildRequires:  go(github.com/dustin/go-humanize)
BuildRequires:  go(github.com/go-faster/city)
BuildRequires:  go(github.com/go-faster/errors)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/google/go-github/v43)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/hashicorp/go-version)
BuildRequires:  go(github.com/jackc/puddle/v2)
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/pascaldekloe/name)
BuildRequires:  go(github.com/pierrec/lz4/v4)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/segmentio/asm)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(go.uber.org/zap)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/oauth2)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  tzdata

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/dustin/go-humanize)
Requires:       go(github.com/go-faster/city)
Requires:       go(github.com/go-faster/errors)
Requires:       go(github.com/google/go-github/v43)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/hashicorp/go-version)
Requires:       go(github.com/jackc/puddle/v2)
Requires:       go(github.com/klauspost/compress)
Requires:       go(github.com/pierrec/lz4/v4)
Requires:       go(github.com/segmentio/asm)
Requires:       go(github.com/stretchr/testify)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(go.uber.org/multierr)
Requires:       go(go.uber.org/zap)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/oauth2)
Requires:       go(golang.org/x/sync)

%description
Ch-go implements the ClickHouse native protocol, typed column encodings,
compression, connection pooling, tracing, and low-level query APIs.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
