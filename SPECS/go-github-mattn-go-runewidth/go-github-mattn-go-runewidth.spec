# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-runewidth
%define go_import_path  github.com/mattn/go-runewidth

Name:           go-github-mattn-go-runewidth
Version:        0.0.19
Release:        %autorelease
Summary:        wcwidth for golang
License:        MIT
URL:            https://github.com/mattn/go-runewidth
#!RemoteAsset
Source0:        https://github.com/mattn/go-runewidth/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/clipperhouse/uax29/v2)
BuildRequires:  unicode-ucd

Provides:       go(github.com/mattn/go-runewidth) = %{version}

Requires:       go(github.com/clipperhouse/uax29/v2)

%description
go-runewidth Provides functions to get fixed width of the character
or string.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
