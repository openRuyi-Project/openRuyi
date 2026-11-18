# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-errorlint
%define go_import_path  codeberg.org/polyfloyd/go-errorlint

Name:           go-codeberg-polyfloyd-go-errorlint
Version:        1.9.0
Release:        %autorelease
Summary:        Go analyzer for error wrapping and comparisons
License:        MIT
URL:            https://codeberg.org/polyfloyd/go-errorlint
#!RemoteAsset:  sha256:de8a4f504965d9db00d5b1b39d50a4ec97d8725813957adf3cddbee1901139c4
Source0:        https://codeberg.org/polyfloyd/go-errorlint/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n go-errorlint

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(codeberg.org/polyfloyd/go-errorlint) = %{version}
Provides:       go(codeberg.org/polyfloyd/go-errorlint/errorlint) = %{version}

Requires:       go(golang.org/x/tools)

%description
Go analyzer for error wrapping and comparisons.
This package contains the complete upstream source repository and test data.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
