# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           csrf
%define go_import_path  github.com/gorilla/csrf

Name:           go-github-gorilla-csrf
Version:        1.7.3
Release:        %autorelease
Summary:        CSRF prevention middleware for Go web applications
License:        BSD-3-Clause
URL:            https://github.com/gorilla/csrf
#!RemoteAsset:  sha256:4399ac78e57691e3b5d67f440567e11eca999fce05c986d2ea7410b5f49e8438
Source0:        https://github.com/gorilla/csrf/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Preserve generateRandomBytes error handling after crypto/rand.Read became
# process-fatal on random source errors in Go 1.24.
Patch2000:      2000-csrf-preserve-random-source-errors-on-Go-1.24.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/gorilla/securecookie)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/gorilla/securecookie)

%description
Gorilla CSRF provides Cross-Site Request Forgery prevention middleware for Go
web applications and services.

%prep -a
rm -rf vendor

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
