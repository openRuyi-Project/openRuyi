# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           libc
%define go_import_path  modernc.org/libc
%define go_test_exclude_glob %{go_import_path}*

Name:           go-modernc-libc
Version:        1.73.4
Release:        %autorelease
Summary:        Package libc is a partial reimplementation of C libc in pure Go
License:        BSD-3-Clause
URL:            https://gitlab.com/cznic/libc
#!RemoteAsset:  sha256:611241e59553c1df4fce7c69df800726cbfef438a8f15080e9f12f4701688515
Source0:        https://gitlab.com/cznic/libc/-/archive/v%{version}/libc-v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/dustin/go-humanize)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(modernc.org/mathutil)
BuildRequires:  go(modernc.org/memory)

Provides:       go(modernc.org/libc) = %{version}

Requires:       go(github.com/dustin/go-humanize)
Requires:       go(github.com/google/uuid)
Requires:       go(golang.org/x/sys)
Requires:       go(modernc.org/mathutil)
Requires:       go(modernc.org/memory)

%description
Package libc is a partial reimplementation of C libc in pure Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
