# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gogrep
%define go_import_path  github.com/quasilyte/gogrep

Name:           go-github-quasilyte-gogrep
Version:        0.5.0
Release:        %autorelease
Summary:        Syntax-aware pattern matching for Go source code
License:        BSD-3-Clause
URL:            https://github.com/quasilyte/gogrep
#!RemoteAsset:  sha256:a7df0adb083b8e85eee4708634b425996ff963cd0a90de4aed37ec21f8cd62bf
Source0:        https://github.com/quasilyte/gogrep/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-toolsmith/astequal)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/pprof)
BuildRequires:  go(github.com/quasilyte/perf-heatmap)
BuildRequires:  go(golang.org/x/exp/typeparams)

Provides:       go(github.com/quasilyte/gogrep) = %{version}
Provides:       go(github.com/quasilyte/gogrep/cmd/gogrep) = %{version}
Provides:       go(github.com/quasilyte/gogrep/filters) = %{version}
Provides:       go(github.com/quasilyte/gogrep/internal/stdinfo) = %{version}
Provides:       go(github.com/quasilyte/gogrep/nodetag) = %{version}

Requires:       go(github.com/go-toolsmith/astequal)
Requires:       go(github.com/google/pprof)
Requires:       go(github.com/quasilyte/perf-heatmap)
Requires:       go(golang.org/x/exp/typeparams)

%description
Syntax-aware pattern matching for Go source code.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n gogrep-%{version}

%install -a
# Nested modules use their declared import paths; keep repository fixtures intact.
install -d %{buildroot}%{go_sys_gopath}/github.com/quasilyte/gogrep/cmd/gogrep
cp -a cmd/gogrep/. %{buildroot}%{go_sys_gopath}/github.com/quasilyte/gogrep/cmd/gogrep/

%check
# Stage all modules at their declared paths before testing every package.
%{go_common}
mkdir -p %{_builddir}/go/src/github.com/quasilyte/gogrep/cmd/gogrep
cp -a cmd/gogrep/. %{_builddir}/go/src/github.com/quasilyte/gogrep/cmd/gogrep/
mkdir -p %{_builddir}/go/src/github.com/quasilyte/gogrep
cp -a ./. %{_builddir}/go/src/github.com/quasilyte/gogrep/
# The package list omits modules that only declare tool dependencies.
(
    cd %{_builddir}/go/src/github.com/quasilyte/gogrep
    packages=$(go list -e -f '{{if or .GoFiles .CgoFiles .TestGoFiles .XTestGoFiles}}{{.ImportPath}}{{end}}' ./...)
    if [ -n "$packages" ]; then
        go test -v $packages
    fi
)

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/github.com/quasilyte/gogrep

%changelog
%autochangelog
