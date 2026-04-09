# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           arch
%define go_import_path  golang.org/x/arch
# TODO: https://github.com/golang/go/issues/73682
# And this is noarch so globally disable test failure
%define go_test_ignore_failure 1

Name:           go-golang-x-arch
Version:        0.23.0
Release:        %autorelease
Summary:        Go supplementary cryptography libraries
License:        BSD-3-Clause
URL:            https://golang.org/x/arch
VCS:            git:https://github.com/golang/arch
#!RemoteAsset
Source0:        https://github.com/golang/arch/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}
BuildOption(check):  -short

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(rsc.io/pdf)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/term)

Provides:       go(golang.org/x/arch) = %{version}

Requires:       go(rsc.io/pdf)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/term)

%description
This repository holds supplementary Go cryptography packages.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
