# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-difflib
%define go_import_path  github.com/pmezard/go-difflib

Name:           go-github-pmezard-go-difflib
Version:        1.0.0
Release:        %autorelease
Summary:        Partial port of Python difflib package to Go
License:        BSD-3-Clause
URL:            https://github.com/pmezard/go-difflib
#!RemoteAsset
Source0:        https://github.com/pmezard/go-difflib/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/pmezard/go-difflib) = %{version}

%description
Go-difflib is a partial port of python 3 difflib package. Its main goal
was to make unified and context diff available in pure Go, mostly for
testing purposes.

The following class and functions (and related tests) have be ported:

 * SequenceMatcher
 * unified_diff()
 * context_diff()

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
