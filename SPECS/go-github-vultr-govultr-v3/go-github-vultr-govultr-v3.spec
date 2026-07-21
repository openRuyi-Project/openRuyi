# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           govultr
%define go_import_path  github.com/vultr/govultr/v3

Name:           go-github-vultr-govultr-v3
Version:        3.32.0
Release:        %autorelease
Summary:        Vultr API client for Go
License:        MIT
URL:            https://github.com/vultr/govultr
#!RemoteAsset:  sha256:30725b6bb3b971a6e96d16971825e2b71c653b4034e21ad589e8ae4288d8e7c0
Source0:        https://github.com/vultr/govultr/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-querystring)
BuildRequires:  go(github.com/hashicorp/go-retryablehttp)

Provides:       go(github.com/vultr/govultr/v3) = %{version}

Requires:       go(github.com/google/go-querystring)
Requires:       go(github.com/hashicorp/go-retryablehttp)

%description
This package provides version 3 of the Vultr public API client for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
