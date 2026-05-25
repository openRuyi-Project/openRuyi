# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           difflib
%define go_import_path  github.com/pmezard/go-difflib
%define commit_id 5d4384ee4fb2527b0a1256a821ebfc92f91efefc

Name:           go-github-pmezard-go-difflib-difflib
Version:        0+git20181226.5d4384e
Release:        %autorelease
Summary:        Unified and context diff library for Go
License:        BSD-3-Clause
URL:            https://github.com/pmezard/go-difflib
#!RemoteAsset:  sha256:b53328c5679cc43d5bac8f0a149b7754f6915fa07533aef904a29e9889264d20
Source0:        https://github.com/pmezard/go-difflib/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Go 1.25 vet rejects non-constant format strings in upstream tests.
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/pmezard/go-difflib/difflib) = %{version}

%description
This package provides helpers for producing unified and context diffs in Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
