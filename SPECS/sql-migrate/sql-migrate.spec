# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           sql-migrate
%define go_import_path  github.com/rubenv/sql-migrate
%define commit_id       8d140a17f3511200a446d4d970322ad057c5c322

Name:           sql-migrate
Version:        0+git20260922.8d140a1
Release:        %autorelease
Summary:        SQL schema migration tool for Go
License:        MIT
URL:            https://github.com/rubenv/sql-migrate
#!RemoteAsset:  sha256:6005649966b4875e4d9c05dec8ac91b7a1d10ecc09cf820a283e709ffeb5ce40
Source0:        https://github.com/rubenv/sql-migrate/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildSystem:    golang

BuildRequires:  gcc
BuildRequires:  go
BuildRequires:  go-rpm-macros
# Transitive imports missing from the distribution cli/go-multierror Requires.
BuildRequires:  go(github.com/Masterminds/sprig/v3)
BuildRequires:  go(github.com/hashicorp/errwrap)
BuildRequires:  go(github.com/denisenkom/go-mssqldb)
BuildRequires:  go(github.com/go-sql-driver/mysql)
BuildRequires:  go(github.com/gobuffalo/packr/v2)
BuildRequires:  go(github.com/lib/pq)
BuildRequires:  go(github.com/mattn/go-sqlite3)
BuildRequires:  go(github.com/mitchellh/cli)
BuildRequires:  go(github.com/olekukonko/tablewriter) < 1.0.0
BuildRequires:  go(gopkg.in/check.v1)
BuildRequires:  go(gopkg.in/gorp.v1)
BuildRequires:  go(gopkg.in/yaml.v2)

%package     -n go-github-rubenv-sql-migrate
Summary:        Go source for sql-migrate
BuildArch:      noarch

Provides:       go(github.com/rubenv/sql-migrate) = %{version}

Requires:       go(github.com/Masterminds/sprig/v3)
Requires:       go(github.com/hashicorp/errwrap)
Requires:       go(github.com/denisenkom/go-mssqldb)
Requires:       go(github.com/go-sql-driver/mysql)
Requires:       go(github.com/lib/pq)
Requires:       go(github.com/mattn/go-sqlite3)
Requires:       go(github.com/mitchellh/cli)
Requires:       go(github.com/olekukonko/tablewriter) < 1.0.0
Requires:       go(gopkg.in/gorp.v1)
Requires:       go(gopkg.in/yaml.v2)

%description
SQL schema migration tool for Go.

%description -n go-github-rubenv-sql-migrate
This package provides the reusable Go source for sql-migrate.

%build
# The executable is below the library root.
%go_common
mkdir -p _bin
%{__go} build %{go_build_flags_default} -buildmode=pie -trimpath -o _bin/%{_name} %{go_import_path}/sql-migrate

%install
install -D -m755 _bin/%{_name} %{buildroot}%{_bindir}/%{_name}
rm -rf _bin
%buildsystem_golangmodules_install

%check -a
%{buildroot}%{_bindir}/%{_name} --version > version-output.txt 2>&1
grep -Fx "1.0.0" version-output.txt

%files
%doc README.md
%license LICENSE
%{_bindir}/%{_name}

%files -n go-github-rubenv-sql-migrate
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
