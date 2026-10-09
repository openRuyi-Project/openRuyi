# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           table
%define go_import_path  github.com/rodaine/table

Name:           go-github-rodaine-table
Version:        1.4.0
Release:        %autorelease
Summary:        Go library for simple terminal tables
License:        MIT
URL:            https://github.com/rodaine/table
VCS:            git:https://github.com/rodaine/table
#!RemoteAsset:  sha256:83c5ff178b1bcb6b40dc8800b0702801938d9ce79188b5a24e3a608b639b4f7a
Source0:        https://github.com/rodaine/table/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/mattn/go-runewidth)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/rodaine/table) = %{version}

Requires:       go(github.com/mattn/go-runewidth)

%description
Table is a small Go library for generating simple, lightweight tables
for terminal output.

%files
%doc readme.md
%license license
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
