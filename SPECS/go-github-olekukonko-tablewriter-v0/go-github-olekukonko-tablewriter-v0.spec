# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           tablewriter
%define go_import_path  github.com/olekukonko/tablewriter

Name:           go-github-olekukonko-tablewriter-v0
Version:        0.0.5
Release:        %autorelease
Summary:        ASCII table in golang
License:        MIT
URL:            https://github.com/olekukonko/tablewriter
#!RemoteAsset
Source0:        https://github.com/olekukonko/tablewriter/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/mattn/go-runewidth)

Conflicts:      go(github.com/olekukonko/tablewriter) >= 1.0.0

Provides:       go(github.com/olekukonko/tablewriter) = %{version}

Requires:       go(github.com/mattn/go-runewidth)

%description
tablewriter is a Go library for generating **rich text-based tables**
with support for multiple output formats, including ASCII, Unicode,
Markdown, HTML, and colorized terminals. Perfect for CLI tools, logs,
and web applications.

This is the legacy version of tablewriter.


%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
