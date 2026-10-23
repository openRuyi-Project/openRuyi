# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           tparallel
%define go_import_path  github.com/moricho/tparallel

Name:           go-github-moricho-tparallel
Version:        0.3.2
Release:        %autorelease
Summary:        Tparallel finds inappropriate usage of t.Parallel() method in your Go test codes
License:        MIT
URL:            https://github.com/moricho/tparallel
#!RemoteAsset:  sha256:05c2ed831c8ce6694c4556cceaff80f100a40d180360b9c1354d69a1959a039b
Source0:        https://github.com/moricho/tparallel/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/gostaticanalysis/analysisutil)
BuildRequires:  go(github.com/gostaticanalysis/comment)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/moricho/tparallel) = %{version}
Provides:       go(github.com/moricho/tparallel/pkg/ssafunc) = %{version}
Provides:       go(github.com/moricho/tparallel/pkg/ssainstr) = %{version}

Requires:       go(github.com/gostaticanalysis/analysisutil)
Requires:       go(golang.org/x/tools)

%description
Tparallel finds inappropriate usage of t.Parallel() method in your Go test codes.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n tparallel-%{version}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/github.com/moricho/tparallel

%changelog
%autochangelog
