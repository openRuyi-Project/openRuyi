# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           varnamelen
%define go_import_path  github.com/blizzy78/varnamelen

Name:           go-github-blizzy78-varnamelen
Version:        0.8.0
Release:        %autorelease
Summary:        Go analyzer for variable names and scope length
License:        MIT
URL:            https://github.com/blizzy78/varnamelen
#!RemoteAsset:  sha256:8c0ebfe6d58287c6d966fbb768913c054d57d6a7ae91afbcbd45b557d8c95452
Source0:        https://github.com/blizzy78/varnamelen/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.16
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/matryer/is)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/tools/go/analysis)
BuildRequires:  go(golang.org/x/tools/go/analysis/analysistest)
BuildRequires:  go(golang.org/x/tools/go/analysis/passes/inspect)
BuildRequires:  go(golang.org/x/tools/go/analysis/singlechecker)
BuildRequires:  go(golang.org/x/tools/go/ast/inspector)

# Export the source module roots and every installed Go package.
Provides:       go(github.com/blizzy78/varnamelen) = %{version}
Provides:       go(github.com/blizzy78/varnamelen/cmd) = %{version}

Requires:       go(golang.org/x/tools/go/analysis)
Requires:       go(golang.org/x/tools/go/analysis/passes/inspect)
Requires:       go(golang.org/x/tools/go/analysis/singlechecker)
Requires:       go(golang.org/x/tools/go/ast/inspector)

%description
Go analyzer for variable names and scope length. This package contains the
complete upstream repository sources and tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
