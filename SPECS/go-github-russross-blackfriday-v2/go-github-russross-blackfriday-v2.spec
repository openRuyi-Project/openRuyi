# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           blackfriday
%define go_import_path  github.com/russross/blackfriday/v2

Name:           go-github-russross-blackfriday-v2
Version:        2.1.0
Release:        %autorelease
Summary:        Blackfriday: a markdown processor for Go
License:        BSD
URL:            https://github.com/russross/blackfriday
#!RemoteAsset
Source0:        https://github.com/russross/blackfriday/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}
# go (>=1.12) will run vet by default, but blackfriday has some issues with it
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/russross/blackfriday/v2)

%description
Blackfriday is a Markdown
(https://daringfireball.net/projects/markdown/) processor implemented in
Go (https://golang.org/). It is paranoid about its input (so you can
safely feed it user-supplied data), it is fast, it supports common
extensions (tables, smart punctuation substitutions, etc.), and it is
safe for all utf-8 (unicode) input.

Currently maintained and recommended version of Blackfriday is v2.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
