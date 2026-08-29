# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-patricia
%define go_import_path  github.com/tchap/go-patricia/v2

Name:           go-github-tchap-go-patricia-v2
Version:        2.3.3
Release:        %autorelease
Summary:        Patricia trie implementation for Go
License:        MIT
URL:            https://github.com/tchap/go-patricia
#!RemoteAsset:  sha256:77072a4ac0274f76de642c5678e92c7af3ee6d61b96e77ce0dbb78fa2cebf012
Source0:        https://github.com/tchap/go-patricia/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/tchap/go-patricia/v2) = %{version}

%description
A generic patricia trie (also called radix tree) implemented in Go
(Golang).

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
