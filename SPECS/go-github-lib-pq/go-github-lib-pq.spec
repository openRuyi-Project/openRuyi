# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           pq
%define go_import_path  github.com/lib/pq
# pq test failure due to network connection part - Julian
# TODO: kerberos require additional dependencies - Julian
%define go_test_exclude %{shrink:
    github.com/lib/pq
    github.com/lib/pq/auth/kerberos
}

Name:           go-github-lib-pq
Version:        1.11.1
Release:        %autorelease
Summary:        Go PostgreSQL driver for database/sql
License:        MIT
URL:            https://github.com/lib/pq
#!RemoteAsset
Source0:        https://github.com/lib/pq/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/lib/pq) = %{version}

%description
pq is a Go PostgreSQL driver for database/sql.

All maintained versions of PostgreSQL are supported. Older versions may work, but this is not tested.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
