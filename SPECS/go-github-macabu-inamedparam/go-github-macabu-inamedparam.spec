# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           inamedparam
%define go_import_path  github.com/macabu/inamedparam

Name:           go-github-macabu-inamedparam
Version:        0.2.0
Release:        %autorelease
Summary:        A linter that reports interfaces with unnamed method parameters
License:        MIT
URL:            https://github.com/macabu/inamedparam
#!RemoteAsset:  sha256:843c291d3f14a3244cedf0950ef6055108c3f55ea68b5db79651c243773e8e7a
Source0:        https://github.com/macabu/inamedparam/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/macabu/inamedparam) = %{version}

Requires:       go(golang.org/x/tools)

%description
A linter that reports interfaces with unnamed method parameters.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n inamedparam-%{version}

%files
%doc README.md
%license LICENSE-MIT
%{go_sys_gopath}/github.com/macabu/inamedparam

%changelog
%autochangelog
