# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           mirror
%define go_import_path  github.com/butuzov/mirror

Name:           go-github-butuzov-mirror
Version:        1.3.3
Release:        %autorelease
Summary:        Go analyzer for more efficient bytes and strings operations
License:        MIT
URL:            https://github.com/butuzov/mirror
#!RemoteAsset:  sha256:16c5b911d64eb8a43a2f55c5bc7a6c5acde6f65fd3235d83a282bd8c0b0f0a65
Source0:        https://github.com/butuzov/mirror/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.25.0
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/tools/go/analysis)
BuildRequires:  go(golang.org/x/tools/go/analysis/analysistest)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/inspect)
BuildRequires:  go(golang.org/x/tools/go/analysis/singlechecker)
BuildRequires:  go(golang.org/x/tools/go/ast/inspector)
BuildRequires:  go(golang.org/x/tools/txtar)

# Export the source module roots and every installed Go package.
Provides:       go(github.com/butuzov/mirror) = %{version}
Provides:       go(github.com/butuzov/mirror/cmd/internal/mirror-table) = %{version}
Provides:       go(github.com/butuzov/mirror/cmd/internal/tests) = %{version}
Provides:       go(github.com/butuzov/mirror/cmd/mirror) = %{version}
Provides:       go(github.com/butuzov/mirror/internal/checker) = %{version}

Requires:       go(golang.org/x/tools/go/analysis)
Requires:       go(golang.org/x/tools/go/analysis/passes/inspect)
Requires:       go(golang.org/x/tools/go/analysis/singlechecker)
Requires:       go(golang.org/x/tools/go/ast/inspector)

%description
Go analyzer for more efficient bytes and strings operations. This package
contains the complete upstream repository sources and tests.

%files
%doc readme.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
