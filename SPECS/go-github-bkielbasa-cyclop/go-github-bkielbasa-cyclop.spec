# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           cyclop
%define go_import_path  github.com/bkielbasa/cyclop

Name:           go-github-bkielbasa-cyclop
Version:        1.2.3
Release:        %autorelease
Summary:        Cyclomatic complexity analyzer for Go functions and packages
License:        MIT
URL:            https://github.com/bkielbasa/cyclop
#!RemoteAsset:  sha256:53c63def874811feec2a2d1e0afbc4216fe67c1ff210618c291afa6884d2cd6f
Source0:        https://github.com/bkielbasa/cyclop/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.22.0
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/tools/go/analysis)
BuildRequires:  go(golang.org/x/tools/go/analysis/analysistest)
BuildRequires:  go(golang.org/x/tools/go/analysis/singlechecker)

# Export the source module roots and every installed Go package.
Provides:       go(github.com/bkielbasa/cyclop) = %{version}
Provides:       go(github.com/bkielbasa/cyclop/cmd/cyclop) = %{version}
Provides:       go(github.com/bkielbasa/cyclop/pkg/analyzer) = %{version}

Requires:       go(golang.org/x/tools/go/analysis)
Requires:       go(golang.org/x/tools/go/analysis/singlechecker)

%description
Cyclomatic complexity analyzer for Go functions and packages. This package
contains the complete upstream repository sources and tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
