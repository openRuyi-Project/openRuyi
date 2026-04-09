# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           tools
%define go_import_path  golang.org/x/tools
# So tired, can't stand more flaky tests - 251
%define go_test_exclude_glob %{shrink:
    golang.org/x/tools/cmd/signature-fuzzer/*
    golang.org/x/tools/cmd/stringer
    golang.org/x/tools/copyright
    golang.org/x/tools/go/analysis/checker
    golang.org/x/tools/go/analysis/internal/checker
    golang.org/x/tools/go/analysis/passes/inline
    golang.org/x/tools/go/analysis/passes/modernize
    golang.org/x/tools/go/analysis/unitchecker
    golang.org/x/tools/go/callgraph*
    golang.org/x/tools/go/loader
    golang.org/x/tools/go/packages
    golang.org/x/tools/go/ssa
    golang.org/x/tools/go/types/objectpath
    golang.org/x/tools/gopls*
    golang.org/x/tools/internal/gocommand
    golang.org/x/tools/internal/gcimporter
    golang.org/x/tools/internal/mcp
    golang.org/x/tools/internal/mcp/internal/oauthex
    golang.org/x/tools/internal/refactor/inline
    golang.org/x/tools/internal/typesinternal/typeindex
    golang.org/x/tools/refactor/eg
}

Name:           go-golang-x-tools
Version:        0.40.0
Release:        %autorelease
Summary:        Various packages and tools that support the Go programming language
License:        BSD-3-Clause
URL:            https://golang.org/x/tools
VCS:            git:https://github.com/golang/tools
#!RemoteAsset
Source0:        https://github.com/golang/tools/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
#!RemoteAsset
Source1:        https://github.com/golang/telemetry/archive/config/v0.80.0.tar.gz#/telemetry-config-v0.80.0.tar.gz
BuildSystem:    golangmodules

# Skip flaky test - 251
Patch0:         2000-skip-test.patch
# Patches from debian, thanks!
Patch1:         2001-Set-GO111MODULE-on.patch

BuildOption(prep):  -n %{_name}-%{version}
BuildOption(check):  -short -timeout=30m

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/yuin/goldmark)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sync)

Provides:       go(golang.org/x/tools) = %{version}

Requires:       go(github.com/yuin/goldmark)
Requires:       go(golang.org/x/mod)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/sync)

%description
This package provides the golang.org/x/tools module, comprising
various tools and packages mostly for static analysis of Go programs.

%package     -n go-tools
Summary:        Executable of tools

%description -n go-tools
This package contains the golang.org/x/tools module executables, comprising
various tools and packages mostly for static analysis of Go programs.

%prep -a
%go_prep
# Provide only the x/telemetry subtree
# See https://go.dev/issue/58894
pushd %{_builddir}/go/src/%{go_import_path}
mkdir -p vendor/golang.org/x/telemetry
tar -xf %{SOURCE1} \
    --strip-components=1 \
    -C vendor/golang.org/x/telemetry \
    telemetry-config-v0.80.0
cat > vendor/modules.txt <<'EOF'
# golang.org/x/telemetry v0.80.0
## explicit
golang.org/x/telemetry
EOF
popd

# Build binaries for tools
%build
%go_common
cd %{_builddir}/go/src/%{go_import_path}
go install -trimpath -v -p %{?_smp_build_ncpus} ./cmd/...

# Install binaries for tools
%install -a
install -d %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/go/bin/* %{buildroot}%{_bindir}/

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%files -n go-tools
%license LICENSE*
%{_bindir}/*

%changelog
%autochangelog
