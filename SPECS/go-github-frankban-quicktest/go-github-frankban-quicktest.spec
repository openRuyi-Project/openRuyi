# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           quicktest
%define go_import_path  github.com/frankban/quicktest

Name:           go-github-frankban-quicktest
Version:        1.14.6
Release:        %autorelease
Summary:        Quick helpers for testing Go applications
License:        MIT
URL:            https://github.com/frankban/quicktest
#!RemoteAsset
Source0:        https://github.com/frankban/quicktest/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/kr/pretty)

Provides:       go(github.com/frankban/quicktest) = %{version}

Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/kr/pretty)

%description
This package quicktest provides a collection of Go helpers for writing
tests.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
