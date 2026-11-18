# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           intrange
%define go_import_path  github.com/ckaznocha/intrange

Name:           go-github-ckaznocha-intrange
Version:        0.3.1
Release:        %autorelease
Summary:        Go analyzer for loops that can range over integers
License:        MIT
URL:            https://github.com/ckaznocha/intrange
#!RemoteAsset:  sha256:a7d38a841407efe6c6f0b664526b9528dfc83bfd6ac5bc7fb4d5968761b7c49f
Source0:        https://github.com/ckaznocha/intrange/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# https://github.com/ckaznocha/intrange/pull/57
Patch1000:      1000-update-testutil-testdata-layout.patch

BuildRequires:  go >= 1.24.1
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/gostaticanalysis/testutil)
BuildRequires:  go(github.com/hashicorp/go-version)
BuildRequires:  go(github.com/josharian/mapfs)
BuildRequires:  go(github.com/josharian/txtarfs)
BuildRequires:  go(github.com/newmo-oss/gotestingmock)
BuildRequires:  go(github.com/otiai10/copy)
BuildRequires:  go(github.com/otiai10/mint)
BuildRequires:  go(github.com/tenntenn/modver)
BuildRequires:  go(github.com/tenntenn/text/transform)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/tools/go/analysis)
BuildRequires:  go(golang.org/x/tools/go/analysis/analysistest)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/inspect)
BuildRequires:  go(golang.org/x/tools/go/analysis/unitchecker)
BuildRequires:  go(golang.org/x/tools/go/ast/inspector)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(google.golang.org/protobuf/reflect/protoreflect)

# Export the source module roots and every installed Go package.
Provides:       go(github.com/ckaznocha/intrange) = %{version}
Provides:       go(github.com/ckaznocha/intrange/cmd/intrange) = %{version}

Requires:       go(golang.org/x/tools/go/analysis)
Requires:       go(golang.org/x/tools/go/analysis/passes/inspect)
Requires:       go(golang.org/x/tools/go/analysis/unitchecker)
Requires:       go(golang.org/x/tools/go/ast/inspector)

%description
Go analyzer for loops that can range over integers. This package contains the
complete upstream repository sources and tests.

# Resolve the module fixture from the installed protobuf source because OBS
# tests do not have access to the Go module proxy.
%check -p
export GOPROXY=off
export GOSUMDB=off
export GOTOOLCHAIN=local
go mod edit \
    -replace=google.golang.org/protobuf=%{go_sys_gopath}/google.golang.org/protobuf \
    testdata/src/main/go.mod

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
