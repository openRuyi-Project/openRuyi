# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           testutil
%define go_import_path  github.com/gostaticanalysis/testutil

Name:           go-github-gostaticanalysis-testutil
Version:        0.6.1
Release:        %autorelease
Summary:        Test utilities for Go static analysis packages
License:        MIT
URL:            https://github.com/gostaticanalysis/testutil
#!RemoteAsset:  sha256:23d4db8b6e047d92517c2b2cce5bf20ded7c02096bc81ee944c40297024f9d24
Source0:        https://github.com/gostaticanalysis/testutil/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Module operations must remain enabled when the caller uses GOPATH mode.
Patch2000:      2000-enable-module-mode-for-go-subprocesses.patch

BuildRequires:  go >= 1.24.1
BuildRequires:  go-rpm-macros
# issue00023 keeps a large module graph as test input and removes it before
# invoking Go; build requirements cover the packaged module and compiled tests.
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/go-cmp/cmp)
BuildRequires:  go(github.com/hashicorp/go-version)
BuildRequires:  go(github.com/josharian/mapfs)
BuildRequires:  go(github.com/josharian/txtarfs)
BuildRequires:  go(github.com/newmo-oss/gotestingmock)
BuildRequires:  go(github.com/otiai10/copy)
BuildRequires:  go(github.com/otiai10/mint)
BuildRequires:  go(github.com/tenntenn/golden)
BuildRequires:  go(github.com/tenntenn/modver)
BuildRequires:  go(github.com/tenntenn/text/transform)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/mod/modfile)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/text/transform)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/tools/go/analysis)
BuildRequires:  go(golang.org/x/tools/go/analysis/analysistest)
BuildRequires:  go(golang.org/x/tools/txtar)

# Export the source module roots and every installed Go package.
Provides:       go(github.com/gostaticanalysis/testutil) = %{version}

Requires:       go(github.com/otiai10/copy)
Requires:       go(github.com/tenntenn/modver)
Requires:       go(github.com/tenntenn/text/transform)
Requires:       go(golang.org/x/mod/modfile)
Requires:       go(golang.org/x/text/transform)
Requires:       go(golang.org/x/tools/go/analysis)
Requires:       go(golang.org/x/tools/go/analysis/analysistest)
Requires:       go(golang.org/x/tools/txtar)

%description
Test utilities for Go static analysis packages. This package contains the
complete upstream repository sources and tests.

# Keep fixture module operations offline and use the installed Go toolchain.
%check -p
export GOPROXY=off
export GOSUMDB=off
export GOTOOLCHAIN=local

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
