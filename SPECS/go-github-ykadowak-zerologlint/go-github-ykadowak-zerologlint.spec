# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           zerologlint
%define go_import_path  github.com/ykadowak/zerologlint

Name:           go-github-ykadowak-zerologlint
Version:        0.1.5
Release:        %autorelease
Summary:        Zerologlint is a linter for zerolog that can be run with go vet or through golangci-lint since v1.53.0
License:        MIT
URL:            https://github.com/ykadowak/zerologlint
#!RemoteAsset:  sha256:5453a2b966ba221adcc1f082446708976b9144eb2387dcd9057fb18d747fd47b
Source0:        https://github.com/ykadowak/zerologlint/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/gostaticanalysis/comment)
BuildRequires:  go(github.com/gostaticanalysis/testutil)
BuildRequires:  go(github.com/hashicorp/go-version)
BuildRequires:  go(github.com/mattn/go-colorable)
BuildRequires:  go(github.com/mattn/go-isatty)
BuildRequires:  go(github.com/otiai10/copy)
BuildRequires:  go(github.com/rs/zerolog)
BuildRequires:  go(github.com/tenntenn/modver)
BuildRequires:  go(github.com/tenntenn/text/transform)
BuildRequires:  go(golang.org/x/exp)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/ykadowak/zerologlint) = %{version}

Requires:       go(github.com/gostaticanalysis/comment)
Requires:       go(golang.org/x/tools)

%description
Zerologlint is a linter for zerolog that can be run with go vet or through golangci-lint since v1.53.0.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n zerologlint-%{version}

# Use packaged source trees for temporary analyzer modules because OBS has no
# Go module proxy access.
%check -p
export GOPROXY=off
export GOSUMDB=off
export GOTOOLCHAIN=local
go mod edit \
    -replace=github.com/rs/zerolog=%{go_sys_gopath}/github.com/rs/zerolog \
    -replace=github.com/mattn/go-colorable=%{go_sys_gopath}/github.com/mattn/go-colorable \
    -replace=github.com/mattn/go-isatty=%{go_sys_gopath}/github.com/mattn/go-isatty \
    -replace=golang.org/x/exp=%{go_sys_gopath}/golang.org/x/exp \
    -replace=golang.org/x/sys=%{go_sys_gopath}/golang.org/x/sys \
    testdata/src/a/go.mod

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/github.com/ykadowak/zerologlint

%changelog
%autochangelog
