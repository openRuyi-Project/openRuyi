# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           mysql
%define go_import_path  github.com/go-sql-driver/mysql

Name:           go-github-go-sql-driver-mysql
Version:        1.9.2
Release:        %autorelease
Summary:        Go MySQL Driver is a MySQL driver for Go's (golang) database/sql package
License:        MPL-2.0
URL:            https://github.com/go-sql-driver/mysql
#!RemoteAsset
Source0:        https://github.com/go-sql-driver/mysql/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(filippo.io/edwards25519)

Provides:       go(github.com/go-sql-driver/mysql) = %{version}

Requires:       go(filippo.io/edwards25519)

%description
MySQL-Driver for Go's database/sql package
 Features:
  - Lightweight and fast
  - Native Go implementation. No C-bindings, just pure Go
  - Connections over TCP/IPv4, TCP/IPv6 or Unix domain sockets
  - Automatic handling of broken connections
  - Automatic Connection Pooling (by database/sql package)
  - Supports queries larger than 16MB
  - Full sql.RawBytes support.
  - Intelligent LONG DATA handling in prepared statements
  - Secure LOAD DATA LOCAL INFILE support with file Whitelisting and io.Reader
    support
  - Optional time.Time parsing
  - Optional placeholder interpolation

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
