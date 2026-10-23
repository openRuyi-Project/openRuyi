# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           sqlclosecheck
%define go_import_path  github.com/ryanrolds/sqlclosecheck

Name:           go-github-ryanrolds-sqlclosecheck
Version:        0.6.0
Release:        %autorelease
Summary:        Linter that checks if SQL rows/statements are closed
License:        MIT
URL:            https://github.com/ryanrolds/sqlclosecheck
#!RemoteAsset:  sha256:3520a1c62e1667b67d0a4a3be07224a669bf906b175b2e172d01f15b377b2faa
Source0:        https://github.com/ryanrolds/sqlclosecheck/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-sql-driver/mysql)
BuildRequires:  go(github.com/jackc/pgpassfile)
BuildRequires:  go(github.com/jackc/pgservicefile)
BuildRequires:  go(github.com/jackc/pgx/v5)
BuildRequires:  go(github.com/jackc/puddle/v2)
BuildRequires:  go(github.com/jmoiron/sqlx)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/ryanrolds/sqlclosecheck) = %{version}
Provides:       go(github.com/ryanrolds/sqlclosecheck/pkg/analyzer) = %{version}
Provides:       go(github.com/ryanrolds/sqlclosecheck/tools) = %{version}

Requires:       go(github.com/go-sql-driver/mysql)
Requires:       go(github.com/jackc/pgx/v5)
Requires:       go(github.com/jmoiron/sqlx)
Requires:       go(golang.org/x/tools)

%description
Linter that checks if SQL rows/statements are closed.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n sqlclosecheck-%{version}
# Use packaged dependencies instead of the bundled snapshots.
rm -rf vendor

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/github.com/ryanrolds/sqlclosecheck

%changelog
%autochangelog
