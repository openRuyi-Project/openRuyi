# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           noctx
%define go_import_path  github.com/sonatard/noctx

Name:           go-github-sonatard-noctx
Version:        0.5.1
Release:        %autorelease
Summary:        Noctx finds function calls without context.Context
License:        MIT
URL:            https://github.com/sonatard/noctx
#!RemoteAsset:  sha256:3ad2658b76baab0e6406fdde8cce5f6a4d8ec76f66aa3e33a70f1a2532f324d9
Source0:        https://github.com/sonatard/noctx/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/gostaticanalysis/analysisutil)
BuildRequires:  go(github.com/gostaticanalysis/comment)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/sonatard/noctx) = %{version}

Requires:       go(github.com/gostaticanalysis/analysisutil)
Requires:       go(golang.org/x/tools)

%description
Noctx finds function calls without context.Context.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n noctx-%{version}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/github.com/sonatard/noctx

%changelog
%autochangelog
