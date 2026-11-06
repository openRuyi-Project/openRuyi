# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-printf-func-name
%define go_import_path  github.com/golangci/go-printf-func-name

Name:           go-github-golangci-go-printf-func-name
Version:        0.1.1
Release:        %autorelease
Summary:        Go analyzer for printf-style function names
License:        MIT
URL:            https://github.com/golangci/go-printf-func-name
#!RemoteAsset:  sha256:e057d53ca11ffc956603e4cb1f07a53de096a4526aa90fc8c71d27d2f5e527f7
Source0:        https://github.com/golangci/go-printf-func-name/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.23.0
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
Provides:       go(github.com/golangci/go-printf-func-name) = %{version}
Provides:       go(github.com/golangci/go-printf-func-name/cmd/go-printf-func-name) = %{version}
Provides:       go(github.com/golangci/go-printf-func-name/pkg/analyzer) = %{version}

Requires:       go(golang.org/x/tools/go/analysis)
Requires:       go(golang.org/x/tools/go/analysis/passes/inspect)
Requires:       go(golang.org/x/tools/go/analysis/singlechecker)
Requires:       go(golang.org/x/tools/go/ast/inspector)

%description
Go analyzer for printf-style function names. This package contains the
complete upstream repository sources and tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
