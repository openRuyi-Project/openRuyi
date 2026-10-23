# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global _name           go-git-fixtures
%define go_import_path  github.com/go-git/go-git-fixtures/v5
%global commit_id       0622d7459a67dc7cc1b8a8bb74ce7c3789c156bd

Name:           go-github-go-git-go-git-fixtures-v5
Version:        5.1.1+git20261023.0622d74
Release:        %autorelease
Summary:        Git repository fixtures for go-git
License:        Apache-2.0
URL:            https://github.com/go-git/go-git-fixtures
#!RemoteAsset:  sha256:70f244be4f2640e92c0742ae80602f46f48e98348252d35e3d11042c79332249
Source0:        https://github.com/go-git/go-git-fixtures/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-git/go-billy/v6)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/go-git/go-git-fixtures/v5) = %{version}

Requires:       go(github.com/go-git/go-billy/v6)

%description
Embedded Git repository fixtures and helpers used by the go-git test suites.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
