# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           pkcs8
%define go_import_path  github.com/youmark/pkcs8
%define commit_id a2c0da244d782506f23dd28c916a6efc2b33f9d6

Name:           go-github-youmark-pkcs8
Version:        0+git20260909.a2c0da2
Release:        %autorelease
Summary:        PKCS#8 private key support for Go
License:        MIT
URL:            https://github.com/youmark/pkcs8
#!RemoteAsset:  sha256:8e02b6c68f130faea3769d913fadebf214afb4869f7c1e8e9b4e45d938e6e25b
Source0:        https://github.com/youmark/pkcs8/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/crypto)

Provides:       go(github.com/youmark/pkcs8) = %{version}

Requires:       go(golang.org/x/crypto)

%description
PKCS8 parses and marshals encrypted and unencrypted private keys in PKCS#8
format, with password-based encryption support.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
