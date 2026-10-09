# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: tangyihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           hcloud-go
%define go_import_path  github.com/hetznercloud/hcloud-go/v2

Name:           go-github-hetznercloud-hcloud-go-v2
Version:        2.49.0
Release:        %autorelease
Summary:        A Go library for the Hetzner Cloud API
License:        MIT
URL:            https://github.com/hetznercloud/hcloud-go
#!RemoteAsset:  sha256:0e45fa957760b31c671b0bbacd40158989c527fea1b254341c20c7f26da796d9
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
