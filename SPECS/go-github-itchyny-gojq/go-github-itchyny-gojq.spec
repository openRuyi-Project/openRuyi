# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gojq
%define go_import_path  github.com/itchyny/gojq

Name:           go-github-itchyny-gojq
Version:        0.12.19
Release:        %autorelease
Summary:        jq parser and interpreter for Go
License:        MIT
URL:            https://github.com/itchyny/gojq
#!RemoteAsset:  sha256:d6c6ecf8b7d9ed892216aee61101e8bc45359dc63d5ba3ab596922c4ea11e1ab
Source0:        https://github.com/itchyny/gojq/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/clipperhouse/stringish)
BuildRequires:  go(github.com/clipperhouse/uax29/v2)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/itchyny/go-yaml)
BuildRequires:  go(github.com/itchyny/timefmt-go)
BuildRequires:  go(github.com/mattn/go-isatty)
BuildRequires:  go(github.com/mattn/go-runewidth)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/itchyny/go-yaml)
Requires:       go(github.com/itchyny/timefmt-go)
Requires:       go(github.com/mattn/go-isatty)
Requires:       go(github.com/mattn/go-runewidth)

%description
GoJQ provides a pure Go parser and interpreter for the jq query language and
includes a compatible command-line implementation.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
