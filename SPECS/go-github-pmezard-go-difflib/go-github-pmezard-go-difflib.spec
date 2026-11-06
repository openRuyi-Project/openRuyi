# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-difflib
%define go_import_path  github.com/pmezard/go-difflib
%define commit_id       5d4384ee4fb2527b0a1256a821ebfc92f91efefc

Name:           go-github-pmezard-go-difflib
Version:        1.0.1+git20260721.5d4384e
Release:        %autorelease
Summary:        Partial port of Python difflib package to Go
License:        BSD-3-Clause
URL:            https://github.com/pmezard/go-difflib
#!RemoteAsset:  sha256:b53328c5679cc43d5bac8f0a149b7754f6915fa07533aef904a29e9889264d20
Source0:        https://github.com/pmezard/go-difflib/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Go vet reports non-constant fmt.Printf calls in upstream tests.
# - HNO3Miracle
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/pmezard/go-difflib) = %{version}
Provides:       go(github.com/pmezard/go-difflib/difflib) = %{version}

%description
Go-difflib is a partial port of python 3 difflib package. Its main goal
was to make unified and context diff available in pure Go, mostly for
testing purposes.

The following class and functions (and related tests) have be ported:

 * SequenceMatcher
 * unified_diff()
 * context_diff()

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
