# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-critic
%define go_import_path  github.com/go-critic/go-critic

Name:           go-github-go-critic-go-critic
Version:        0.15.0
Release:        %autorelease
Summary:        Extensible static analysis library and tool for Go
License:        MIT
URL:            https://github.com/go-critic/go-critic
#!RemoteAsset:  sha256:6cee82b801a849aef3adb714b7900d6df7b27213af984368be4c65db8400632e
Source0:        https://github.com/go-critic/go-critic/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.25.0
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/cristalhq/acmd)
BuildRequires:  go(github.com/go-toolsmith/astcast)
BuildRequires:  go(github.com/go-toolsmith/astcopy)
BuildRequires:  go(github.com/go-toolsmith/astequal)
BuildRequires:  go(github.com/go-toolsmith/astfmt)
BuildRequires:  go(github.com/go-toolsmith/astp)
BuildRequires:  go(github.com/go-toolsmith/pkgload)
BuildRequires:  go(github.com/go-toolsmith/strparse)
BuildRequires:  go(github.com/go-toolsmith/typep)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/go-cmp/cmp)
BuildRequires:  go(github.com/mattn/goveralls)
BuildRequires:  go(github.com/quasilyte/go-consistent)
BuildRequires:  go(github.com/quasilyte/go-ruleguard)
BuildRequires:  go(github.com/quasilyte/go-ruleguard/analyzer)
BuildRequires:  go(github.com/quasilyte/go-ruleguard/dsl)
BuildRequires:  go(github.com/quasilyte/go-ruleguard/ruleguard)
BuildRequires:  go(github.com/quasilyte/go-ruleguard/ruleguard/ir)
BuildRequires:  go(github.com/quasilyte/go-ruleguard/ruleguard/irconv)
BuildRequires:  go(github.com/quasilyte/go-ruleguard/ruleguard/irprint)
BuildRequires:  go(github.com/quasilyte/gogrep)
BuildRequires:  go(github.com/quasilyte/regex/syntax)
BuildRequires:  go(github.com/quasilyte/stdinfo)
BuildRequires:  go(golang.org/x/exp/typeparams)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/tools/go/analysis)
BuildRequires:  go(golang.org/x/tools/go/analysis/analysistest)
BuildRequires:  go(golang.org/x/tools/go/analysis/singlechecker)
BuildRequires:  go(golang.org/x/tools/go/ast/astutil)
BuildRequires:  go(golang.org/x/tools/go/packages)

# Export the source module roots and every installed Go package.
Provides:       go(github.com/go-critic/go-critic) = %{version}
Provides:       go(github.com/go-critic/go-critic/checkers) = %{version}
Provides:       go(github.com/go-critic/go-critic/checkers/analyzer) = %{version}
Provides:       go(github.com/go-critic/go-critic/checkers/internal/astwalk) = %{version}
Provides:       go(github.com/go-critic/go-critic/checkers/internal/linttest) = %{version}
Provides:       go(github.com/go-critic/go-critic/checkers/internal/lintutil) = %{version}
Provides:       go(github.com/go-critic/go-critic/checkers/rules) = %{version}
Provides:       go(github.com/go-critic/go-critic/checkers/rulesdata) = %{version}
Provides:       go(github.com/go-critic/go-critic/cmd/go-critic) = %{version}
Provides:       go(github.com/go-critic/go-critic/cmd/go-critic-analysis) = %{version}
Provides:       go(github.com/go-critic/go-critic/cmd/gocritic) = %{version}
Provides:       go(github.com/go-critic/go-critic/cmd/gocritic-analysis) = %{version}
Provides:       go(github.com/go-critic/go-critic/cmd/makedocs) = %{version}
Provides:       go(github.com/go-critic/go-critic/linter) = %{version}
Provides:       go(github.com/go-critic/go-critic/tools) = %{version}

Requires:       go(github.com/cristalhq/acmd)
Requires:       go(github.com/go-toolsmith/astcast)
Requires:       go(github.com/go-toolsmith/astcopy)
Requires:       go(github.com/go-toolsmith/astequal)
Requires:       go(github.com/go-toolsmith/astfmt)
Requires:       go(github.com/go-toolsmith/astp)
Requires:       go(github.com/go-toolsmith/pkgload)
Requires:       go(github.com/go-toolsmith/strparse)
Requires:       go(github.com/go-toolsmith/typep)
Requires:       go(github.com/google/go-cmp/cmp)
Requires:       go(github.com/mattn/goveralls)
Requires:       go(github.com/quasilyte/go-consistent)
Requires:       go(github.com/quasilyte/go-ruleguard/dsl)
Requires:       go(github.com/quasilyte/go-ruleguard/ruleguard)
Requires:       go(github.com/quasilyte/go-ruleguard/ruleguard/ir)
Requires:       go(github.com/quasilyte/go-ruleguard/ruleguard/irconv)
Requires:       go(github.com/quasilyte/go-ruleguard/ruleguard/irprint)
Requires:       go(github.com/quasilyte/regex/syntax)
Requires:       go(golang.org/x/tools/go/analysis)
Requires:       go(golang.org/x/tools/go/analysis/singlechecker)
Requires:       go(golang.org/x/tools/go/ast/astutil)
Requires:       go(golang.org/x/tools/go/packages)

%description
Extensible static analysis library and tool for Go. This package contains the
complete upstream repository sources and tests.

# tools/go.mod has no active Go packages; retain its sources and dependencies.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
