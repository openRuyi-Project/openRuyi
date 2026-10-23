# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-billy
%define go_import_path  github.com/go-git/go-billy/v6

Name:           go-github-go-git-go-billy-v6
Version:        6.0.0~beta1
Release:        %autorelease
Summary:        Filesystem abstraction library for Go
License:        Apache-2.0
URL:            https://github.com/go-git/go-billy
#!RemoteAsset:  sha256:7f39bc28b36ffa41d982c901bc761264f306a325a885243fd3fef0c0f7338330
Source0:        https://github.com/go-git/go-billy/archive/v6.0.0-beta.1.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-6.0.0-beta.1

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/go-git/go-billy/v6) = %{version}

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
