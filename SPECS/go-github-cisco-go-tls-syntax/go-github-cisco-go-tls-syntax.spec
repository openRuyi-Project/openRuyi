# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-tls-syntax
%define go_import_path  github.com/cisco/go-tls-syntax
%define commit_id       46b0cfb76b9b7d3f37685363fe10e8533fc5f37c

Name:           go-github-cisco-go-tls-syntax
Version:        0+git20261118.46b0cfb
Release:        %autorelease
Summary:        TLS defines its own syntax
License:        BSD-2-Clause
URL:            https://github.com/cisco/go-tls-syntax
#!RemoteAsset:  sha256:4c3c5d875edcc2da5181020e383aa0b3add5a5179a6ba384bab20827a8dce21c
Source0:        https://github.com/cisco/go-tls-syntax/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/cisco/go-tls-syntax) = %{version}

%description
TLS presentation syntax serialization library for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
