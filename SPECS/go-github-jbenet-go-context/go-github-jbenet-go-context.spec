# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-context
%define go_import_path  github.com/jbenet/go-context
%define commit_id d14ea06fba99483203c19d92cfcd13ebe73135f4

Name:           go-github-jbenet-go-context
Version:        0+git20260601.d14ea06
Release:        %autorelease
Summary:        Context extension helpers for Go
License:        MIT
URL:            https://github.com/jbenet/go-context
#!RemoteAsset:  sha256:5a66b28a0649053468e019573cc3783c53f6c96360947a20b37fba86d4a7d6d0
Source0:        https://github.com/jbenet/go-context/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/net)

Provides:       go(github.com/jbenet/go-context) = %{version}

Requires:       go(golang.org/x/net)

%description
go-context provides helper packages extending Go context usage, including
deadline helpers and context-aware I/O wrappers.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
