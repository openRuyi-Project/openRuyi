# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           termenv
%define go_import_path  github.com/muesli/termenv
# TODO: test dependency need too much dependency, add it later - Julian
%define go_test_ignore_failure 1

Name:           go-github-muesli-termenv
Version:        0.16.0
Release:        %autorelease
Summary:        Advanced ANSI style & color support for your terminal applications
License:        MIT
URL:            https://github.com/muesli/termenv
#!RemoteAsset
Source0:        https://github.com/muesli/termenv/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/aymanbagabas/go-osc52)
BuildRequires:  go(github.com/lucasb-eyer/go-colorful)
BuildRequires:  go(github.com/mattn/go-isatty)
BuildRequires:  go(github.com/rivo/uniseg)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/muesli/termenv) = %{version}

Requires:       go(github.com/aymanbagabas/go-osc52)
Requires:       go(github.com/lucasb-eyer/go-colorful)
Requires:       go(github.com/mattn/go-isatty)
Requires:       go(github.com/rivo/uniseg)
Requires:       go(golang.org/x/sys)

%description
termenv lets you safely use advanced styling options on the terminal. It
gathers information about the terminal environment in terms of its ANSI
& color support and offers you convenient methods to colorize and style
your output, without you having to deal with all kinds of weird ANSI
escape sequences and color conversions.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
