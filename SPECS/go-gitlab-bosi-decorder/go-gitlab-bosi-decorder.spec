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
#!RemoteAsset:  git+https://gitlab.com/bosi/decorder.git#1590c2504b32b4e93de792936d91cfca4308cf53
#!CreateArchive
Source0:        %{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Go 1.27 vet requires a constant format string for Reportf.
Patch2000:      2000-use-constant-format-for-reportf.patch

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
