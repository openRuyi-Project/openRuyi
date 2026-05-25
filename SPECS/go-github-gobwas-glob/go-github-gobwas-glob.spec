# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           glob
%define go_import_path  github.com/gobwas/glob

Name:           go-github-gobwas-glob
Version:        0.2.3
Release:        %autorelease
Summary:        Go glob
License:        MIT
URL:            https://github.com/gobwas/glob
#!RemoteAsset:  sha256:325026fc78bcebcf31151b6e060f4e1c3321b04ded3dab63b63610b323c10850
Source0:        https://github.com/gobwas/glob/archive/refs/tags/v0.2.3.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

Patch2000:      2000-fix-non-constant-fprintf-format.patch

BuildOption(prep):  -n glob-0.2.3

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/gobwas/glob) = %{version}
Provides:       go(github.com/gobwas/glob/compiler) = %{version}
Provides:       go(github.com/gobwas/glob/match) = %{version}
Provides:       go(github.com/gobwas/glob/match/debug) = %{version}
Provides:       go(github.com/gobwas/glob/syntax) = %{version}
Provides:       go(github.com/gobwas/glob/syntax/ast) = %{version}
Provides:       go(github.com/gobwas/glob/syntax/lexer) = %{version}
Provides:       go(github.com/gobwas/glob/util/runes) = %{version}
Provides:       go(github.com/gobwas/glob/util/strings) = %{version}


%description
glob.go (https://golang.org)

[Image: GoDoc] (https://godoc.org/github.com/gobwas/glob?status.svg)
(https://godoc.org/github.com/gobwas/glob) [Image: Build Status]
(https://travis-ci.org/gobwas/glob.svg?branch=master) (https://travis-
ci.org/gobwas/glob)

 | Go Globbing Library.

Install


%files
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
