# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           tagalign
%define go_import_path  github.com/4meepo/tagalign

Name:           go-github-4meepo-tagalign
Version:        1.4.4
Release:        %autorelease
Summary:        Go analyzer for consistent struct tag alignment
License:        MIT
URL:            https://github.com/4meepo/tagalign
#!RemoteAsset:  sha256:f128fd09b28f75cdb9986aef6d21967b127cfd08e44dad690feec0f3cdc936c4
Source0:        https://github.com/4meepo/tagalign/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.22.0
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/alfatraining/structtag)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/kr/pretty)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/stretchr/testify/assert)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/tools/go/analysis)
BuildRequires:  go(golang.org/x/tools/go/analysis/analysistest)
BuildRequires:  go(golang.org/x/tools/go/analysis/singlechecker)
BuildRequires:  go(gopkg.in/check.v1)
BuildRequires:  go(gopkg.in/yaml.v3)

# Export the source module roots and every installed Go package.
Provides:       go(github.com/4meepo/tagalign) = %{version}
Provides:       go(github.com/4meepo/tagalign/cmd/tagalign) = %{version}

Requires:       go(github.com/alfatraining/structtag)
Requires:       go(golang.org/x/tools/go/analysis)
Requires:       go(golang.org/x/tools/go/analysis/singlechecker)

%description
Go analyzer for consistent struct tag alignment. This package contains the
complete upstream repository sources and tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
