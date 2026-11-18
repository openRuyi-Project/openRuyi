# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           nilerr
%define go_import_path  github.com/gostaticanalysis/nilerr

Name:           go-github-gostaticanalysis-nilerr
Version:        0.1.2
Release:        %autorelease
Summary:        Go analyzer for nil returns after non-nil error checks
License:        MIT
URL:            https://github.com/gostaticanalysis/nilerr
#!RemoteAsset:  sha256:4349cec6657b713032f6b23e80751f63d6257e7354064cf8565ddae75a0adbc9
Source0:        https://github.com/gostaticanalysis/nilerr/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.23.0
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/gostaticanalysis/comment)
BuildRequires:  go(github.com/gostaticanalysis/comment/passes/commentmap)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/tools/go/analysis)
BuildRequires:  go(golang.org/x/tools/go/analysis/analysistest)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/buildssa)
BuildRequires:  go(golang.org/x/tools/go/analysis/singlechecker)
BuildRequires:  go(golang.org/x/tools/go/ssa)

# Export the source module roots and every installed Go package.
Provides:       go(github.com/gostaticanalysis/nilerr) = %{version}
Provides:       go(github.com/gostaticanalysis/nilerr/cmd/nilerr) = %{version}

Requires:       go(github.com/gostaticanalysis/comment)
Requires:       go(github.com/gostaticanalysis/comment/passes/commentmap)
Requires:       go(golang.org/x/tools/go/analysis)
Requires:       go(golang.org/x/tools/go/analysis/passes/buildssa)
Requires:       go(golang.org/x/tools/go/analysis/singlechecker)
Requires:       go(golang.org/x/tools/go/ssa)

%description
Go analyzer for nil returns after non-nil error checks. This package contains
the complete upstream repository sources and tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
