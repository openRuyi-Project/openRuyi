# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           squirrel
%define go_import_path  github.com/Masterminds/squirrel

Name:           go-github-masterminds-squirrel
Version:        1.4.0
Release:        %autorelease
Summary:        Fluent SQL query builder for Go
License:        MIT
URL:            https://github.com/Masterminds/squirrel
#!RemoteAsset:  sha256:a4f59e9622a49c010949373d36ddda198fe0de1e66de6c524edc415aead8ff9c
Source0:        https://github.com/Masterminds/squirrel/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  gcc
BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-sql-driver/mysql)
BuildRequires:  go(github.com/lann/builder)
BuildRequires:  go(github.com/lib/pq)
BuildRequires:  go(github.com/mattn/go-sqlite3)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/Masterminds/squirrel) = %{version}

Requires:       go(github.com/lann/builder)

%description
Fluent SQL query builder for Go.

%files
%doc README.md
%license LICENSE.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
