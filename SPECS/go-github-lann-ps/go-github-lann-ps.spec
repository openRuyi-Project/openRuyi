# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ps
%define go_import_path  github.com/lann/ps
%define commit_id       62de8c46ede02a7675c4c79c84883eb164cb71e3

Name:           go-github-lann-ps
Version:        0+git20260922.62de8c4
Release:        %autorelease
Summary:        Persistent immutable data structures for Go
License:        MIT
URL:            https://github.com/lann/ps
#!RemoteAsset:  sha256:1d0df31d2532d3f5a5292b6229310ae6ba57b9a0b8756bbbd480767dfb7d8678
Source0:        https://github.com/lann/ps/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/lann/ps) = %{version}

%description
Persistent immutable data structures for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
