# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global _name           go-billy
%define go_import_path  github.com/go-git/go-billy/v6
%global commit_id       37866f83c2d3de721f62787b8b480db26780b72e

Name:           go-github-go-git-go-billy-v6
Version:        5.5.0+git20261023.37866f8
Release:        %autorelease
Summary:        Filesystem abstraction library for Go
License:        Apache-2.0
URL:            https://github.com/go-git/go-billy
#!RemoteAsset:  sha256:ebb486d690c7da3a5bdeb8e416602a0b5526528ef02390c879e961d0817dacd3
Source0:        https://github.com/go-git/go-billy/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/cyphar/filepath-securejoin)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/go-git/go-billy/v6) = %{version}

Requires:       go(github.com/cyphar/filepath-securejoin)
Requires:       go(golang.org/x/sys)

%description
Filesystem interfaces and OS-backed, in-memory and embedded filesystem
implementations used by go-git v6.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
