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
Version:        0.50.0
Release:        %autorelease
Summary:        Various packages and tools that support the Go programming language
License:        BSD-3-Clause
URL:            https://golang.org/x/tools
VCS:            git:https://github.com/golang/tools
#!RemoteAsset:  sha256:22d397e6b0a3040aae4fbc6fccb7738b31575a86b754b8604892353f195368a2
Source0:        https://github.com/golang/tools/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
#!RemoteAsset:  sha256:7c7d1718dd80c6fed01597c3a4789ce373386c865531b62da656e2eff2f9ab29
Source1:        https://github.com/golang/telemetry/archive/config/v0.119.0.tar.gz#/telemetry-config-v0.119.0.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Skip flaky test - 251
Patch2000:      2000-skip-test.patch
# Patches from debian, thanks!
Patch2001:      2001-Set-GO111MODULE-on.patch

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
Provides:       go(golang.org/x/tools/cover) = %{version}
Provides:       go(golang.org/x/tools/go/analysis) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/analysistest) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/multichecker) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/appends) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/asmdecl) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/assign) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/atomic) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/atomicalign) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/bools) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/buildssa) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/buildtag) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/cgocall) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/composite) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/copylock) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/ctrlflow) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/deepequalerrors) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/defers) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/directive) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/errorsas) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/fieldalignment) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/findcall) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/framepointer) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/hostport) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/httpmux) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/httpresponse) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/ifaceassert) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/inline) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/inspect) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/loopclosure) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/lostcancel) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/modernize) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/nilfunc) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/nilness) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/pkgfact) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/printf) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/reflectvaluecompare) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/shadow) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/shift) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/sigchanyzer) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/slog) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/sortslice) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/stdmethods) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/stdversion) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/stringintconv) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/structtag) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/testinggoroutine) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/tests) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/timeformat) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/unmarshal) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/unreachable) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/unsafeptr) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/unusedresult) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/unusedwrite) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/passes/waitgroup) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/singlechecker) = %{version}
Provides:       go(golang.org/x/tools/go/analysis/unitchecker) = %{version}
Provides:       go(golang.org/x/tools/go/ast/astutil) = %{version}
Provides:       go(golang.org/x/tools/go/ast/inspector) = %{version}
Provides:       go(golang.org/x/tools/go/gcexportdata) = %{version}
Provides:       go(golang.org/x/tools/go/packages) = %{version}
Provides:       go(golang.org/x/tools/go/ssa) = %{version}
Provides:       go(golang.org/x/tools/go/types/objectpath) = %{version}
Provides:       go(golang.org/x/tools/go/types/typeutil) = %{version}
Provides:       go(golang.org/x/tools/imports) = %{version}
Provides:       go(golang.org/x/tools/txtar) = %{version}

Requires:       go(github.com/yuin/goldmark)
Requires:       go(golang.org/x/mod)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/sync)

%description
This package provides the golang.org/x/tools module, comprising
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
    telemetry-config-v0.119.0
cat > vendor/modules.txt <<'EOF'
# golang.org/x/telemetry v0.119.0
## explicit
golang.org/x/telemetry
EOF
popd

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
