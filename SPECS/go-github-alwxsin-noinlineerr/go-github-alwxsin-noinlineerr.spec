# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           noinlineerr
%define go_import_path  github.com/AlwxSin/noinlineerr

Name:           go-github-alwxsin-noinlineerr
Version:        1.0.6
Release:        %autorelease
Summary:        Go analyzer for inline error handling
License:        MIT
URL:            https://github.com/AlwxSin/noinlineerr
#!RemoteAsset:  sha256:32cfdfea0fb14cf516b4f134ec8c99b2d91b6d204b95371fbe7e55bc3693e77a
Source0:        https://github.com/AlwxSin/noinlineerr/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Go 1.26 vet rejects the dynamic message passed to Reportf.
Patch2000:       2000-use-diagnostic-for-dynamic-message.patch

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
Provides:       go(github.com/AlwxSin/noinlineerr) = %{version}
Provides:       go(github.com/AlwxSin/noinlineerr/cmd/noinlineerr) = %{version}

Requires:       go(golang.org/x/tools/go/analysis)
Requires:       go(golang.org/x/tools/go/analysis/passes/inspect)
Requires:       go(golang.org/x/tools/go/analysis/singlechecker)
Requires:       go(golang.org/x/tools/go/ast/inspector)

%description
Go analyzer for inline error handling. This package contains the complete
upstream repository sources and tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
