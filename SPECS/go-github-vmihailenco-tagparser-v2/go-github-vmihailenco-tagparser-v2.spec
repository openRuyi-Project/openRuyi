# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           tagparser
%define go_import_path  github.com/vmihailenco/tagparser/v2

Name:           go-github-vmihailenco-tagparser-v2
Version:        2.0.0
Release:        %autorelease
Summary:        Opinionated Golang tag parser
License:        BSD-2-Clause
URL:            https://github.com/vmihailenco/tagparser
#!RemoteAsset:  sha256:676b99c051fef68d1b0fb0385103de0e42a3ee556919b2b54ff5d3445bac56dd
Source0:        https://github.com/vmihailenco/tagparser/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/vmihailenco/tagparser/v2) = %{version}

%description
Opinionated Golang tag parser

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
