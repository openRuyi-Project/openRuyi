# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           dtls
%define go_import_path  github.com/pion/dtls/v2
%define go_test_exclude %{go_import_path}/pkg/protocol/handshake

Name:           go-github-pion-dtls-v2
Version:        2.2.12
Release:        %autorelease
Summary:        A Go implementation of DTLS
License:        MIT
URL:            https://github.com/pion/dtls
#!RemoteAsset:  sha256:17d45dba2712a9fff680f1e441b26566daf7f9103656fd3f65d05fda0b5e0009
Source0:        https://github.com/pion/dtls/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/pion/logging)
BuildRequires:  go(github.com/pion/transport/v2)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/net)

Provides:       go(github.com/pion/dtls/v2) = %{version}

Requires:       go(github.com/pion/logging)
Requires:       go(github.com/pion/transport/v2)
Requires:       go(golang.org/x/crypto)

%description
Native DTLS 1.2 implementation in the Go programming language.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
