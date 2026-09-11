# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           sqlstruct
%define go_import_path  github.com/kisielk/sqlstruct
%global commit_id 5f3e10d3ab4629a59d584f8e22c4f21d54108b01

Name:           go-github-kisielk-sqlstruct
Version:        0+git20260911.5f3e10d
Release:        %autorelease
Summary:        SQL row scanning helpers for Go
License:        MIT
URL:            https://github.com/kisielk/sqlstruct
#!RemoteAsset:  sha256:e1d7079d7e4587f3f7ecba40ac272d7e3146d3cd1196865d09846d6031a2dae1
Source0:        https://github.com/kisielk/sqlstruct/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/kisielk/sqlstruct) = %{version}

%description
Sqlstruct maps SQL query result columns to Go struct fields, simplifying
row scanning with the database/sql package.

%prep
%autosetup -n %{_name}-%{commit_id}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
