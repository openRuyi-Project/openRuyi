# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           clickhouse-go-linter
%define go_import_path  github.com/ClickHouse/clickhouse-go-linter

Name:           go-github-clickhouse-clickhouse-go-linter
Version:        1.2.1
Release:        %autorelease
Summary:        Go analyzer for ClickHouse native driver usage
License:        Apache-2.0
URL:            https://github.com/ClickHouse/clickhouse-go-linter
#!RemoteAsset:  sha256:3490513839f7488e8dc9a0337ee4e1e0af4397f8bddb8159891a37f32cf4dfce
Source0:        https://github.com/ClickHouse/clickhouse-go-linter/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.24.0
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/tools/go/analysis)
BuildRequires:  go(golang.org/x/tools/go/analysis/analysistest)
BuildRequires:  go(golang.org/x/tools/go/analysis/multichecker)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/inspect)
BuildRequires:  go(golang.org/x/tools/go/ast/inspector)

# Export the source module roots and every installed Go package.
Provides:       go(github.com/ClickHouse/clickhouse-go-linter) = %{version}
Provides:       go(github.com/ClickHouse/clickhouse-go-linter/internal/util) = %{version}
Provides:       go(github.com/ClickHouse/clickhouse-go-linter/passes/chbatchclose) = %{version}
Provides:       go(github.com/ClickHouse/clickhouse-go-linter/passes/chrowserr) = %{version}

Requires:       go(golang.org/x/tools/go/analysis)
Requires:       go(golang.org/x/tools/go/analysis/multichecker)
Requires:       go(golang.org/x/tools/go/analysis/passes/inspect)
Requires:       go(golang.org/x/tools/go/ast/inspector)

%description
Go analyzer for ClickHouse native driver usage. This package contains the
complete upstream repository sources and tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
