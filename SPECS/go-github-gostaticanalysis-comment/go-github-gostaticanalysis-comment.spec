# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           comment
%define go_import_path  github.com/gostaticanalysis/comment

Name:           go-github-gostaticanalysis-comment
Version:        1.5.0
Release:        %autorelease
Summary:        Go syntax tree comment mapping utilities
License:        MIT
URL:            https://github.com/gostaticanalysis/comment
#!RemoteAsset:  sha256:26924fb46a4f168e88ffda811e27e04117f2c3aefed8fa9fd04a3dd6345cdb49
Source0:        https://github.com/gostaticanalysis/comment/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Go 1.26 vet rejects a dynamic format string in this test.
Patch2000:      2000-use-constant-format-string.patch
# Current x/tools requires test analyzers to have both a name and documentation.
Patch2001:      2001-name-test-analyzer.patch

BuildRequires:  go >= 1.22.9
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/go-cmp/cmp)
BuildRequires:  go(github.com/gostaticanalysis/testutil)
BuildRequires:  go(github.com/hashicorp/go-version)
BuildRequires:  go(github.com/otiai10/copy)
BuildRequires:  go(github.com/tenntenn/modver)
BuildRequires:  go(github.com/tenntenn/text/transform)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/tools/go/analysis)
BuildRequires:  go(golang.org/x/tools/go/analysis/analysistest)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/inspect)
BuildRequires:  go(golang.org/x/tools/go/ast/inspector)
BuildRequires:  go(golang.org/x/tools/txtar)
BuildRequires:  go(golang.org/x/xerrors)

# Export the source module roots and every installed Go package.
Provides:       go(github.com/gostaticanalysis/comment) = %{version}
Provides:       go(github.com/gostaticanalysis/comment/passes/commentmap) = %{version}

Requires:       go(golang.org/x/tools/go/analysis)

%description
Go syntax tree comment mapping utilities. This package contains the complete
upstream repository sources and tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
