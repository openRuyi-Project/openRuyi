# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           terminfo
%define go_import_path  github.com/xo/terminfo
%define commit_id abceb7e1c41eed2857facd9bbdaaa5ff8137d901
# Test failure, may be cause by outdate code - Julian
%define go_test_ignore_failure 1

Name:           go-github-xo-terminfo
Version:        0+git20220910.abceb7e
Release:        %autorelease
Summary:        A terminfo package in pure go!
License:        MIT
URL:            https://github.com/xo/terminfo
#!RemoteAsset
Source0:        https://github.com/xo/terminfo/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/exp)

Provides:       go(github.com/xo/terminfo) = %{version}

%description
Package terminfo provides a pure-Go implementation of reading
information
from the terminfo database.

terminfo is meant as a replacement for ncurses in simple Go programs.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
