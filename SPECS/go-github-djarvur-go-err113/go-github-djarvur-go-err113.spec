# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-err113
%define go_import_path  github.com/Djarvur/go-err113

Name:           go-github-djarvur-go-err113
Version:        0.1.1
Release:        %autorelease
Summary:        Go analyzer for error creation and comparison
License:        MIT
URL:            https://github.com/Djarvur/go-err113
#!RemoteAsset:  sha256:344d29ea7fe9d3ff085fa31d10cb992579e541561f20933bd6df4a30db3ddefe
Source0:        https://github.com/Djarvur/go-err113/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.23.0
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/tools/go/analysis)
BuildRequires:  go(golang.org/x/tools/go/analysis/analysistest)
BuildRequires:  go(golang.org/x/tools/go/analysis/singlechecker)
BuildRequires:  go(golang.org/x/tools/go/ast/inspector)

# Export the source module roots and every installed Go package.
Provides:       go(github.com/Djarvur/go-err113) = %{version}
Provides:       go(github.com/Djarvur/go-err113/cmd/err113) = %{version}

Requires:       go(golang.org/x/tools/go/analysis)
Requires:       go(golang.org/x/tools/go/analysis/singlechecker)
Requires:       go(golang.org/x/tools/go/ast/inspector)

%description
Go analyzer for error creation and comparison. This package contains the
complete upstream repository sources and tests.

%files
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
