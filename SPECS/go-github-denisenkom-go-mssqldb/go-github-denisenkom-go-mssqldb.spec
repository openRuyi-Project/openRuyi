# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-mssqldb
%define go_import_path  github.com/denisenkom/go-mssqldb
%define commit_id       cfbb681360f0a7de54ae77703318f0e60d422e00

Name:           go-github-denisenkom-go-mssqldb
Version:        0+git20260922.cfbb681
Release:        %autorelease
Summary:        Microsoft SQL Server database/sql driver for Go
License:        BSD-3-Clause
URL:            https://github.com/denisenkom/go-mssqldb
#!RemoteAsset:  sha256:ae3dd5c142eaf3379e906e43fd94ed263a6efde66a6d625d9fd66f5d3b9d2b0e
Source0:        https://github.com/denisenkom/go-mssqldb/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Legacy dynamic logging formats fail current go vet checks.
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/golang-sql/civil)
BuildRequires:  go(golang.org/x/crypto)

Provides:       go(github.com/denisenkom/go-mssqldb) = %{version}

Requires:       go(github.com/golang-sql/civil)
Requires:       go(golang.org/x/crypto)

%description
Microsoft SQL Server database/sql driver for Go.

%files
%doc README.md
%license LICENSE.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
