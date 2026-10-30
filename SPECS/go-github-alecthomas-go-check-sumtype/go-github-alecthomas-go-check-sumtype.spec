# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-check-sumtype
%define go_import_path  github.com/alecthomas/go-check-sumtype

Name:           go-github-alecthomas-go-check-sumtype
Version:        0.5.0
Release:        %autorelease
Summary:        Exhaustiveness checker for Go sum types
License:        MIT OR Unlicense
URL:            https://github.com/alecthomas/go-check-sumtype
#!RemoteAsset:  sha256:86727598bed7a80ebb318180f9db56c4e52b8f6bca0f7c50d6cca9ac3eeca2e2
Source0:        https://github.com/alecthomas/go-check-sumtype/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.27.0
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/tools/go/analysis)
BuildRequires:  go(golang.org/x/tools/go/analysis/analysistest)
BuildRequires:  go(golang.org/x/tools/go/analysis/singlechecker)

# Export the source module roots and every installed Go package.
Provides:       go(github.com/alecthomas/go-check-sumtype) = %{version}
Provides:       go(github.com/alecthomas/go-check-sumtype/cmd/go-check-sumtype) = %{version}

Requires:       go(golang.org/x/tools/go/analysis)
Requires:       go(golang.org/x/tools/go/analysis/singlechecker)

%description
Exhaustiveness checker for Go sum types. This package contains the complete
upstream repository sources and tests.

%files
%doc README.md
%license COPYING
%license LICENSE-MIT
%license UNLICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
