# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           blackfriday
%define go_import_path  github.com/russross/blackfriday

Name:           go-github-russross-blackfriday
Version:        1.6.0
Release:        %autorelease
Summary:        Blackfriday: a markdown processor for Go
License:        BSD
URL:            https://github.com/russross/blackfriday
#!RemoteAsset
Source0:        https://github.com/russross/blackfriday/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/russross/blackfriday)

%description
Blackfriday is a Markdown
(https://daringfireball.net/projects/markdown/) processor implemented in
Go (https://golang.org/). It is paranoid about its input (so you can
safely feed it user-supplied data), it is fast, it supports common
extensions (tables, smart punctuation substitutions, etc.), and it is
safe for all utf-8 (unicode) input.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
