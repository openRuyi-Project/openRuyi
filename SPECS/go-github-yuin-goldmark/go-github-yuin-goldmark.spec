# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           goldmark
%define go_import_path  github.com/yuin/goldmark

Name:           go-github-yuin-goldmark
Version:        1.7.14
Release:        %autorelease
Summary:        A markdown parser written in Go. Easy to extend, standard(CommonMark) compliant, well structured.
License:        MIT
URL:            https://github.com/yuin/goldmark
#!RemoteAsset
Source0:        https://github.com/yuin/goldmark/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}
BuildOption(check):  -short

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/yuin/goldmark) = %{version}

%description
A Markdown parser written in Go. Easy to extend, standards-compliant,
well-structured.

Features

 * **Standards-compliant.**  goldmark is fully compliant with the latest
   CommonMark (https://commonmark.org/) specification.
 * **Extensible.**  Do you want to add a @username mention syntax to
   Markdown?
   You can easily do so in goldmark. You can add your AST nodes,
   parsers for block-level elements, parsers for inline-level elements,
   transformers for paragraphs, transformers for the whole AST structure,
   and
   renderers.
 * **Performance.**  goldmark's performance is on par with that of cmark,
   the CommonMark reference implementation written in C.
 * **Robust.**  goldmark is tested with go test --fuzz.
 * **Built-in extensions.**  goldmark ships with common extensions like
   tables, strikethrough,
   task lists, and definition lists.
 * **Depends only on standard libraries.**

%files
%license LICENSE*
%doc README*
%{_datadir}/gocode/src/%{go_import_path}

%changelog
%autochangelog
