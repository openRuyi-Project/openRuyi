# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           pkgload
%define go_import_path  github.com/go-toolsmith/pkgload

Name:           go-github-go-toolsmith-pkgload
Version:        1.2.2
Release:        %autorelease
Summary:        Go package loading helpers for static analysis
License:        MIT
URL:            https://github.com/go-toolsmith/pkgload
#!RemoteAsset:  sha256:42d95327f7ae32af71c172ebc628cde436a562283969a6959da21310f761cc76
Source0:        https://github.com/go-toolsmith/pkgload/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Relative fixture paths have local import IDs in GOPATH mode.
Patch2000:      2000-tests-load-fixtures-by-import-path.patch

BuildRequires:  go >= 1.17
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/tools/go/packages)

# Export the source module roots and every installed Go package.
Provides:       go(github.com/go-toolsmith/pkgload) = %{version}

Requires:       go(golang.org/x/tools/go/packages)

%description
Go package loading helpers for static analysis. This package contains the
complete upstream repository sources and tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
