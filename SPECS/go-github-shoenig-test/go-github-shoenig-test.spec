# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           test
%define go_import_path  github.com/shoenig/test
# Test failure, may be cause by outdate code - Julian
%define go_test_ignore_failure 1

Name:           go-github-shoenig-test
Version:        1.12.2
Release:        %autorelease
Summary:        A modern generic testing assertions library for Go
License:        MPL-2.0
URL:            https://github.com/shoenig/test
#!RemoteAsset
Source0:        https://github.com/shoenig/test/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)

Provides:       go(github.com/shoenig/test) = %{version}

Requires:       go(github.com/google/go-cmp)

%description
test is a modern and generics oriented testing assertions library for
Go.

There are five key packages,

 * must - assertions causing test failure and halt the test case
   immediately
 * test - assertions causing test failure and allow the test case to
   continue
 * wait - utilities for waiting on conditionals in tests
 * skip - utilities for skipping test cases in some situations
 * util - utilities for writing concise tests, e.g. managing temp files
 * portal - utilities for allocating free ports for network listeners in
   tests

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
