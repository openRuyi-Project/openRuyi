# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           clickhouse-go
%define go_import_path  github.com/ClickHouse/clickhouse-go
%define go_test_exclude %{go_import_path}/examples

Name:           go-github-clickhouse-clickhouse-go
Version:        1.5.4
Release:        %autorelease
Summary:        Golang SQL database driver for Yandex ClickHouse
License:        MIT
URL:            https://github.com/ClickHouse/clickhouse-go
VCS:            git:https://github.com/ClickHouse/clickhouse-go.git
#!RemoteAsset:  sha256:1a625c85a49d3d4eab611492d124065ac1771b2f0eca7f3e5cd0cc28fc45d77b
Source0:        https://github.com/ClickHouse/clickhouse-go/archive/v1.5.4.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n clickhouse-go-1.5.4
BuildOption(check):  -run '^$'

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/bkaradzic/go-lz4)
BuildRequires:  go(github.com/cloudflare/golz4)
BuildRequires:  go(github.com/jmoiron/sqlx)
BuildRequires:  go(github.com/pierrec/lz4)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/ClickHouse/clickhouse-go) = %{version}

Requires:       go(github.com/jmoiron/sqlx)

%description
This package provides the github.com/ClickHouse/clickhouse-go Go module source.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
