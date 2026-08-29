# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: tangyihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           hcloud-go
%define go_import_path  github.com/hetznercloud/hcloud-go/v2

Name:           go-github-hetznercloud-hcloud-go-v2
Version:        2.42.0
Release:        %autorelease
Summary:        A Go library for the Hetzner Cloud API
License:        MIT
URL:            https://github.com/hetznercloud/hcloud-go
#!RemoteAsset:  sha256:25cfa0ac028ede3b4e7f5970252feff8c0949fe7cc7e6eacb3fc15550ee3683d
Source0:        https://github.com/hetznercloud/hcloud-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/prometheus/client_golang)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/net)

Provides:       go(github.com/hetznercloud/hcloud-go/v2) = %{version}

Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/prometheus/client_golang)
Requires:       go(github.com/stretchr/testify)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/net)

%description
This package provides the Go client library for the Hetzner Cloud API.
It is used by Go programs to manage Hetzner Cloud resources.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
