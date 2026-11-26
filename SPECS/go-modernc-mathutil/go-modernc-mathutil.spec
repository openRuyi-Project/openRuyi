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
#!RemoteAsset:  git+https://gitlab.com/cznic/mathutil.git#28129eec384c30a304561c3c8779e4bb29cbff12
#!CreateArchive
Source0:        %{_name}-%{version}.tar.gz
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
