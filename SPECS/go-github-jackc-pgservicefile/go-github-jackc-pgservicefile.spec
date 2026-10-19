# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           pgservicefile
%define go_import_path  github.com/jackc/pgservicefile
%define commit_id       5a60cdf6a76120dc3d5152b95f3b5fd8aa7cc9eb

Name:           go-github-jackc-pgservicefile
Version:        0+git20261019.5a60cdf
Release:        %autorelease
Summary:        Parser for PostgreSQL service files
License:        MIT
URL:            https://github.com/jackc/pgservicefile
#!RemoteAsset:  sha256:6784ef1364ab9793d28bb5f7398ec5a79d27982d2880d0454526b21036d418bc
Source0:        https://github.com/jackc/pgservicefile/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
Pgservicefile parses PostgreSQL connection service files and exposes the
named connection settings to Go applications.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
