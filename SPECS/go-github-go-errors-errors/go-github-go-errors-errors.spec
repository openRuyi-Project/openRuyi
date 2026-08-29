# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           errors
%define go_import_path  github.com/go-errors/errors

Name:           go-github-go-errors-errors
Version:        1.5.1
Release:        %autorelease
Summary:        Errors with stacktraces for Go
License:        MIT
URL:            https://github.com/go-errors/errors
#!RemoteAsset:  sha256:b58594dbf9a8b7389ea5f03a8d35d25fd0620f4680341b68bceed43a43823aaf
Source0:        https://github.com/go-errors/errors/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Go 1.25 vet rejects upstream non-constant Errorf strings and old-style examples.
# - HNO3Miracle
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/go-errors/errors) = %{version}

%description
Package errors adds stacktrace support to errors in go.

This is particularly useful when you want to understand the state of
execution when an error was returned unexpectedly.

%files
%doc README.md
%license LICENSE.MIT
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
