# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-sqlmock
%define go_import_path  github.com/DATA-DOG/go-sqlmock

Name:           go-github-data-dog-go-sqlmock
Version:        1.5.2
Release:        %autorelease
Summary:        Mock database driver for testing Go SQL code
License:        BSD-3-Clause
URL:            https://github.com/DATA-DOG/go-sqlmock
VCS:            git:https://github.com/DATA-DOG/go-sqlmock.git
#!RemoteAsset:  sha256:e0914e2bce867bb6708e8ceb7ca7ece4c5a6473a873d0a5927943a932dbdd03e
Source0:        https://github.com/DATA-DOG/go-sqlmock/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Downstream: preserve preformatted errors and pass the Go printf analyzer.
Patch2000:      2000-use-errors-new-for-preformatted-messages.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/kisielk/sqlstruct)

Provides:       go(%{go_import_path}) = %{version}

%description
This library implements a mock database/sql driver for Go tests. It checks
expected queries, arguments, transactions, and results without a database
server. The source package includes the upstream examples and their tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
