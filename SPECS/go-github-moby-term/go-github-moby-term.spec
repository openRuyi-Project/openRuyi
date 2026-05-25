# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           term
%define go_import_path  github.com/moby/term

Name:           go-github-moby-term
Version:        0.5.2
Release:        %autorelease
Summary:        Terminal handling helpers from Moby
License:        Apache-2.0
URL:            https://github.com/moby/term
#!RemoteAsset:  sha256:59e529a9312d119489e081dd1ac56fc3e27ff4e4a7ea4df49430261aa570f472
Source0:        https://github.com/moby/term/archive/refs/tags/v0.5.2.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n term-0.5.2

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/creack/pty)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/sys/unix)

Provides:       go(github.com/moby/term) = %{version}
Provides:       go(github.com/moby/term/windows) = %{version}

Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/sys/unix)


%description
term - utilities for dealing with terminals

[Image: Test] (https://github.com/moby/term/workflows/Test/badge.svg)
[Image: GoDoc] (https://godoc.org/github.com/moby/term?status.svg)
(https://godoc.org/github.com/moby/term) [Image: Go Report Card]
(https://goreportcard.com/badge/github.com/moby/term)
(https://goreportcard.com/report/github.com/moby/term)

term provides structures and helper functions to work with terminal
(state, sizes).


%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
