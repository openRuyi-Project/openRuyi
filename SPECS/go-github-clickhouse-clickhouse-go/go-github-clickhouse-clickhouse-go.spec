# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           clickhouse-go
%define go_import_path  github.com/ClickHouse/clickhouse-go

Name:           go-github-clickhouse-clickhouse-go
Version:        1.5.4
Release:        %autorelease
Summary:        Go database driver for ClickHouse
License:        MIT
URL:            https://github.com/ClickHouse/clickhouse-go
#!RemoteAsset:  sha256:1a625c85a49d3d4eab611492d124065ac1771b2f0eca7f3e5cd0cc28fc45d77b
Source0:        https://github.com/ClickHouse/clickhouse-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# These integration tests require a ClickHouse server on localhost:9000.
BuildOption(check):  -skip '^(Test_NullableArray|Test_ConnCheck|Test_ConnCheckNegative|Test_Issue38_uint64_support|Test_Issue42_Plain_SQL_Support|TestBytes|TestNullableEnumWithoutLeadZero|TestQuerySettings|Test_ColumnarInsert|Test_Compress|Test_Custom_Types|Test_Scan_Value|Test_Decimal128|Test_Decimal|Test_DirectInsert|Test_DirectArrayT|Test_Negative_OpenConnectAndPing|Test_Nullable|Test_OpenConnectAndPing|Test_RegisterTLSConfig|Test_CreateTable|Test_Insert|Test_InsertBatch|Test_Select|Test_SimpleSelect|Test_ArrayT|Test_Insert_FixedString|Test_With_Totals|Test_Tx|Test_Temporary_Table|Test_Select_External_Tables|Test_Enum|Test_Ternary_Operator|Test_UUID|Test_IP|Test_Context_Timeout|Test_Ping_Context_Timeout|Test_Timeout|Test_InArray|TestArrayArrayT|Test_LikeQuery|Test_NullableScan|Test_Tuple|Test_ReadHistogram|Test_ReadArrayArrayTuple|Test_RegisterDial)$'

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/bkaradzic/go-lz4)
BuildRequires:  go(github.com/cloudflare/golz4)
BuildRequires:  go(github.com/pierrec/lz4)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/ClickHouse/clickhouse-go) = %{version}

Requires:       go(github.com/cloudflare/golz4)

%description
This package provides a database/sql driver and a native client for
ClickHouse, with column conversion and compression support.

%prep -a
# Standalone examples use additional application libraries.
rm -rf examples

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
