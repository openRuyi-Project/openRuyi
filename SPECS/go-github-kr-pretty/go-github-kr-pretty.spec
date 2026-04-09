# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           pretty
%define go_import_path  github.com/kr/pretty

Name:           go-github-kr-pretty
Version:        0.3.1
Release:        %autorelease
Summary:        Pretty printing for Go values
License:        MIT
URL:            https://github.com/kr/pretty
#!RemoteAsset
Source0:        https://github.com/kr/pretty/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/kr/text)
BuildRequires:  go(github.com/rogpeppe/go-internal)

Provides:       go(github.com/kr/pretty) = %{version}

Requires:       go(github.com/kr/text)
Requires:       go(github.com/rogpeppe/go-internal)

%description
Go library package github.com/kr/pretty provides pretty-printing
for Go values. This is useful during debugging, to avoid wrapping
long output lines in the terminal.

%files
%license License
%doc Readme
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
