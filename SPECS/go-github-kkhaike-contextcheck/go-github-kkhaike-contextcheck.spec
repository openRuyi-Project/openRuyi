# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           contextcheck
%define go_import_path  github.com/kkHAIKE/contextcheck

Name:           go-github-kkhaike-contextcheck
Version:        1.1.6
Release:        %autorelease
Summary:        Go analyzer for context propagation
License:        Apache-2.0
URL:            https://github.com/kkHAIKE/contextcheck
#!RemoteAsset:  sha256:4a3ffda677d1fb67b39b33688607e6a3bfb31a5fb393ee1ba7a0ed74f9b71a1a
Source0:        https://github.com/kkHAIKE/contextcheck/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/gostaticanalysis/analysisutil)
BuildRequires:  go(github.com/gostaticanalysis/comment)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/kkHAIKE/contextcheck) = %{version}

Requires:       go(github.com/gostaticanalysis/analysisutil)
Requires:       go(golang.org/x/tools)

%description
Go analyzer for context propagation.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n contextcheck-%{version}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/github.com/kkHAIKE/contextcheck

%changelog
%autochangelog
