# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           rowserrcheck
%define go_import_path  github.com/golangci/rowserrcheck

Name:           go-github-golangci-rowserrcheck
Version:        0+git20261022.e0740d5
Release:        %autorelease
Summary:        Go analyzer for database row error checks
License:        MIT
URL:            https://github.com/golangci/rowserrcheck
#!RemoteAsset:  sha256:cbfa0b512698f1a6cc71b92fde2728d0a8ef563b7c40b76e3c46a88e85aefee3
Source0:        https://codeload.github.com/golangci/rowserrcheck/tar.gz/e0740d52dee8bb753c0dd9ea4d10cb62621f4acc#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.26.0
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/tools/go/analysis)
BuildRequires:  go(golang.org/x/tools/go/analysis/analysistest)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/buildssa)
BuildRequires:  go(golang.org/x/tools/go/analysis/singlechecker)
BuildRequires:  go(golang.org/x/tools/go/ssa)

# Export the source module roots and every installed Go package.
Provides:       go(github.com/golangci/rowserrcheck) = %{version}
Provides:       go(github.com/golangci/rowserrcheck/passes/rowserr) = %{version}

Requires:       go(golang.org/x/tools/go/analysis)
Requires:       go(golang.org/x/tools/go/analysis/passes/buildssa)
Requires:       go(golang.org/x/tools/go/analysis/singlechecker)
Requires:       go(golang.org/x/tools/go/ssa)

%description
Go analyzer for database row error checks. This package contains the complete
upstream repository sources and tests.

%prep
%autosetup -n rowserrcheck-e0740d52dee8bb753c0dd9ea4d10cb62621f4acc

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
