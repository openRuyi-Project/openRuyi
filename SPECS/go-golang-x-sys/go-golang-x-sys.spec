# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           sys
%define go_import_path  golang.org/x/sys
%define go_test_ignore_failure 1

Name:           go-golang-x-sys
Version:        0.39.0
Release:        %autorelease
Summary:        Go packages for low-level interaction with the operating system
License:        BSD-3-Clause
URL:            https://golang.org/x/sys
VCS:            git:https://github.com/golang/sys
#!RemoteAsset
Source0:        https://github.com/golang/sys/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(golang.org/x/sys) = %{version}

%description
This repository provides supplemental Go packages for low-level interactions with
the operating system.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
