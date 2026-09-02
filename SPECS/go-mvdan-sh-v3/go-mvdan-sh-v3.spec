# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           sh
%define go_import_path  mvdan.cc/sh/v3
# moreinterp is an independently versioned module outside the sh/v3 module.
%define go_test_exclude_glob %{go_import_path}/moreinterp*

Name:           go-mvdan-sh-v3
Version:        3.13.1
Release:        %autorelease
Summary:        Shell parser, formatter, and interpreter for Go
License:        BSD-3-Clause
URL:            https://github.com/mvdan/sh
#!RemoteAsset:  sha256:b31aad2d4c26b0c6e8ebe894d59022520bbebce33e082d7d29e4325eee35d308
Source0:        https://github.com/mvdan/sh/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Preserve the development version fallback in GOPATH builds.
Patch2000:      2000-Report-devel-for-builds-without-a-module-version.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/creack/pty)
BuildRequires:  go(github.com/go-quicktest/qt)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/renameio/v2)
BuildRequires:  go(github.com/kr/pretty)
BuildRequires:  go(github.com/kr/text)
BuildRequires:  go(github.com/rogpeppe/go-internal)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/term)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(mvdan.cc/editorconfig)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/google/renameio/v2)
Requires:       go(github.com/rogpeppe/go-internal)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/term)
Requires:       go(mvdan.cc/editorconfig)

%description
This package parses, formats, and interprets POSIX shell, Bash, and mksh syntax
and supplies the libraries used by shfmt.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}
%exclude %{go_sys_gopath}/%{go_import_path}/moreinterp

%changelog
%autochangelog
