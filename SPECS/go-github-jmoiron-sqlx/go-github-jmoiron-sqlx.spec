# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           sqlx
%define go_import_path  github.com/jmoiron/sqlx

Name:           go-github-jmoiron-sqlx
Version:        1.2.0
Release:        %autorelease
Summary:        Extensions to Go database/sql
License:        MIT
URL:            https://github.com/jmoiron/sqlx
#!RemoteAsset:  sha256:90a0cecf61892ad7d2303720d5fced62df07746b30990b249799593b498f0df9
Source0:        https://github.com/jmoiron/sqlx/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  gcc
BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-sql-driver/mysql)
BuildRequires:  go(github.com/lib/pq)
BuildRequires:  go(github.com/mattn/go-sqlite3)

Provides:       go(github.com/jmoiron/sqlx) = %{version}

%description
Extensions to Go database/sql.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
