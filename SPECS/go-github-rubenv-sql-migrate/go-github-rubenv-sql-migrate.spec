# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           sql-migrate
%define go_import_path  github.com/rubenv/sql-migrate

Name:           go-github-rubenv-sql-migrate
Version:        0+git20200616.8d140a1
Release:        %autorelease
Summary:        SQL Schema migration tool for Go
License:        MIT
URL:            https://github.com/rubenv/sql-migrate
VCS:            git:https://github.com/rubenv/sql-migrate.git
#!RemoteAsset:  sha256:6005649966b4875e4d9c05dec8ac91b7a1d10ecc09cf820a283e709ffeb5ce40
Source0:        https://github.com/rubenv/sql-migrate/archive/8d140a17f351.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n sql-migrate-8d140a17f3511200a446d4d970322ad057c5c322

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/Masterminds/sprig/v3)
BuildRequires:  go(github.com/denisenkom/go-mssqldb)
BuildRequires:  go(github.com/go-sql-driver/mysql)
BuildRequires:  go(github.com/gobuffalo/packr/v2)
BuildRequires:  go(github.com/hashicorp/errwrap)
BuildRequires:  go(github.com/lib/pq)
BuildRequires:  go(github.com/mattn/go-sqlite3)
BuildRequires:  go(github.com/mitchellh/cli)
# Upstream requires tablewriter v0; name the compatibility package to avoid
# the ambiguous virtual provider shared with tablewriter v1.
BuildRequires:  go-github-olekukonko-tablewriter-v0
BuildRequires:  go(gopkg.in/check.v1)
BuildRequires:  go(gopkg.in/gorp.v1)
BuildRequires:  go(gopkg.in/yaml.v2)

Provides:       go(github.com/rubenv/sql-migrate) = %{version}

Requires:       go(github.com/Masterminds/sprig/v3)
Requires:       go(github.com/denisenkom/go-mssqldb)
Requires:       go(github.com/go-sql-driver/mysql)
Requires:       go(github.com/hashicorp/errwrap)
Requires:       go(github.com/lib/pq)
Requires:       go(github.com/mattn/go-sqlite3)
Requires:       go(github.com/mitchellh/cli)
Requires:       go-github-olekukonko-tablewriter-v0
Requires:       go(gopkg.in/gorp.v1)
Requires:       go(gopkg.in/yaml.v2)

%description
This package provides the github.com/rubenv/sql-migrate Go module source.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
