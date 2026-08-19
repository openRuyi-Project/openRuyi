# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: Apache-2.0

%define _name           certtostore
%define go_import_path  github.com/google/certtostore

Name:           go-github-google-certtostore
Version:        1.0.7
Release:        %autorelease
Summary:        Store certificates in the native certificate store
License:        Apache-2.0
URL:            https://github.com/google/certtostore
#!RemoteAsset:  sha256:7d2db1943c080cbf116bd7f00f1c1a951061c69a5cea216d7edda53f7ede25b5
Source0:        https://github.com/google/certtostore/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/StackExchange/wmi)
BuildRequires:  go(github.com/google/deck)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/google/certtostore) = %{version}

Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/sys)

%description
certtostore stores and retrieves certificates using the native certificate
store on supported platforms.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
