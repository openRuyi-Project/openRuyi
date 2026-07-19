# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-pretty
%define go_import_path  github.com/jedib0t/go-pretty/v6

Name:           go-github-jedib0t-go-pretty-v6
Version:        6.8.1
Release:        %autorelease
Summary:        Table-writer and more in golang
License:        MIT
URL:            https://github.com/jedib0t/go-pretty
#!RemoteAsset:  sha256:565f47f897c082acd54b0ad44db25940d4f647483660e5292dbedd20cd7235fb
Source0:        %{url}/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

# Disable Go vet for upstream tests and demos that pass dynamic strings to formatting APIs. - Jvle
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/mattn/go-runewidth)
BuildRequires:  go(github.com/pkg/profile)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/term)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  tzdata

Provides:       go(github.com/jedib0t/go-pretty/v6) = %{version}

Requires:       go(github.com/mattn/go-runewidth)
Requires:       go(github.com/pkg/profile)
Requires:       go(github.com/stretchr/testify)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/term)
Requires:       go(golang.org/x/text)

%description
Utilities to prettify console output of tables, lists,
progress bars, text, and more with a heavy emphasis on
customization and flexibility.

%files
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
