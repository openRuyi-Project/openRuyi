# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gods
%define go_import_path  github.com/emirpasic/gods

Name:           go-github-emirpasic-gods
Version:        1.18.1
Release:        %autorelease
Summary:        GoDS (Go Data Structures) - Sets, Lists, Stacks, Maps, Trees, Queues, and much more
License:        BSD-2-Clause AND ISC
URL:            https://github.com/emirpasic/gods
#!RemoteAsset
Source0:        https://github.com/emirpasic/gods/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/emirpasic/gods) = %{version}

%description
Implementation of various data structures and algorithms in Go.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
