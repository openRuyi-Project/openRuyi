# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           nilnil
%define go_import_path  github.com/Antonboom/nilnil

Name:           go-github-antonboom-nilnil
Version:        1.1.2
Release:        %autorelease
Summary:        Go analyzer for invalid values returned without errors
License:        MIT
URL:            https://github.com/Antonboom/nilnil
#!RemoteAsset:  sha256:8de149dbf3cf2d9576cd943672a061c154af152bfe30970fc532e4ea28bf9283
Source0:        https://github.com/Antonboom/nilnil/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.24.0
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
Provides:       go(github.com/Antonboom/nilnil) = %{version}
Provides:       go(github.com/Antonboom/nilnil/pkg/analyzer) = %{version}

Requires:       go(golang.org/x/tools/go/analysis)
Requires:       go(golang.org/x/tools/go/analysis/passes/inspect)
Requires:       go(golang.org/x/tools/go/analysis/singlechecker)
Requires:       go(golang.org/x/tools/go/ast/inspector)

%description
Go analyzer for invalid values returned without errors. This package contains
the complete upstream repository sources and tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
