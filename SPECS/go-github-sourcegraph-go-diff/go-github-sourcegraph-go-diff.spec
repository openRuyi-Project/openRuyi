# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-diff
%define go_import_path  github.com/sourcegraph/go-diff

Name:           go-github-sourcegraph-go-diff
Version:        0.9.0
Release:        %autorelease
Summary:        Parse and print unified diffs in Go
License:        MIT
URL:            https://github.com/sourcegraph/go-diff
#!RemoteAsset:  sha256:0edcd3bb269d407d5889b7a6776d2f3d87ac29ad506b44006f41cfde1edd427b
Source0:        https://github.com/sourcegraph/go-diff/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)

Provides:       go(github.com/sourcegraph/go-diff) = %{version}
Provides:       go(github.com/sourcegraph/go-diff/diff) = %{version}

Requires:       go(github.com/google/go-cmp)

%description
This library parses and prints unified diff files, including Git extended
headers and multi-file patches.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
