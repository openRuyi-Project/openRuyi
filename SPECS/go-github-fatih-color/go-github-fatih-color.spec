# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           color
%define go_import_path  github.com/fatih/color

Name:           go-github-fatih-color
Version:        1.18.0
Release:        %autorelease
Summary:        Color package for Go (golang)
License:        MIT
URL:            https://github.com/fatih/color
#!RemoteAsset
Source0:        https://github.com/fatih/color/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/mattn/go-colorable)

Provides:       go(github.com/fatih/color)

Requires:       go(github.com/mattn/go-colorable)

%description
Color lets you use colorized outputs in terms of ANSI Escape Codes
(http://en.wikipedia.org/wiki/ANSI_escape_code#Colors) in Go (Golang).
It has support for Windows too! The API can be used in several ways,
pick one that suits you.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
