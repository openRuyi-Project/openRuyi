# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           exptostd
%define go_import_path  github.com/ldez/exptostd

Name:           go-github-ldez-exptostd
Version:        0.4.5
Release:        %autorelease
Summary:        It is an analyzer that detects functions from golang.org/x/exp/ that can be replaced by std functions
License:        Apache-2.0
URL:            https://github.com/ldez/exptostd
#!RemoteAsset:  sha256:64efc74f79cc494fdece3a2dbdc68ecd75798caf478b0a5a2b01543d4183cf25
Source0:        https://github.com/ldez/exptostd/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/exp)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/ldez/exptostd) = %{version}

Requires:       go(golang.org/x/tools)

%description
It is an analyzer that detects functions from golang.org/x/exp/ that can be replaced by std functions.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n exptostd-%{version}

%files
%doc readme.md
%license LICENSE
%{go_sys_gopath}/github.com/ldez/exptostd

%changelog
%autochangelog
