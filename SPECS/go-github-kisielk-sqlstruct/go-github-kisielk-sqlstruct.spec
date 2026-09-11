# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           sqlstruct
%define go_import_path  github.com/kisielk/sqlstruct
%define commit_id       5f3e10d3ab4629a59d584f8e22c4f21d54108b01

Name:           go-github-kisielk-sqlstruct
Version:        0+git20260906.5f3e10d
Release:        %autorelease
Summary:        Helpers for mapping SQL rows to Go structs
License:        MIT
URL:            https://github.com/kisielk/sqlstruct
VCS:            git:https://github.com/kisielk/sqlstruct.git
#!RemoteAsset:  sha256:e1d7079d7e4587f3f7ecba40ac272d7e3146d3cd1196865d09846d6031a2dae1
Source0:        https://github.com/kisielk/sqlstruct/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Downstream: allow repeated aliased scans without retaining a RawBytes row lock.
Patch2000:      2000-discard-unmapped-columns-without-retaining-rows.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
This library maps database/sql query results to Go structs and generates
column lists from struct fields, including aliases for joined queries.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
