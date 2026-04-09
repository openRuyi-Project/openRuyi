# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           mod
%define go_import_path  golang.org/x/mod
%define go_test_exclude golang.org/x/mod/zip

Name:           go-golang-x-mod
Version:        0.31.0
Release:        %autorelease
Summary:        Go module mechanics libraries
License:        BSD-3-Clause
URL:            https://golang.org/x/mod
VCS:            git:https://github.com/golang/mod
#!RemoteAsset
Source0:        https://github.com/golang/mod/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}
BuildOption(check):  -test.short

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(golang.org/x/mod) = %{version}

%description
This repository holds packages for writing tools
that work directly with Go module mechanics.
That is, it is for direct manipulation of Go modules themselves.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
