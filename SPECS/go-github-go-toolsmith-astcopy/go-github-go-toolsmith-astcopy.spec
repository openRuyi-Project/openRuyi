# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           astcopy
%define go_import_path  github.com/go-toolsmith/astcopy

Name:           go-github-go-toolsmith-astcopy
Version:        1.1.0
Release:        %autorelease
Summary:        Deep copy operations for Go syntax trees
License:        MIT
URL:            https://github.com/go-toolsmith/astcopy
#!RemoteAsset:  sha256:44489b1449a949c29fac89ff9e0ce8ac5f8424fc2e190e3bcb131fef075c72c3
Source0:        https://github.com/go-toolsmith/astcopy/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.16
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-toolsmith/astequal)
BuildRequires:  go(github.com/go-toolsmith/strparse)
BuildRequires:  go(golang.org/x/exp/typeparams)

# Export the source module roots and every installed Go package.
Provides:       go(github.com/go-toolsmith/astcopy) = %{version}

Requires:       go(golang.org/x/exp/typeparams)

%description
Deep copy operations for Go syntax trees. This package contains the complete
upstream repository sources and tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
