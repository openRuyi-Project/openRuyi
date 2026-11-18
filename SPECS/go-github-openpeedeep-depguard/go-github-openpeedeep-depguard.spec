# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           depguard
%define go_import_path  github.com/OpenPeeDeeP/depguard/v2

Name:           go-github-openpeedeep-depguard
Version:        2.2.1
Release:        %autorelease
Summary:        A Go linter that checks package imports are in a list of acceptable packages
License:        GPL-3.0-only
URL:            https://github.com/OpenPeeDeeP/depguard
#!RemoteAsset:  sha256:834ada68442dc0b896696d178d829ccba81902a29822c9b7ab75cd3c9512e1a3
Source0:        https://github.com/OpenPeeDeeP/depguard/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/BurntSushi/toml)
BuildRequires:  go(github.com/gobwas/glob)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(github.com/OpenPeeDeeP/depguard/v2) = %{version}
Provides:       go(github.com/OpenPeeDeeP/depguard/v2/internal/utils) = %{version}

Requires:       go(github.com/BurntSushi/toml)
Requires:       go(github.com/gobwas/glob)
Requires:       go(golang.org/x/tools)
Requires:       go(gopkg.in/yaml.v3)

%description
A Go linter that checks package imports are in a list of acceptable packages.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n depguard-%{version}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/github.com/OpenPeeDeeP/depguard/v2

%changelog
%autochangelog
