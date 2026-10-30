# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           asasalint
%define go_import_path  github.com/alingse/asasalint

Name:           go-github-alingse-asasalint
Version:        0.0.11
Release:        %autorelease
Summary:        Go analyzer for variadic calls with slices of any
License:        MIT
URL:            https://github.com/alingse/asasalint
#!RemoteAsset:  sha256:cf706c488ea314102d197f42c2efeadf8838a0ecd8ff45e4d06d2e45f5f85d67
Source0:        https://github.com/alingse/asasalint/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Go 1.23 materializes the predeclared any alias in go/types.
Patch2000:      2000-support-go-types-aliases.patch
# Also resolve the predeclared any alias in the slice element type.
Patch2001:      2001-resolve-slice-element-aliases.patch

BuildRequires:  go >= 1.18
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/tools/go/analysis)
BuildRequires:  go(golang.org/x/tools/go/analysis/analysistest)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/inspect)
BuildRequires:  go(golang.org/x/tools/go/analysis/singlechecker)
BuildRequires:  go(golang.org/x/tools/go/ast/inspector)

# Export the source module roots and every installed Go package.
Provides:       go(github.com/alingse/asasalint) = %{version}
Provides:       go(github.com/alingse/asasalint/cmd/asasalint) = %{version}

Requires:       go(golang.org/x/tools/go/analysis)
Requires:       go(golang.org/x/tools/go/analysis/passes/inspect)
Requires:       go(golang.org/x/tools/go/analysis/singlechecker)
Requires:       go(golang.org/x/tools/go/ast/inspector)

%description
Go analyzer for variadic calls with slices of any. This package contains the
complete upstream repository sources and tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
