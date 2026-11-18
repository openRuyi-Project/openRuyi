# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           sys
%define go_import_path  golang.org/x/sys
%define go_test_ignore_failure 1

Name:           go-golang-x-sys
Version:        0.48.0
Release:        %autorelease
Summary:        Go packages for low-level interaction with the operating system
License:        BSD-3-Clause
URL:            https://golang.org/x/sys
VCS:            git:https://github.com/golang/sys
#!RemoteAsset:  sha256:687396efb3a2f3903c04f8b8fd012e2f11549e4ac8cd9ec23ef1fa7ef1e074a3
Source0:        https://github.com/golang/sys/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(golang.org/x/sys) = %{version}
Provides:       go(golang.org/x/sys/unix) = %{version}
Provides:       go(golang.org/x/sys/windows) = %{version}

%description
This repository provides supplemental Go packages for low-level interactions with
the operating system.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
