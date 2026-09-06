# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           pkcs8
%define go_import_path  github.com/youmark/pkcs8

Name:           go-github-youmark-pkcs8
Version:        1.3
Release:        %autorelease
Summary:        PKCS#8 private key support for Go
License:        MIT
URL:            https://github.com/youmark/pkcs8
#!RemoteAsset:  sha256:cefad79e9fe925449f33861fcb770b46084cdc6f3400f9d99db7e90a268aad5d
Source0:        https://github.com/youmark/pkcs8/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/crypto)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(golang.org/x/crypto)

%description
PKCS8 parses and marshals encrypted and unencrypted PKCS#8 private keys in Go.

%files
%doc README README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
