# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           strparse
%define go_import_path  github.com/go-toolsmith/strparse

Name:           go-github-go-toolsmith-strparse
Version:        1.1.0
Release:        %autorelease
Summary:        Go syntax parser helpers for strings
License:        MIT
URL:            https://github.com/go-toolsmith/strparse
#!RemoteAsset:  sha256:822c63bb396f5a0d75a5a24136355593cc4d72afe71f019b4128577598e62680
Source0:        https://github.com/go-toolsmith/strparse/archive/v%{version}.tar.gz
# Use the complete test dependency to break its reciprocal test dependency.
#!RemoteAsset:  sha256:c728110b9472e912aa1006bb3213fdf1feb0a856d90d35a02587c8d8e001312c
Source1:        https://github.com/go-toolsmith/astequal/archive/v1.2.0.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.18
BuildRequires:  go-rpm-macros
# Source1 supplies astequal; retain its complete external dependency closure.
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/go-cmp/cmp)

# Export the source module roots and every installed Go package.
Provides:       go(github.com/go-toolsmith/strparse) = %{version}

%description
Go syntax parser helpers for strings. This package contains the complete
upstream repository sources and tests.

# Stage the full test dependency in the GOPATH used by golangmodules.
# Keep it outside the strparse source tree so it is not installed in this RPM.
%prep -a
mkdir -p %{_builddir}/go/src/github.com/go-toolsmith/astequal
tar -xf %{SOURCE1} --strip-components=1 -C %{_builddir}/go/src/github.com/go-toolsmith/astequal

# Also validate the staged dependency, including its tests that import strparse.
%check -a
%go_common
cd %{_builddir}/go/src/github.com/go-toolsmith/astequal
%{__go} test %{go_test_flags_default} ./...

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
