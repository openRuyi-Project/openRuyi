# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           tagliatelle
%define go_import_path  github.com/ldez/tagliatelle

Name:           go-github-ldez-tagliatelle
Version:        0.8.0
Release:        %autorelease
Summary:        Go analyzer for struct tag naming conventions
License:        Apache-2.0
URL:            https://github.com/ldez/tagliatelle
#!RemoteAsset:  sha256:5aa750a6e700ba52f94ce1e479bd3e856be60ace121ab1651d27546694443cd0
Source0:        https://github.com/ldez/tagliatelle/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# These dependency-free fixture modules do not need go mod vendor.
Patch2000:      2000-offline-module-fixtures.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/ettle/strcase)
BuildRequires:  go(github.com/hashicorp/go-immutable-radix/v2)
BuildRequires:  go(github.com/hashicorp/golang-lru/v2)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/ldez/tagliatelle) = %{version}

Requires:       go(github.com/ettle/strcase)
Requires:       go(github.com/hashicorp/go-immutable-radix/v2)
Requires:       go(golang.org/x/tools)

%description
Go analyzer for struct tag naming conventions.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n tagliatelle-%{version}

%files
%doc readme.md
%license LICENSE
%{go_sys_gopath}/github.com/ldez/tagliatelle

%changelog
%autochangelog
