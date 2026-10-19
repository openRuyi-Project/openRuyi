# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           mathutil
%define go_import_path  modernc.org/mathutil

Name:           go-modernc-mathutil
Version:        1.7.1
Release:        %autorelease
Summary:        utilities supplementing the standard 'math' and 'math/rand' packages
License:        BSD-3-Clause
URL:            https://gitlab.com/cznic/mathutil
#!RemoteAsset:  sha256:78174f3ed1cea720592a31a8fc154278802d3fd8e461a074ed3caad1752f4fb6
Source0:        https://gitlab.com/cznic/mathutil/-/archive/v%{version}/mathutil-v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(check):  -v=false

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/remyoudompheng/bigfft)

Provides:       go(modernc.org/mathutil) = %{version}

Requires:       go(github.com/remyoudompheng/bigfft)

%description
Package mathutil provides utilities supplementing the standard 'math' and
'math/rand' packages.

%files
%doc README
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
