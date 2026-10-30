# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           perfsprint
%define go_import_path  github.com/catenacyber/perfsprint

Name:           go-github-catenacyber-perfsprint
Version:        0.10.1
Release:        %autorelease
Summary:        Go analyzer for efficient formatting operations
License:        MIT
URL:            https://github.com/catenacyber/perfsprint
#!RemoteAsset:  sha256:d3fc6bcd689081fad06004ed956048720afd15790103763ee25c4c8823928f41
Source0:        https://github.com/catenacyber/perfsprint/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.24.0
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
Provides:       go(github.com/catenacyber/perfsprint) = %{version}
Provides:       go(github.com/catenacyber/perfsprint/analyzer) = %{version}

Requires:       go(golang.org/x/tools/go/analysis)
Requires:       go(golang.org/x/tools/go/analysis/passes/inspect)
Requires:       go(golang.org/x/tools/go/analysis/singlechecker)
Requires:       go(golang.org/x/tools/go/ast/inspector)

%description
Go analyzer for efficient formatting operations. This package contains the
complete upstream repository sources and tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
