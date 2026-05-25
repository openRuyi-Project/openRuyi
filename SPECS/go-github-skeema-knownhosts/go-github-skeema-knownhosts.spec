# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           knownhosts
%define go_import_path  github.com/skeema/knownhosts

Name:           go-github-skeema-knownhosts
Version:        1.3.2
Release:        %autorelease
Summary:        Enhanced known_hosts management for Go SSH
License:        Apache-2.0
URL:            https://github.com/skeema/knownhosts
#!RemoteAsset:  sha256:80e0892ca8108e20b6de6f6f531f526b9953c704127c4330cbb886762af3d681
Source0:        https://github.com/skeema/knownhosts/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/crypto)

Provides:       go(github.com/skeema/knownhosts) = %{version}

Requires:       go(golang.org/x/crypto)

%description
knownhosts provides higher-level management helpers for OpenSSH known_hosts
files on top of Go's SSH knownhosts support.

%files
%doc README.md
%doc CONTRIBUTING.md
%license LICENSE
%license NOTICE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
