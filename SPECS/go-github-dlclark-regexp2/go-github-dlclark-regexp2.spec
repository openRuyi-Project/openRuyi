# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           regexp2
%define go_import_path  github.com/dlclark/regexp2

Name:           go-github-dlclark-regexp2
Version:        1.11.5
Release:        %autorelease
Summary:        A full-featured regex engine in pure Go based on the .NET engine
License:        MIT
URL:            https://github.com/dlclark/regexp2
#!RemoteAsset
Source0:        https://github.com/dlclark/regexp2/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# https://sources.debian.org/src/golang-github-dlclark-regexp2/1.11.0%2Bds1-1/debian/patches/0001-increase-timeout-to-10ms.patch
Patch0:         2000-increase-timeout-to-10ms.patch

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/dlclark/regexp2) = %{version}

%description
Regexp2 is a feature-rich RegExp engine for Go.  It doesn't have
constant
time guarantees like the built-in regexp package, but it allows
backtracking and is compatible with Perl5 and .NET.  You'll likely be
better off with the RE2 engine from the regexp package and should only
use this if you need to write very complex patterns or require
compatibility with .NET.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
