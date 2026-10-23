# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-ruleguard
%define go_import_path  github.com/quasilyte/go-ruleguard

Name:           go-github-quasilyte-go-ruleguard
Version:        0.4.5
Release:        %autorelease
Summary:        Analysis-based Go linter that runs dynamically loaded rules
License:        BSD-3-Clause
URL:            https://github.com/quasilyte/go-ruleguard
#!RemoteAsset:  sha256:31b6ffb57c912ffc43b91e09551e72f11287924d03ee2bf8c01ad71961fca484
Source0:        https://github.com/quasilyte/go-ruleguard/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/cespare/subcmd)
BuildRequires:  go(github.com/go-ruleguard/rg1)
BuildRequires:  go(github.com/go-toolsmith/astcopy)
BuildRequires:  go(github.com/go-toolsmith/astequal)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/quasilyte/gogrep)
BuildRequires:  go(github.com/quasilyte/stdinfo)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(go.uber.org/zap)
BuildRequires:  go(golang.org/x/exp/typeparams)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/quasilyte/go-ruleguard) = %{version}
Provides:       go(github.com/quasilyte/go-ruleguard/_docs) = %{version}
Provides:       go(github.com/quasilyte/go-ruleguard/analyzer) = %{version}
Provides:       go(github.com/quasilyte/go-ruleguard/analyzer/testanalyzer) = %{version}
Provides:       go(github.com/quasilyte/go-ruleguard/cmd/gorules) = %{version}
Provides:       go(github.com/quasilyte/go-ruleguard/dsl) = %{version}
Provides:       go(github.com/quasilyte/go-ruleguard/dsl/types) = %{version}
Provides:       go(github.com/quasilyte/go-ruleguard/internal/goenv) = %{version}
Provides:       go(github.com/quasilyte/go-ruleguard/internal/golist) = %{version}
Provides:       go(github.com/quasilyte/go-ruleguard/internal/xsrcimporter) = %{version}
Provides:       go(github.com/quasilyte/go-ruleguard/internal/xtypes) = %{version}
Provides:       go(github.com/quasilyte/go-ruleguard/ruleguard) = %{version}
Provides:       go(github.com/quasilyte/go-ruleguard/ruleguard/goutil) = %{version}
Provides:       go(github.com/quasilyte/go-ruleguard/ruleguard/ir) = %{version}
Provides:       go(github.com/quasilyte/go-ruleguard/ruleguard/irconv) = %{version}
Provides:       go(github.com/quasilyte/go-ruleguard/ruleguard/irprint) = %{version}
Provides:       go(github.com/quasilyte/go-ruleguard/ruleguard/profiling) = %{version}
Provides:       go(github.com/quasilyte/go-ruleguard/ruleguard/quasigo) = %{version}
Provides:       go(github.com/quasilyte/go-ruleguard/ruleguard/quasigo/internal/evaltest) = %{version}
Provides:       go(github.com/quasilyte/go-ruleguard/ruleguard/quasigo/stdlib/qfmt) = %{version}
Provides:       go(github.com/quasilyte/go-ruleguard/ruleguard/quasigo/stdlib/qstrconv) = %{version}
Provides:       go(github.com/quasilyte/go-ruleguard/ruleguard/quasigo/stdlib/qstrings) = %{version}
Provides:       go(github.com/quasilyte/go-ruleguard/ruleguard/textmatch) = %{version}
Provides:       go(github.com/quasilyte/go-ruleguard/ruleguard/typematch) = %{version}
Provides:       go(github.com/quasilyte/go-ruleguard/rules) = %{version}

Requires:       go(github.com/cespare/subcmd)
Requires:       go(github.com/go-toolsmith/astcopy)
Requires:       go(github.com/quasilyte/gogrep)
Requires:       go(github.com/quasilyte/stdinfo)
Requires:       go(golang.org/x/exp/typeparams)
Requires:       go(golang.org/x/tools)

%description
Analysis-based Go linter that runs dynamically loaded rules.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n go-ruleguard-%{version}

%install -a
# Nested modules use their declared import paths; keep repository fixtures intact.
install -d %{buildroot}%{go_sys_gopath}/github.com/quasilyte/go-ruleguard/cmd/gorules
cp -a cmd/gorules/. %{buildroot}%{go_sys_gopath}/github.com/quasilyte/go-ruleguard/cmd/gorules/
install -d %{buildroot}%{go_sys_gopath}/github.com/quasilyte/go-ruleguard/dsl
cp -a dsl/. %{buildroot}%{go_sys_gopath}/github.com/quasilyte/go-ruleguard/dsl/
install -d %{buildroot}%{go_sys_gopath}/github.com/quasilyte/go-ruleguard/rules
cp -a rules/. %{buildroot}%{go_sys_gopath}/github.com/quasilyte/go-ruleguard/rules/

%check
# Stage all modules at their declared paths before testing every package.
%{go_common}
mkdir -p %{_builddir}/go/src/github.com/quasilyte/go-ruleguard/cmd/gorules
cp -a cmd/gorules/. %{_builddir}/go/src/github.com/quasilyte/go-ruleguard/cmd/gorules/
mkdir -p %{_builddir}/go/src/github.com/quasilyte/go-ruleguard/rules
cp -a rules/. %{_builddir}/go/src/github.com/quasilyte/go-ruleguard/rules/
mkdir -p %{_builddir}/go/src/github.com/quasilyte/go-ruleguard/dsl
cp -a dsl/. %{_builddir}/go/src/github.com/quasilyte/go-ruleguard/dsl/
mkdir -p %{_builddir}/go/src/github.com/quasilyte/go-ruleguard
cp -a ./. %{_builddir}/go/src/github.com/quasilyte/go-ruleguard/
# The package list omits modules that only declare tool dependencies.
(
    cd %{_builddir}/go/src/github.com/quasilyte/go-ruleguard
    packages=$(go list -e -f '{{if or .GoFiles .CgoFiles .TestGoFiles .XTestGoFiles}}{{.ImportPath}}{{end}}' ./...)
    if [ -n "$packages" ]; then
        go test -v $packages
    fi
)

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/github.com/quasilyte/go-ruleguard

%changelog
%autochangelog
