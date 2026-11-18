# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           iota-mixing
%define go_import_path  github.com/AdminBenni/iota-mixing

Name:           go-github-adminbenni-iota-mixing
Version:        1.0.0
Release:        %autorelease
Summary:        Go analyzer for mixed iota constant declarations
License:        MIT
URL:            https://github.com/AdminBenni/iota-mixing
#!RemoteAsset:  sha256:f2869f9b4b1b70c2b34649e8bfd89824d0c2395a5946f3b9249cd03349751235
Source0:        https://github.com/AdminBenni/iota-mixing/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.23.3
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
Provides:       go(github.com/AdminBenni/iota-mixing) = %{version}
Provides:       go(github.com/AdminBenni/iota-mixing/cmd/iota-mixing) = %{version}
Provides:       go(github.com/AdminBenni/iota-mixing/pkg/analyzer) = %{version}
Provides:       go(github.com/AdminBenni/iota-mixing/pkg/analyzer/flags) = %{version}

Requires:       go(golang.org/x/tools/go/analysis)
Requires:       go(golang.org/x/tools/go/analysis/passes/inspect)
Requires:       go(golang.org/x/tools/go/analysis/singlechecker)
Requires:       go(golang.org/x/tools/go/ast/inspector)

%description
Go analyzer for mixed iota constant declarations. This package contains the
complete upstream repository sources and tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
