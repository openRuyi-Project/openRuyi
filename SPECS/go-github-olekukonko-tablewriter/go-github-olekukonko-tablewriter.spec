# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           tablewriter
%define go_import_path  github.com/olekukonko/tablewriter

Name:           go-github-olekukonko-tablewriter
Version:        1.1.2
Release:        %autorelease
Summary:        ASCII table in golang
License:        MIT
URL:            https://github.com/olekukonko/tablewriter
#!RemoteAsset
Source0:        https://github.com/olekukonko/tablewriter/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/clipperhouse/displaywidth)
BuildRequires:  go(github.com/clipperhouse/uax29/v2)
BuildRequires:  go(github.com/fatih/color)
BuildRequires:  go(github.com/mattn/go-runewidth)
BuildRequires:  go(github.com/olekukonko/errors)
BuildRequires:  go(github.com/olekukonko/ll)
BuildRequires:  go(github.com/olekukonko/ts)

Conflicts:      go(github.com/olekukonko/tablewriter) = 0.0.5

Provides:       go(github.com/olekukonko/tablewriter) = %{version}

Requires:       go(github.com/clipperhouse/displaywidth)
Requires:       go(github.com/clipperhouse/uax29/v2)
Requires:       go(github.com/fatih/color)
Requires:       go(github.com/mattn/go-runewidth)
Requires:       go(github.com/olekukonko/errors)
Requires:       go(github.com/olekukonko/ll)
Requires:       go(github.com/olekukonko/ts)

%description
Tablewriter is a Go library for generating **rich text-based tables**
with support for multiple output formats, including ASCII, Unicode,
Markdown, HTML, and colorized terminals. Perfect for CLI tools, logs,
and web applications.

Key Features

 * **Multi-format rendering**: ASCII, Unicode, Markdown, HTML, ANSI-
   colored
 * **Advanced styling**: Cell merging, alignment, padding, borders
 * **Flexible input**: CSV, structs, slices, or streaming data
 * **High performance**: Minimal allocations, buffer reuse
 * **Modern features**: Generics support, hierarchical merging, real-
   time streaming

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
