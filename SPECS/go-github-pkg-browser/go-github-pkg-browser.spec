# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           browser
%define go_import_path  github.com/pkg/browser
%define commit_id 5ac0b6a4141c771a0d3a081c36b87c977cf9c7db

Name:           go-github-pkg-browser
Version:        0+git20260607.5ac0b6a
Release:        %autorelease
Summary:        Browser opening helpers for Go
License:        BSD-2-Clause
URL:            https://github.com/pkg/browser
#!RemoteAsset:  sha256:3ee8c928b8a2b9b6d6ddebdea40a6350cda5e8647df8008aaccaf0b018f44a3f
Source0:        https://github.com/pkg/browser/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/pkg/browser) = %{version}

%description
This package provides helpers for opening files, readers, and URLs in a browser
window from Go programs.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
