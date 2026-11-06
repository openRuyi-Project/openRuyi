# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           forbidigo
%define go_import_path  github.com/ashanbrown/forbidigo/v2

Name:           go-github-ashanbrown-forbidigo
Version:        2.3.1
Release:        %autorelease
Summary:        Go analyzer for forbidden identifiers
License:        Apache-2.0
URL:            https://github.com/ashanbrown/forbidigo
#!RemoteAsset:  sha256:f330cb25e863d8adf49a80bbc9bb48a8096cbd412d724c28015e836e3f9aeff8
Source0:        https://github.com/ashanbrown/forbidigo/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.24.0
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/go-cmp/cmp)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/stretchr/testify/assert)
BuildRequires:  go(github.com/stretchr/testify/require)
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/tools/go/analysis)
BuildRequires:  go(golang.org/x/tools/go/analysis/analysistest)
BuildRequires:  go(golang.org/x/tools/go/packages)
BuildRequires:  go(gopkg.in/yaml.v3)

# Export the source module roots and every installed Go package.
Provides:       go(github.com/ashanbrown/forbidigo/v2) = %{version}
Provides:       go(github.com/ashanbrown/forbidigo/v2/examples) = %{version}
Provides:       go(github.com/ashanbrown/forbidigo/v2/forbidigo) = %{version}
Provides:       go(github.com/ashanbrown/forbidigo/v2/pkg/analyzer) = %{version}

Requires:       go(github.com/google/go-cmp/cmp)
Requires:       go(go.yaml.in/yaml/v3)
Requires:       go(golang.org/x/tools/go/analysis)
Requires:       go(golang.org/x/tools/go/packages)

%description
Go analyzer for forbidden identifiers. This package contains the complete
upstream repository sources and tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
