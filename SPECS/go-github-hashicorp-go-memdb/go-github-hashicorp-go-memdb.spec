# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-memdb
%define go_import_path  github.com/hashicorp/go-memdb

Name:           go-github-hashicorp-go-memdb
Version:        1.3.5
Release:        %autorelease
Summary:        In-memory database with transactions and MVCC
License:        MPL-2.0
URL:            https://github.com/hashicorp/go-memdb
#!RemoteAsset:  sha256:eb5ec32bc20315971084ee91e0232ee40c32440d2f15b814113578430ecbb8f5
Source0:        https://github.com/hashicorp/go-memdb/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/hashicorp/go-immutable-radix)
BuildRequires:  go(github.com/hashicorp/golang-lru)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/hashicorp/go-immutable-radix)
Requires:       go(github.com/hashicorp/golang-lru)

%description
go-memdb implements an in-memory database built on immutable radix trees.
It supports transactions, multi-version concurrency control, indexing,
and watches for changes.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
