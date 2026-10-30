# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           stun
%define go_import_path  github.com/pion/stun

Name:           go-github-pion-stun
Version:        0.6.1
Release:        %autorelease
Summary:        A Go implementation of STUN
License:        MIT
URL:            https://github.com/pion/stun
#!RemoteAsset:  sha256:6abda07e177b9f65412e3b11dae6a35663869ebecd2d6511281850c93d8f9e59
Source0:        https://github.com/pion/stun/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/pion/dtls/v2)
BuildRequires:  go(github.com/pion/logging)
BuildRequires:  go(github.com/pion/transport/v2)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/pion/stun) = %{version}

Requires:       go(github.com/pion/dtls/v2)
Requires:       go(github.com/pion/logging)
Requires:       go(github.com/pion/transport/v2)

%description
Package stun implements Session Traversal Utilities for NAT (STUN) (RFC 5389)
protocol and client with no external dependencies and zero allocations in hot
paths. Client supports automatic request retransmissions.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
