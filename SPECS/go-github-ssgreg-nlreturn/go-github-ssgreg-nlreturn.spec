# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           nlreturn
%define go_import_path  github.com/ssgreg/nlreturn/v2

Name:           go-github-ssgreg-nlreturn
Version:        2.2.1
Release:        %autorelease
Summary:        Go analyzer for spacing before return and branch statements
License:        MIT
URL:            https://github.com/ssgreg/nlreturn
#!RemoteAsset:  sha256:851be9d1c0d971835030c301d576c6ddbcaba97442e9d5044731548e3f6b3dd4
Source0:        https://github.com/ssgreg/nlreturn/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/ssgreg/nlreturn/v2) = %{version}
Provides:       go(github.com/ssgreg/nlreturn/v2/pkg/nlreturn) = %{version}

Requires:       go(golang.org/x/tools)

%description
Go analyzer for spacing before return and branch statements.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n nlreturn-%{version}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/github.com/ssgreg/nlreturn/v2

%changelog
%autochangelog
