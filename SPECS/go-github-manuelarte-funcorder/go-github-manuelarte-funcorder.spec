# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           funcorder
%define go_import_path  github.com/manuelarte/funcorder

Name:           go-github-manuelarte-funcorder
Version:        0.6.0
Release:        %autorelease
Summary:        Go analyzer for function and method ordering
License:        Apache-2.0
URL:            https://github.com/manuelarte/funcorder
#!RemoteAsset:  sha256:c0e0101d93761d10a259e5763eeac2681eb57ae22f16c9dca410d088db9afafe
Source0:        https://github.com/manuelarte/funcorder/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/manuelarte/funcorder) = %{version}
Provides:       go(github.com/manuelarte/funcorder/analyzer) = %{version}
Provides:       go(github.com/manuelarte/funcorder/internal) = %{version}

Requires:       go(golang.org/x/tools)

%description
Go analyzer for function and method ordering.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n funcorder-%{version}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/github.com/manuelarte/funcorder

%changelog
%autochangelog
