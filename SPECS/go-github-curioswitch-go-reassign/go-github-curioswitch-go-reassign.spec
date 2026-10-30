# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-reassign
%define go_import_path  github.com/curioswitch/go-reassign

Name:           go-github-curioswitch-go-reassign
Version:        0.3.0
Release:        %autorelease
Summary:        Go analyzer for reassigned package variables
License:        MIT
URL:            https://github.com/curioswitch/go-reassign
#!RemoteAsset:  sha256:f11f47c0ad5b082820260c75a84296c7e3362aacf4a3aac67c56f90413f87955
Source0:        https://github.com/curioswitch/go-reassign/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.21
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/magefile/mage)
BuildRequires:  go(github.com/magefile/mage/mage)
BuildRequires:  go(github.com/magefile/mage/sh)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/tools/go/analysis)
BuildRequires:  go(golang.org/x/tools/go/analysis/analysistest)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/inspect)
BuildRequires:  go(golang.org/x/tools/go/analysis/singlechecker)
BuildRequires:  go(golang.org/x/tools/go/ast/inspector)

# Export the source module roots and every installed Go package.
Provides:       go(github.com/curioswitch/go-reassign) = %{version}
Provides:       go(github.com/curioswitch/go-reassign/cmd) = %{version}
Provides:       go(github.com/curioswitch/go-reassign/internal/analyzer) = %{version}
Provides:       go(github.com/curioswitch/go-reassign/magefiles) = %{version}

Requires:       go(github.com/magefile/mage/mage)
Requires:       go(github.com/magefile/mage/sh)
Requires:       go(golang.org/x/tools/go/analysis)
Requires:       go(golang.org/x/tools/go/analysis/passes/inspect)
Requires:       go(golang.org/x/tools/go/analysis/singlechecker)
Requires:       go(golang.org/x/tools/go/ast/inspector)

%description
Go analyzer for reassigned package variables. This package contains the
complete upstream repository sources and tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
