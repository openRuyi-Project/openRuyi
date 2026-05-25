# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-loser
%define go_import_path  github.com/bboreham/go-loser
%define commit_id fcc2c21820a3df67b4354d37b19c39a21de7b96e

Name:           go-github-bboreham-go-loser
Version:        0+git20260607.fcc2c21
Release:        %autorelease
Summary:        Loser Tree data structure, for fast k-way merge
License:        Apache-2.0
URL:            https://github.com/bboreham/go-loser
#!RemoteAsset:  sha256:c0c652d97d0528a882630138bac21908f5b8e0fe4a18aca19b4dbb95f6d511b3
Source0:        https://github.com/bboreham/go-loser/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/exp)

Provides:       go(github.com/bboreham/go-loser) = %{version}

Requires:       go(golang.org/x/exp)

%description
Loser Tree data structure, for fast k-way merge

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
