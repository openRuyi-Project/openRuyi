# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-ansi-parser
%define go_import_path  github.com/leaanthony/go-ansi-parser

Name:           go-github-leaanthony-go-ansi-parser
Version:        1.6.1
Release:        %autorelease
Summary:        ANSI escape sequence parser for Go
License:        MIT
URL:            https://github.com/leaanthony/go-ansi-parser
#!RemoteAsset:  sha256:6fb1280381f9ebe24ae356958116672ec078ae65455f744e93e3c386abd1fe0c
Source0:        https://github.com/leaanthony/go-ansi-parser/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/matryer/is)
BuildRequires:  go(github.com/rivo/uniseg)

Provides:       go(github.com/leaanthony/go-ansi-parser) = %{version}

Requires:       go(github.com/rivo/uniseg)

%description
go-ansi-parser parses ANSI escape sequences and exposes styled text segments
for terminal-oriented Go applications.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
