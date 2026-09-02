# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-htpasswd
%define go_import_path  github.com/tg123/go-htpasswd

Name:           go-github-tg123-go-htpasswd
Version:        1.2.5
Release:        %autorelease
Summary:        HTTP password file authentication library for Go
License:        MIT
URL:            https://github.com/tg123/go-htpasswd
#!RemoteAsset:  sha256:3b8bce670d5afe8579bc6f1ce4bb01f6371a2ae45715f772b080790bed373ac4
Source0:        https://github.com/tg123/go-htpasswd/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/GehirnInc/crypt)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/crypto)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/GehirnInc/crypt)
Requires:       go(golang.org/x/crypto)

%description
This package validates user credentials against Apache-style HTTP password
files.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
