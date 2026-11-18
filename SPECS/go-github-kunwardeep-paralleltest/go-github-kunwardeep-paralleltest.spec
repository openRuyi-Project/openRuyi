# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           paralleltest
%define go_import_path  github.com/kunwardeep/paralleltest

Name:           go-github-kunwardeep-paralleltest
Version:        1.0.16
Release:        %autorelease
Summary:        Go analyzer for parallel test execution
License:        MIT
URL:            https://github.com/kunwardeep/paralleltest
#!RemoteAsset:  sha256:5c68f497bd270e4b6253caba711a48850b02324cf9e7feb31705cdb85477c6e7
Source0:        https://github.com/kunwardeep/paralleltest/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/kunwardeep/paralleltest) = %{version}
Provides:       go(github.com/kunwardeep/paralleltest/pkg/paralleltest) = %{version}

Requires:       go(golang.org/x/tools)

%description
Go analyzer for parallel test execution.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n paralleltest-%{version}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/github.com/kunwardeep/paralleltest

%changelog
%autochangelog
