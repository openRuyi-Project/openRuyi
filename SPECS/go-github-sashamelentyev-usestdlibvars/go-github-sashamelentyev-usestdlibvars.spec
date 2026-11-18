# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           usestdlibvars
%define go_import_path  github.com/sashamelentyev/usestdlibvars

Name:           go-github-sashamelentyev-usestdlibvars
Version:        1.29.0
Release:        %autorelease
Summary:        Go analyzer for reusable standard library constants
License:        MIT
URL:            https://github.com/sashamelentyev/usestdlibvars
#!RemoteAsset:  sha256:ad57e307c5b086720f5b49356d3bc19443ae2221466ce513aebabd5c9e81f0af
Source0:        https://github.com/sashamelentyev/usestdlibvars/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/sashamelentyev/usestdlibvars) = %{version}
Provides:       go(github.com/sashamelentyev/usestdlibvars/pkg/analyzer) = %{version}
Provides:       go(github.com/sashamelentyev/usestdlibvars/pkg/analyzer/internal/mapping) = %{version}

Requires:       go(golang.org/x/tools)

%description
Go analyzer for reusable standard library constants.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n usestdlibvars-%{version}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/github.com/sashamelentyev/usestdlibvars

%changelog
%autochangelog
