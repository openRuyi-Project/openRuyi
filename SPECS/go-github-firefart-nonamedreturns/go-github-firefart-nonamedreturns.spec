# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           nonamedreturns
%define go_import_path  github.com/firefart/nonamedreturns

Name:           go-github-firefart-nonamedreturns
Version:        1.0.8
Release:        %autorelease
Summary:        Go analyzer for named return values
License:        GPL-3.0-only
URL:            https://github.com/firefart/nonamedreturns
#!RemoteAsset:  sha256:1c32124a01105e766f0bfe86c60307f9a2982afe6beb89adf5db620f71401f87
Source0:        https://github.com/firefart/nonamedreturns/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.25.0
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/tools/go/analysis)
BuildRequires:  go(golang.org/x/tools/go/analysis/analysistest)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/inspect)
BuildRequires:  go(golang.org/x/tools/go/analysis/singlechecker)
BuildRequires:  go(golang.org/x/tools/go/ast/inspector)

# Export the source module roots and every installed Go package.
Provides:       go(github.com/firefart/nonamedreturns) = %{version}
Provides:       go(github.com/firefart/nonamedreturns/analyzer) = %{version}

Requires:       go(golang.org/x/tools/go/analysis)
Requires:       go(golang.org/x/tools/go/analysis/passes/inspect)
Requires:       go(golang.org/x/tools/go/analysis/singlechecker)
Requires:       go(golang.org/x/tools/go/ast/inspector)

%description
Go analyzer for named return values. This package contains the complete
upstream repository sources and tests.

%files
%doc Readme.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
