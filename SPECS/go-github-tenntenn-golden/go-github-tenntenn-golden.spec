# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           golden
%define go_import_path  github.com/tenntenn/golden

Name:           go-github-tenntenn-golden
Version:        0.5.5
Release:        %autorelease
Summary:        Utilities for golden file tests
License:        MIT
URL:            https://github.com/tenntenn/golden
#!RemoteAsset:  sha256:9f2e70ea08fbcd8e7a4b6a4fddc8beab7eefeb53e506e68a6108c5c8f7d2e227
Source0:        https://github.com/tenntenn/golden/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp/cmp)
BuildRequires:  go(github.com/google/go-cmp/cmp/cmpopts)
BuildRequires:  go(github.com/josharian/txtarfs)
BuildRequires:  go(golang.org/x/tools/txtar)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/google/go-cmp/cmp)
Requires:       go(github.com/josharian/txtarfs)
Requires:       go(golang.org/x/tools/txtar)

%description
golden provides utilities for comparing and updating golden files.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
