# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-sqlmock
%define go_import_path  github.com/DATA-DOG/go-sqlmock

# The orders example deadlocks in Tx.Rollback with Go 1.27 RawBytes locking:
# TestShouldRefundUserWhenOrderIsCancelled timed out after 1m30s.
%define go_test_exclude %{go_import_path}/examples/orders

Name:           go-github-data-dog-go-sqlmock
Version:        1.5.2
Release:        %autorelease
Summary:        SQL driver mock library for Go
License:        BSD-3-Clause
URL:            https://github.com/DATA-DOG/go-sqlmock
#!RemoteAsset:  sha256:e0914e2bce867bb6708e8ceb7ca7ece4c5a6473a873d0a5927943a932dbdd03e
Source0:        https://github.com/DATA-DOG/go-sqlmock/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Fix go vet: non-constant format string in call to fmt.Errorf.
Patch2000:      2000-use-constant-error-formats.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/kisielk/sqlstruct)

Provides:       go(github.com/DATA-DOG/go-sqlmock) = %{version}

Requires:       go(github.com/kisielk/sqlstruct)

%description
Sqlmock simulates SQL driver behavior for Go tests without a real database
connection, supporting transactions, prepared statements and expectations.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
