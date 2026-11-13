# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           errcheck
%define go_import_path  github.com/kisielk/errcheck

Name:           go-github-kisielk-errcheck
Version:        1.30.0
Release:        %autorelease
Summary:        Errcheck finds silently ignored errors in Go code
License:        MIT
URL:            https://github.com/kisielk/errcheck
#!RemoteAsset:  sha256:0c7b3bfdc9cc659d87c6ed72eb8980e4740e2990a6243a6e67743394ea1c20ff
Source0:        https://github.com/kisielk/errcheck/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Downstream: temporary fixture modules need module mode in GOPATH builds.
Patch2000:      2000-enable-module-mode-for-temporary-fixtures.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/kisielk/errcheck) = %{version}
Provides:       go(github.com/kisielk/errcheck/errcheck) = %{version}

Requires:       go(golang.org/x/tools)

%description
Errcheck finds silently ignored errors in Go code.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n errcheck-%{version}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/github.com/kisielk/errcheck

%changelog
%autochangelog
