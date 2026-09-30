# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           civil
%define go_import_path  github.com/golang-sql/civil
%define commit_id       cb61b32ac6fe84d34b81730175f91965e43d0f90

Name:           go-github-golang-sql-civil
Version:        0+git20260922.cb61b32
Release:        %autorelease
Summary:        Civil date, time and datetime types for Go
License:        Apache-2.0
URL:            https://github.com/golang-sql/civil
#!RemoteAsset:  sha256:fe088ec5d296bfc7f152eb16d5a069526973f6f1f079fdde5ba70e3c3443d25e
Source0:        https://github.com/golang-sql/civil/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/golang-sql/civil) = %{version}

%description
Civil date, time and datetime types for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
