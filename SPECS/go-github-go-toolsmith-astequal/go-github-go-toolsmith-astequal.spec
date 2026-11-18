# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           astequal
%define go_import_path  github.com/go-toolsmith/astequal

Name:           go-github-go-toolsmith-astequal
Version:        1.2.0
Release:        %autorelease
Summary:        Equality comparisons for Go syntax trees
License:        MIT
URL:            https://github.com/go-toolsmith/astequal
#!RemoteAsset:  sha256:c728110b9472e912aa1006bb3213fdf1feb0a856d90d35a02587c8d8e001312c
Source0:        https://github.com/go-toolsmith/astequal/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.18
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-toolsmith/strparse)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/go-cmp/cmp)

# Export the source module roots and every installed Go package.
Provides:       go(github.com/go-toolsmith/astequal) = %{version}

Requires:       go(github.com/google/go-cmp/cmp)

%description
Equality comparisons for Go syntax trees. This package contains the complete
upstream repository sources and tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
