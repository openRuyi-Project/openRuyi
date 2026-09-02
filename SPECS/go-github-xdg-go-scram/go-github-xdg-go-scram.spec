# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           scram
%define go_import_path  github.com/xdg-go/scram

Name:           go-github-xdg-go-scram
Version:        1.2.0
Release:        %autorelease
Summary:        SCRAM client and server implementation for Go
License:        Apache-2.0
URL:            https://github.com/xdg-go/scram
#!RemoteAsset:  sha256:82fb3c673cd698ae14b301c86cd58541c0a678d8fd4f8da0e580ee933811199b
Source0:        https://github.com/xdg-go/scram/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/xdg-go/pbkdf2)
BuildRequires:  go(github.com/xdg-go/stringprep)
BuildRequires:  go(golang.org/x/text)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/xdg-go/pbkdf2)
Requires:       go(github.com/xdg-go/stringprep)

%description
Package scram implements the Salted Challenge Response Authentication
Mechanism described by RFC 5802 and related specifications.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
