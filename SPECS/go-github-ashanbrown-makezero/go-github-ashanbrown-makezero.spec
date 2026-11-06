# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           makezero
%define go_import_path  github.com/ashanbrown/makezero/v2

Name:           go-github-ashanbrown-makezero
Version:        2.2.1
Release:        %autorelease
Summary:        Go analyzer for nonzero slice initialization before append
License:        Apache-2.0
URL:            https://github.com/ashanbrown/makezero
#!RemoteAsset:  sha256:f7192b9a6f1c7ddf4a8e7659da2198abd55d5a15a7570e5dba82891716ce86e5
Source0:        https://github.com/ashanbrown/makezero/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.24.0
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/tools/go/analysis)
BuildRequires:  go(golang.org/x/tools/go/analysis/analysistest)
BuildRequires:  go(golang.org/x/tools/go/packages)

# Export the source module roots and every installed Go package.
Provides:       go(github.com/ashanbrown/makezero/v2) = %{version}
Provides:       go(github.com/ashanbrown/makezero/v2/examples) = %{version}
Provides:       go(github.com/ashanbrown/makezero/v2/makezero) = %{version}
Provides:       go(github.com/ashanbrown/makezero/v2/pkg/analyzer) = %{version}

Requires:       go(golang.org/x/tools/go/analysis)
Requires:       go(golang.org/x/tools/go/packages)

%description
Go analyzer for nonzero slice initialization before append. This package
contains the complete upstream repository sources and tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
