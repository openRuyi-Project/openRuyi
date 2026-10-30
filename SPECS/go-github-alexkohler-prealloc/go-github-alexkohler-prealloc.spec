# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           prealloc
%define go_import_path  github.com/alexkohler/prealloc

Name:           go-github-alexkohler-prealloc
Version:        1.1.0
Release:        %autorelease
Summary:        Go analyzer for slice preallocation opportunities
License:        MIT
URL:            https://github.com/alexkohler/prealloc
#!RemoteAsset:  sha256:fe34c7f66b3c5e79c20a7dc751b7e2136576c624a09689514e2ebac8bd1edc21
Source0:        https://github.com/alexkohler/prealloc/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.24.0
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/tools/go/analysis)
BuildRequires:  go(golang.org/x/tools/go/analysis/analysistest)
BuildRequires:  go(golang.org/x/tools/go/analysis/singlechecker)

# Export the source module roots and every installed Go package.
Provides:       go(github.com/alexkohler/prealloc) = %{version}
Provides:       go(github.com/alexkohler/prealloc/pkg) = %{version}

Requires:       go(golang.org/x/tools/go/analysis)
Requires:       go(golang.org/x/tools/go/analysis/singlechecker)

%description
Go analyzer for slice preallocation opportunities. This package contains the
complete upstream repository sources and tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
