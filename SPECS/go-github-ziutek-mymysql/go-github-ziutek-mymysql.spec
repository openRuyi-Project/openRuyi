# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           mymysql
%define go_import_path  github.com/ziutek/mymysql

Name:           go-github-ziutek-mymysql
Version:        1.5.4
Release:        %autorelease
Summary:        MySQL client and database/sql driver for Go
License:        BSD-3-Clause
URL:            https://github.com/ziutek/mymysql
#!RemoteAsset:  sha256:111b478d6190786ee098af3f365be0e33ed59e30ec4a2a9066b714515089f062
Source0:        https://github.com/ziutek/mymysql/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Legacy formatting calls fail current go vet checks.
BuildOption(check):  -vet=off
# These integration tests require a configured MySQL server on localhost:3306.
BuildOption(check):  -skip '^(TestAll|TestAutoConnectReconnect|TestBigBlob|TestBindStruct|TestDate|TestDateTimeZone|TestDecimal|TestEmpty|TestMediumInt|TestMultiple|TestMultipleResults|TestNull|TestPing|TestPrepared|TestQuery|TestReconnect|TestS|TestSDS|TestSS|TestSSDDD|TestSendLongData|TestStoredProcedures|TestTypes|TestUse|TestVarBinding)$'

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/ziutek/mymysql) = %{version}

%description
MySQL client and database/sql driver for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
