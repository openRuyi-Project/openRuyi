# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           whitespace
%define go_import_path  github.com/ultraware/whitespace

Name:           go-github-ultraware-whitespace
Version:        0.2.0
Release:        %autorelease
Summary:        Whitespace is a linter that checks for unnecessary newlines at the start and end of functions, if, for, etc
License:        MIT
URL:            https://github.com/ultraware/whitespace
#!RemoteAsset:  sha256:7aac712e9b30e031610a320ebef6759448a814d011e22c62a66964ee8aacadba
Source0:        https://github.com/ultraware/whitespace/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/ultraware/whitespace) = %{version}

Requires:       go(golang.org/x/tools)

%description
Whitespace is a linter that checks for unnecessary newlines at the start and end of functions, if, for, etc.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n whitespace-%{version}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/github.com/ultraware/whitespace

%changelog
%autochangelog
