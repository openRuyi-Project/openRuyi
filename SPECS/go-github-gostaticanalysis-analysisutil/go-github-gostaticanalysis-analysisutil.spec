# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           analysisutil
%define go_import_path  github.com/gostaticanalysis/analysisutil

Name:           go-github-gostaticanalysis-analysisutil
Version:        0.7.1
Release:        %autorelease
Summary:        Utilities for Go analysis packages
License:        MIT
URL:            https://github.com/gostaticanalysis/analysisutil
#!RemoteAsset:  sha256:97675d7bd0df22e1b58e48cf6cce3f70ebff10c0f177b02ed2e62c0dc6a571cf
Source0:        https://github.com/gostaticanalysis/analysisutil/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.16
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/gostaticanalysis/comment)
BuildRequires:  go(github.com/gostaticanalysis/comment/passes/commentmap)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/tools/go/analysis)
BuildRequires:  go(golang.org/x/tools/go/analysis/analysistest)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/buildssa)
BuildRequires:  go(golang.org/x/tools/go/packages)
BuildRequires:  go(golang.org/x/tools/go/packages/packagestest)
BuildRequires:  go(golang.org/x/tools/go/ssa)

# Export the source module roots and every installed Go package.
Provides:       go(github.com/gostaticanalysis/analysisutil) = %{version}

Requires:       go(github.com/gostaticanalysis/comment)
Requires:       go(github.com/gostaticanalysis/comment/passes/commentmap)
Requires:       go(golang.org/x/tools/go/analysis)
Requires:       go(golang.org/x/tools/go/ssa)

%description
Utilities for Go analysis packages. This package contains the complete
upstream repository sources and tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
