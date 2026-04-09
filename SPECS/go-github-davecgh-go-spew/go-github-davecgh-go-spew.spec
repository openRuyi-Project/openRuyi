# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-spew
%define go_import_path  github.com/davecgh/go-spew

Name:           go-github-davecgh-go-spew
Version:        1.1.1
Release:        %autorelease
Summary:        Implements a deep pretty printer for Go data structures to aid in debugging
License:        ISC
URL:            https://github.com/davecgh/go-spew
#!RemoteAsset
Source0:        https://github.com/davecgh/go-spew/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/davecgh/go-spew) = %{version}

%description
Go-spew implements a deep pretty printer for Go data structures to aid in
debugging.

A comprehensive suite of tests with 100% test coverage is provided
to ensure proper functionality.  See test_coverage.txt for the
gocov coverage report. Go-spew is licensed under the liberal ISC
license, so it may be used in open source or commercial projects.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
