# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           unconvert
%define go_import_path  github.com/golangci/unconvert

Name:           go-github-golangci-unconvert
Version:        0+git20261022.a129a6e
Release:        %autorelease
Summary:        Go analyzer for unnecessary type conversions
License:        BSD-3-Clause
URL:            https://github.com/golangci/unconvert
#!RemoteAsset:  sha256:7767b9d2821a15335f656d113cba6c01d96e7211d3e7f9fa1e304514b7b3a564
Source0:        https://codeload.github.com/golangci/unconvert/tar.gz/a129a6e6413e8ed232ecab9a9f7083ccd3487c8f#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Build the CLI test helper from the library implementation after the fork.
Patch2000:      2000-tests-build-executable-from-library-sources.patch

BuildRequires:  go >= 1.23.0
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/text/width)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/tools/go/analysis)
BuildRequires:  go(golang.org/x/tools/go/packages)

# Export the source module roots and every installed Go package.
Provides:       go(github.com/golangci/unconvert) = %{version}

Requires:       go(golang.org/x/text/width)
Requires:       go(golang.org/x/tools/go/analysis)
Requires:       go(golang.org/x/tools/go/packages)

%description
Go analyzer for unnecessary type conversions. This package contains the
complete upstream repository sources and tests.

%prep
%autosetup -n unconvert-a129a6e6413e8ed232ecab9a9f7083ccd3487c8f

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
