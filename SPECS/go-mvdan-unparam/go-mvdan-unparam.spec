# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           unparam
%define go_import_path  mvdan.cc/unparam
%define commit_id       7a2c2c0b7aa6c1dfb67b52d5f6c7d873caf30215

Name:           go-mvdan-unparam
Version:        0+git20261022.7a2c2c0
Release:        %autorelease
Summary:        Go analyzer for unused function parameters
License:        BSD-3-Clause
URL:            https://github.com/mvdan/unparam
#!RemoteAsset:  sha256:ab6fecc4af34e734f3c601379db9b63e94214d5792be17025d0919acd836edf7
Source0:        https://github.com/mvdan/unparam/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n unparam-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/rogpeppe/go-internal)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(mvdan.cc/unparam) = %{version}
Provides:       go(mvdan.cc/unparam/check) = %{version}

Requires:       go(golang.org/x/tools)

%description
Go analyzer for unused function parameters.
This package contains the complete upstream source repository and test data.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
