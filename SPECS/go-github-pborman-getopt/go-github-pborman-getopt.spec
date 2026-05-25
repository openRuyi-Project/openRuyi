# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           getopt
%define go_import_path  github.com/pborman/getopt

Name:           go-github-pborman-getopt
Version:        1.1.0
Release:        %autorelease
Summary:        getopt style option parsing for Go
License:        BSD-3-Clause
URL:            https://github.com/pborman/getopt
#!RemoteAsset:  sha256:3018d7168bcafe3e8da21dab9e236cf4d8d6fa80691fb86e19b0d26ef1688567
Source0:        https://github.com/pborman/getopt/archive/refs/tags/v1.1.0.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

Patch2000:      2000-fix-non-constant-fprintf-format.patch

BuildOption(prep):  -n getopt-1.1.0
# Nested Go modules have their own module path/dependencies; skip them in %check
# so the parent package does not try to test unrelated internal tools.
%define go_test_exclude_glob %{go_import_path}/v2*

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/pborman/getopt) = %{version}


%description
getopt [Image: build status] (https://travis-
ci.org/pborman/getopt.svg?branch=master)

Package getopt provides traditional getopt processing for implementing
commands that use traditional command lines.  The standard Go flag
package cannot be used to write a program that parses flags the way ls
or ssh does, for example.  There are two versions, v1 and v2, both named
getopt, that use the following import paths:

  	"github.com/pborman/getopt"     // version 1
  	"github.com/pborman/getopt/v2"  // version 2

%files
%doc README.md
%doc CONTRIBUTING.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}
# Nested Go modules are packaged separately; do not let this module own
# their source directories, otherwise RPM can hit file conflicts.
%exclude %{go_sys_gopath}/%{go_import_path}/v2

%changelog
%autochangelog
