# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           exhaustive
%define go_import_path  github.com/nishanths/exhaustive

Name:           go-github-nishanths-exhaustive
Version:        0.16.1
Release:        %autorelease
Summary:        Go analyzer for exhaustive enum switches and maps
License:        BSD-2-Clause AND BSD-3-Clause
URL:            https://github.com/nishanths/exhaustive
#!RemoteAsset:  sha256:e53fcfbb1b11f41ccc82076a21a8f967a1696b9c251c5521ba57ccf38070d220
Source0:        https://github.com/nishanths/exhaustive/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(rsc.io/script)

Provides:       go(github.com/nishanths/exhaustive) = %{version}
Provides:       go(github.com/nishanths/exhaustive/internal/driver) = %{version}
Provides:       go(github.com/nishanths/exhaustive/internal/passes/finder) = %{version}
Provides:       go(github.com/nishanths/exhaustive/passes/enumerated) = %{version}
Provides:       go(github.com/nishanths/exhaustive/passes/exhaustive) = %{version}

Requires:       go(golang.org/x/tools)

%description
Go analyzer for exhaustive enum switches and maps.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n exhaustive-%{version}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/github.com/nishanths/exhaustive

%changelog
%autochangelog
