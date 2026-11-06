# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           decorder
%define go_import_path  gitlab.com/bosi/decorder

Name:           go-gitlab-bosi-decorder
Version:        0.4.2
Release:        %autorelease
Summary:        Go analyzer for declaration ordering
License:        MIT
URL:            https://gitlab.com/bosi/decorder
#!RemoteAsset:  sha256:5a880c5fcc4a51a1725082bdd0d08767508d2e481fbabf45c4dab34143249927
Source0:        https://gitlab.com/bosi/decorder/-/archive/v%{version}/decorder-v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Go 1.27 vet requires a constant format string for Reportf.
Patch2000:      2000-use-constant-format-for-reportf.patch

BuildOption(prep):  -n decorder-v%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(gitlab.com/bosi/decorder) = %{version}
Provides:       go(gitlab.com/bosi/decorder/cmd/decorder) = %{version}

Requires:       go(golang.org/x/tools)

%description
Go analyzer for declaration ordering.
This package contains the complete upstream source repository and test data.

%files
%doc README.md
%license LICENSE.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
