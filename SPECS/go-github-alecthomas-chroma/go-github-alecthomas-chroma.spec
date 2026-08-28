# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           chroma
%define go_import_path  github.com/alecthomas/chroma
# Lexer golden files from this old API version differ with current regexp2.
%define go_test_exclude %{go_import_path}/lexers

Name:           go-github-alecthomas-chroma
Version:        0.10.0
Release:        %autorelease
Summary:        General-purpose syntax highlighter for Go
License:        MIT
URL:            https://github.com/alecthomas/chroma
#!RemoteAsset:  sha256:98a517ae99f48e3b54d5c8cd7473d5c544f51bee7a4be17f5175736fce37da56
Source0:        https://github.com/alecthomas/chroma/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/alecthomas/kong)
BuildRequires:  go(github.com/alecthomas/kong-hcl)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/dlclark/regexp2)
BuildRequires:  go(github.com/gorilla/csrf)
BuildRequires:  go(github.com/gorilla/handlers)
BuildRequires:  go(github.com/gorilla/mux)
BuildRequires:  go(github.com/mattn/go-colorable)
BuildRequires:  go(github.com/mattn/go-isatty)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/dlclark/regexp2)

%description
Chroma converts source code and other structured text into syntax-highlighted
HTML, ANSI-colored text, and other output formats.

%check -a
go test -c -o /dev/null %{go_import_path}/lexers

%files
%doc README.md
%license COPYING
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
