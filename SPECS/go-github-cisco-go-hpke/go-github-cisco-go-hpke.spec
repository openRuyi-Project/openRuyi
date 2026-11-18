# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-hpke
%define go_import_path  github.com/cisco/go-hpke
%define commit_id       246075f836094272b605d1ecd630cb63b6ba5596

Name:           go-github-cisco-go-hpke
Version:        0+git20261118.246075f
Release:        %autorelease
Summary:        This repo provides a Go implementation of the HPKE primitive proposed for discussion at CFRG
License:        BSD-2-Clause
URL:            https://github.com/cisco/go-hpke
#!RemoteAsset:  sha256:71b261476cf31fd17225991ddbb2a02aac022a901e26055e1e7331175ba25c0f
Source0:        https://github.com/cisco/go-hpke/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/cisco/go-tls-syntax)
BuildRequires:  go(github.com/cloudflare/circl)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/crypto)

Provides:       go(github.com/cisco/go-hpke) = %{version}

Requires:       go(github.com/cisco/go-tls-syntax)
Requires:       go(github.com/cloudflare/circl)
Requires:       go(golang.org/x/crypto)

%description
Go implementation of Hybrid Public Key Encryption (HPKE).

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
