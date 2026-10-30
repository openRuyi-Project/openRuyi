# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           errchkjson
%define go_import_path  github.com/breml/errchkjson

Name:           go-github-breml-errchkjson
Version:        0.4.2
Release:        %autorelease
Summary:        Go analyzer for JSON encoding error checks
License:        MIT
URL:            https://github.com/breml/errchkjson
#!RemoteAsset:  sha256:352fc42c22fd8aeb63addd2fc0896adcdd70c36d9bb70f8dc0f4022d6cb4adf7
Source0:        https://github.com/breml/errchkjson/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.26.0
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/tools/go/analysis)
BuildRequires:  go(golang.org/x/tools/go/analysis/analysistest)
BuildRequires:  go(golang.org/x/tools/go/analysis/singlechecker)
BuildRequires:  go(golang.org/x/tools/go/types/typeutil)

# Export the source module roots and every installed Go package.
Provides:       go(github.com/breml/errchkjson) = %{version}
Provides:       go(github.com/breml/errchkjson/cmd/errchkjson) = %{version}

Requires:       go(golang.org/x/tools/go/analysis)
Requires:       go(golang.org/x/tools/go/analysis/singlechecker)
Requires:       go(golang.org/x/tools/go/types/typeutil)

%description
Go analyzer for JSON encoding error checks. This package contains the
complete upstream repository sources and tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
