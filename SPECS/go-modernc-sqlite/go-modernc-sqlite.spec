# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           sqlite
%define go_import_path  modernc.org/sqlite
%define go_test_exclude %{go_import_path}

Name:           go-modernc-sqlite
Version:        1.53.0
Release:        %autorelease
Summary:        a sql/database driver using a CGo-free port of the C SQLite3 library
License:        BSD-3-Clause
URL:            https://gitlab.com/cznic/sqlite
#!RemoteAsset:  sha256:3f91d99d1ce3cafbff61969c1c6f85104940bb2c22e1e845c957fcf40b445272
Source0:        https://gitlab.com/cznic/sqlite/-/archive/v%{version}/sqlite-v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  tzdata
BuildRequires:  go(github.com/google/pprof)
BuildRequires:  go(github.com/mattn/go-sqlite3)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(modernc.org/fileutil)
BuildRequires:  go(modernc.org/libc)
BuildRequires:  go(modernc.org/mathutil)

Provides:       go(modernc.org/sqlite) = %{version}

Requires:       go(golang.org/x/sys)
Requires:       go(modernc.org/libc)

%description
Package sqlite is a sql/database driver using a CGo-free port of the C SQLite3
library.

SQLite is an in-process implementation of a self-contained, serverless,
zero-configuration, transactional SQL database engine.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
