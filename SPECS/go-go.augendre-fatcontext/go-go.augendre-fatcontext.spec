# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           fatcontext
%define go_import_path  go.augendre.info/fatcontext

Name:           go-go.augendre-fatcontext
Version:        0.10.1
Release:        %autorelease
Summary:        Go analyzer for nested context construction
License:        MIT
URL:            https://github.com/Crocmagnon/fatcontext
#!RemoteAsset:  sha256:455e1c49477bae2c98db6ade61fafdf737db526f16fdf7ff3004f426e0f32a23
Source0:        https://github.com/Crocmagnon/fatcontext/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n fatcontext-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(go.augendre.info/fatcontext) = %{version}
Provides:       go(go.augendre.info/fatcontext/cmd/fatcontext) = %{version}
Provides:       go(go.augendre.info/fatcontext/pkg/analyzer) = %{version}

Requires:       go(golang.org/x/tools)

%description
Go analyzer for nested context construction.
This package contains the complete upstream source repository and test data.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
