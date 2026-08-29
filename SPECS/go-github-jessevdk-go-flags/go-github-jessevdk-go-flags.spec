# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-flags
%define go_import_path  github.com/jessevdk/go-flags

Name:           go-github-jessevdk-go-flags
Version:        1.6.1
Release:        %autorelease
Summary:        Go command-line option parser
License:        BSD-3-Clause
URL:            https://github.com/jessevdk/go-flags
#!RemoteAsset:  sha256:01bae681937db1bcab792da59a859392cb55b678c7a3756a18e29a0ff7a462aa
Source0:        https://github.com/jessevdk/go-flags/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Go 1.25 vet rejects an upstream non-constant format string in newErrorf.
# - HNO3Miracle
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/jessevdk/go-flags) = %{version}

Requires:       go(golang.org/x/sys)

%description
This library provides similar functionality to the builtin flag library
of go, but provides much more functionality and nicer formatting.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
