# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           bidichk
%define go_import_path  github.com/breml/bidichk

Name:           go-github-breml-bidichk
Version:        0.3.4
Release:        %autorelease
Summary:        Go analyzer for dangerous bidirectional Unicode characters
License:        MIT
URL:            https://github.com/breml/bidichk
#!RemoteAsset:  sha256:e9cbf7a01a82d57497219c407ac9adc90fb4ee121edf2cde38e7b521f54bfeb6
Source0:        https://github.com/breml/bidichk/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.26.0
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/tools/go/analysis)
BuildRequires:  go(golang.org/x/tools/go/analysis/analysistest)
BuildRequires:  go(golang.org/x/tools/go/analysis/singlechecker)

# Export the source module roots and every installed Go package.
Provides:       go(github.com/breml/bidichk) = %{version}
Provides:       go(github.com/breml/bidichk/cmd/bidichk) = %{version}
Provides:       go(github.com/breml/bidichk/pkg/bidichk) = %{version}

Requires:       go(golang.org/x/tools/go/analysis)
Requires:       go(golang.org/x/tools/go/analysis/singlechecker)

%description
Go analyzer for dangerous bidirectional Unicode characters. This package
contains the complete upstream repository sources and tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
