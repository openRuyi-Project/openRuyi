# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-hostpool
%define go_import_path  github.com/bitly/go-hostpool

Name:           go-github-bitly-go-hostpool
Version:        0.1.1
Release:        %autorelease
Summary:        Host pool library for Go
License:        MIT
URL:            https://github.com/bitly/go-hostpool
#!RemoteAsset:  sha256:7fb8b2ec737a76becf80c0fe586ccb4bce4f0479505e1366a5c59d6f59359c49
Source0:        https://github.com/bitly/go-hostpool/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(%{go_import_path}) = %{version}

%description
This package selects hosts using round-robin or epsilon-greedy strategies and
temporarily avoids unresponsive hosts.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
