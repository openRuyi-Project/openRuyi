# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-sqllexer
%define go_import_path  github.com/DataDog/go-sqllexer

Name:           go-github-datadog-go-sqllexer
Version:        0.2.4
Release:        %autorelease
Summary:        SQL lexer for query obfuscation and normalization
License:        MIT
URL:            https://github.com/DataDog/go-sqllexer
#!RemoteAsset:  sha256:c048dba3e8fe14ba02449d72dbca0325cb1888aa2d11ab2f7cd9d966fa3929ce
Source0:        https://github.com/DataDog/go-sqllexer/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(%{go_import_path}) = %{version}

%description
Go-sqllexer tokenizes SQL queries for obfuscation and normalization without
implementing a full SQL parser.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
