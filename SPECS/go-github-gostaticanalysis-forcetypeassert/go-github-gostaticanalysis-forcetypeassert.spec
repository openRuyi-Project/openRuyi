# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           forcetypeassert
%define go_import_path  github.com/gostaticanalysis/forcetypeassert

Name:           go-github-gostaticanalysis-forcetypeassert
Version:        0.2.0
Release:        %autorelease
Summary:        Go analyzer for unchecked type assertions
License:        MIT
URL:            https://github.com/gostaticanalysis/forcetypeassert
#!RemoteAsset:  sha256:01d290d11bdeebdb1cf6db2d9f5a5270d28b6abce42359412ec3adc356c95462
Source0:        https://github.com/gostaticanalysis/forcetypeassert/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.23.0
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
Provides:       go(github.com/gostaticanalysis/forcetypeassert) = %{version}
Provides:       go(github.com/gostaticanalysis/forcetypeassert/cmd/forcetypeassert) = %{version}

Requires:       go(golang.org/x/tools/go/analysis)
Requires:       go(golang.org/x/tools/go/analysis/passes/inspect)
Requires:       go(golang.org/x/tools/go/analysis/singlechecker)
Requires:       go(golang.org/x/tools/go/ast/inspector)

%description
Go analyzer for unchecked type assertions. This package contains the complete
upstream repository sources and tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
