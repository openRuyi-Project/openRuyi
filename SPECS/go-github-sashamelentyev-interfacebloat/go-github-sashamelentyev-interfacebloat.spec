# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           interfacebloat
%define go_import_path  github.com/sashamelentyev/interfacebloat

Name:           go-github-sashamelentyev-interfacebloat
Version:        1.1.0
Release:        %autorelease
Summary:        Go analyzer for oversized interfaces
License:        MIT
URL:            https://github.com/sashamelentyev/interfacebloat
#!RemoteAsset:  sha256:77eabfa8cb5f231237630ede028e452be73d1217501e0a6c64efa4567ee11dba
Source0:        https://github.com/sashamelentyev/interfacebloat/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/sashamelentyev/interfacebloat) = %{version}
Provides:       go(github.com/sashamelentyev/interfacebloat/pkg/analyzer) = %{version}

Requires:       go(golang.org/x/tools)

%description
Go analyzer for oversized interfaces.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n interfacebloat-%{version}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/github.com/sashamelentyev/interfacebloat

%changelog
%autochangelog
