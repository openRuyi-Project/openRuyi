# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           nilnesserr
%define go_import_path  github.com/alingse/nilnesserr

Name:           go-github-alingse-nilnesserr
Version:        0.2.0
Release:        %autorelease
Summary:        Go analyzer for inconsistent nil error returns
License:        MIT
URL:            https://github.com/alingse/nilnesserr
#!RemoteAsset:  sha256:06529af0a9bc6bbf859c11026add9f6570f38791a6e75abf1a22beadd3e74fbd
Source0:        https://github.com/alingse/nilnesserr/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.22.0
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/tools/go/analysis)
BuildRequires:  go(golang.org/x/tools/go/analysis/analysistest)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/buildssa)
BuildRequires:  go(golang.org/x/tools/go/analysis/singlechecker)
BuildRequires:  go(golang.org/x/tools/go/ssa)

# Export the source module roots and every installed Go package.
Provides:       go(github.com/alingse/nilnesserr) = %{version}
Provides:       go(github.com/alingse/nilnesserr/cmd/nilnesserr) = %{version}
Provides:       go(github.com/alingse/nilnesserr/internal/typeparams) = %{version}

Requires:       go(golang.org/x/tools/go/analysis)
Requires:       go(golang.org/x/tools/go/analysis/passes/buildssa)
Requires:       go(golang.org/x/tools/go/analysis/singlechecker)
Requires:       go(golang.org/x/tools/go/ssa)

%description
Go analyzer for inconsistent nil error returns. This package contains the
complete upstream repository sources and tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
