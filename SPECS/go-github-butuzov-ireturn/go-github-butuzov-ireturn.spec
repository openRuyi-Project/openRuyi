# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ireturn
%define go_import_path  github.com/butuzov/ireturn

Name:           go-github-butuzov-ireturn
Version:        0.4.1
Release:        %autorelease
Summary:        Go analyzer for functions returning interfaces
License:        MIT
URL:            https://github.com/butuzov/ireturn
#!RemoteAsset:  sha256:7cf0307dab451821660077e7ed97382126d5a80d3cf9fcb438cc27cfaaad1997
Source0:        https://github.com/butuzov/ireturn/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Preserve the any constraint in generic return diagnostics on Go 1.27.
Patch2000:      2000-preserve-empty-generic-constraints.patch

BuildRequires:  go >= 1.25.0
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/stretchr/testify/assert)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/tools/go/analysis)
BuildRequires:  go(golang.org/x/tools/go/analysis/analysistest)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/inspect)
BuildRequires:  go(golang.org/x/tools/go/analysis/singlechecker)
BuildRequires:  go(golang.org/x/tools/go/ast/inspector)
BuildRequires:  go(gopkg.in/yaml.v3)

# Export the source module roots and every installed Go package.
Provides:       go(github.com/butuzov/ireturn) = %{version}
Provides:       go(github.com/butuzov/ireturn/analyzer) = %{version}
Provides:       go(github.com/butuzov/ireturn/analyzer/internal/config) = %{version}
Provides:       go(github.com/butuzov/ireturn/analyzer/internal/types) = %{version}
Provides:       go(github.com/butuzov/ireturn/cmd/ireturn) = %{version}

Requires:       go(golang.org/x/tools/go/analysis)
Requires:       go(golang.org/x/tools/go/analysis/passes/inspect)
Requires:       go(golang.org/x/tools/go/analysis/singlechecker)
Requires:       go(golang.org/x/tools/go/ast/inspector)

%description
Go analyzer for functions returning interfaces. This package contains the
complete upstream repository sources and tests.

%files
%doc readme.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
