# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           nestif
%define go_import_path  github.com/nakabonne/nestif

Name:           go-github-nakabonne-nestif
Version:        0.3.1
Release:        %autorelease
Summary:        Provides an API to detect complex nested if statements
License:        BSD-2-Clause
URL:            https://github.com/nakabonne/nestif
#!RemoteAsset:  sha256:aaec7b719a18be653e8e1d42ec5dbe1a1e16366202abb2bb9e1ff32f5af6a869
Source0:        https://github.com/nakabonne/nestif/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/spf13/pflag)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/nakabonne/nestif) = %{version}

Requires:       go(github.com/spf13/pflag)

%description
Provides an API to detect complex nested if statements.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n nestif-%{version}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/github.com/nakabonne/nestif

%changelog
%autochangelog
