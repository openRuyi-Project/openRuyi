# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ssh
%define go_import_path  github.com/gliderlabs/ssh

Name:           go-github-gliderlabs-ssh
Version:        0.3.8
Release:        %autorelease
Summary:        Higher-level API for building SSH servers in Go
License:        BSD-3-Clause
URL:            https://github.com/gliderlabs/ssh
#!RemoteAsset:  sha256:ee8f9f5867d00518457d84089e564ba052f860abf18b12a445acbc8f51b0f65e
Source0:        https://github.com/gliderlabs/ssh/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/anmitsu/go-shlex)
BuildRequires:  go(golang.org/x/crypto)

Provides:       go(github.com/gliderlabs/ssh) = %{version}

Requires:       go(github.com/anmitsu/go-shlex)
Requires:       go(golang.org/x/crypto)

%description
gliderlabs/ssh wraps golang.org/x/crypto/ssh with a higher-level API for
building SSH servers, with an API style similar to net/http.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
