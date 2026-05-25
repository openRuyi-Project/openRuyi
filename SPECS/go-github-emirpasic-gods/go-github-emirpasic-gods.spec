# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gods
%define go_import_path  github.com/emirpasic/gods

Name:           go-github-emirpasic-gods
Version:        1.18.1
Release:        %autorelease
Summary:        Go data structures and algorithms
License:        BSD-2-Clause AND ISC
URL:            https://github.com/emirpasic/gods
#!RemoteAsset:  sha256:741fb139fc74b20c0e5eae63a0a5ee0646019953b15955ac4505f1dd5dded104
Source0:        https://github.com/emirpasic/gods/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/emirpasic/gods) = %{version}

%description
Implementation of various data structures and algorithms in Go.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
