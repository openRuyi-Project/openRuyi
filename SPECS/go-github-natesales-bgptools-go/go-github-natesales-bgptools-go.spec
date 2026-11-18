# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           bgptools-go
%define go_import_path  github.com/natesales/bgptools-go
%define commit_id       2b519d61269c327e654b24a72b28850074badc2a

Name:           go-github-natesales-bgptools-go
Version:        0+git20261118.2b519d6
Release:        %autorelease
Summary:        Go interface for bgp.tools WHOIS API
License:        GPL-3.0-only
URL:            https://github.com/natesales/bgptools-go
#!RemoteAsset:  sha256:01e59ec26f24d90f4f6451ff96ebac9710975f6443146bdc5b06a30c9839f481
Source0:        https://github.com/natesales/bgptools-go/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/natesales/bgptools-go) = %{version}

%description
Go interface for the bgp.tools WHOIS API.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
