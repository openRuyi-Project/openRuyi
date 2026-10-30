# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           sloglint
%define go_import_path  go-simpler.org/sloglint

Name:           go-go-simpler-sloglint
Version:        0.12.0
Release:        %autorelease
Summary:        Go analyzer for structured logging conventions
License:        MPL-2.0
URL:            https://github.com/go-simpler/sloglint
#!RemoteAsset:  sha256:cb968f427f47997f04b5034f9d86eb70d6386a660b77e472112f8b9f8adaa19a
Source0:        https://github.com/go-simpler/sloglint/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n sloglint-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/ettle/strcase)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(go-simpler.org/sloglint) = %{version}
Provides:       go(go-simpler.org/sloglint/cmd/sloglint) = %{version}

Requires:       go(github.com/ettle/strcase)
Requires:       go(golang.org/x/tools)

%description
Go analyzer for structured logging conventions.
This package contains the complete upstream source repository and test data.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
