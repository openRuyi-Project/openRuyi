# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           embeddedstructfieldcheck
%define go_import_path  github.com/manuelarte/embeddedstructfieldcheck

Name:           go-github-manuelarte-embeddedstructfieldcheck
Version:        0.4.0
Release:        %autorelease
Summary:        Linter that checks that embedded types should be at the top of the field list of a struct
License:        Apache-2.0
URL:            https://github.com/manuelarte/embeddedstructfieldcheck
#!RemoteAsset:  sha256:d4e1c3c7b3ee0efd9b23b990587be36dae90363e6cb1279bf1632345d46d184a
Source0:        https://github.com/manuelarte/embeddedstructfieldcheck/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/manuelarte/embeddedstructfieldcheck) = %{version}
Provides:       go(github.com/manuelarte/embeddedstructfieldcheck/analyzer) = %{version}
Provides:       go(github.com/manuelarte/embeddedstructfieldcheck/internal) = %{version}

Requires:       go(golang.org/x/tools)

%description
Linter that checks that embedded types should be at the top of the field list of a struct.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n embeddedstructfieldcheck-%{version}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/github.com/manuelarte/embeddedstructfieldcheck

%changelog
%autochangelog
