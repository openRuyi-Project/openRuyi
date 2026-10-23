# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-git-fixtures
%define go_import_path  github.com/go-git/go-git-fixtures/v6

Name:           go-github-go-git-go-git-fixtures-v6
Version:        6.0.0~alpha1
Release:        %autorelease
Summary:        Git repository fixtures for go-git
License:        Apache-2.0
URL:            https://github.com/go-git/go-git-fixtures
#!RemoteAsset:  sha256:49026c35604594fd2cdcf64e9604f5cf7758d4fcf19f6136decb1baa8a277f3e
Source0:        https://github.com/go-git/go-git-fixtures/archive/v6.0.0-alpha.1.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-6.0.0-alpha.1

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-git/go-billy/v6)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/go-git/go-git-fixtures/v6) = %{version}

Requires:       go(github.com/go-git/go-billy/v6)

%description
Embedded Git repository fixtures and helpers used by the go-git test suites.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
