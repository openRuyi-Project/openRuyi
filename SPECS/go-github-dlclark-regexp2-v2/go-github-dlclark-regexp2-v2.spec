# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           regexp2
%define go_import_path  github.com/dlclark/regexp2/v2

Name:           go-github-dlclark-regexp2-v2
Version:        2.9.1
Release:        %autorelease
Summary:        Backtracking regular expression engine for Go, version 2
License:        MIT
URL:            https://github.com/dlclark/regexp2
#!RemoteAsset:  sha256:862c96d1622775484cf65f82e2aaa9aab3012f6a341418fbfc79a28a3e1a9cb6
Source0:        https://github.com/dlclark/regexp2/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/dlclark/regexp2/v2) = %{version}
Provides:       go(github.com/dlclark/regexp2/v2/compat) = %{version}
Provides:       go(github.com/dlclark/regexp2/v2/helpers) = %{version}
Provides:       go(github.com/dlclark/regexp2/v2/syntax) = %{version}

%description
Regexp2 implements a backtracking regular expression engine with
.NET-compatible syntax under the version 2 Go import path.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
