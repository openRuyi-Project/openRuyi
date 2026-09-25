# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gorp.v1
%define go_import_path  gopkg.in/gorp.v1

Name:           go-gopkg-gorp.v1
Version:        1.7.2
Release:        %autorelease
Summary:        SQL mapping for Go structs
License:        MIT
URL:            https://github.com/go-gorp/gorp
#!RemoteAsset:  sha256:63488c583d4bf25eb03f8224eef5934158da81650063a96b53ff4f50b9ff5409
Source0:        https://github.com/go-gorp/gorp/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# An old test formats a floating-point value as an integer.
BuildOption(check):  -vet=off

BuildRequires:  gcc
BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-sql-driver/mysql)
BuildRequires:  go(github.com/lib/pq)
BuildRequires:  go(github.com/mattn/go-sqlite3)
BuildRequires:  go(github.com/ziutek/mymysql)

Provides:       go(gopkg.in/gorp.v1) = %{version}

%description
SQL mapping for Go structs.

%check -p
# Upstream supports running the database tests against a local SQLite database.
export GORP_TEST_DIALECT=sqlite
export GORP_TEST_DSN="$PWD/gorptest.db"

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
