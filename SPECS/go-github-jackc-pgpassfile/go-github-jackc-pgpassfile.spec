# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           pgpassfile
%define go_import_path  github.com/jackc/pgpassfile

Name:           go-github-jackc-pgpassfile
Version:        1.0.0
Release:        %autorelease
Summary:        Parser for PostgreSQL password files
License:        MIT
URL:            https://github.com/jackc/pgpassfile
#!RemoteAsset:  sha256:df8904662382e1d0064ec7a5a8c36c49264d7128cea923d597802ada8c5b9603
Source0:        https://github.com/jackc/pgpassfile/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
Pgpassfile parses PostgreSQL password files and matches entries by host,
port, database, and user.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
