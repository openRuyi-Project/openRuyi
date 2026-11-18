# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           predeclared
%define go_import_path  github.com/nishanths/predeclared

Name:           go-github-nishanths-predeclared
Version:        0.3.1
Release:        %autorelease
Summary:        Command predeclared applies the predeclared static analysis to the specified Go packages
License:        BSD-3-Clause
URL:            https://github.com/nishanths/predeclared
#!RemoteAsset:  sha256:eefcbca96105ea5d285c41c7dbb8262d540ed955cdb1d13fb45773165d564251
Source0:        https://github.com/nishanths/predeclared/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/nishanths/predeclared) = %{version}
Provides:       go(github.com/nishanths/predeclared/internal/driver) = %{version}
Provides:       go(github.com/nishanths/predeclared/passes/predeclared) = %{version}

Requires:       go(golang.org/x/tools)

%description
Command predeclared applies the predeclared static analysis to the specified Go packages.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n predeclared-%{version}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/github.com/nishanths/predeclared

%changelog
%autochangelog
