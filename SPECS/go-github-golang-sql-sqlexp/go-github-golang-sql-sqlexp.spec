# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           sqlexp
%define go_import_path  github.com/golang-sql/sqlexp

Name:           go-github-golang-sql-sqlexp
Version:        0.1.0
Release:        %autorelease
Summary:        Experimental extensions to Go database/sql
License:        BSD-3-Clause
URL:            https://github.com/golang-sql/sqlexp
#!RemoteAsset:  sha256:a12b1e379722c31ca26a386b0193316ebed188310aa897b6c89980752a0ed05d
Source0:        https://github.com/golang-sql/sqlexp/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}
Provides:       go(%{go_import_path}/nest) = %{version}

%description
Sqlexp provides experimental database interfaces for messages, naming,
quoting, savepoints, and nested transactions.

%files
%doc README.md
%license LICENSE
%license PATENTS
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
