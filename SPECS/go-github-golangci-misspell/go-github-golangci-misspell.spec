# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           misspell
%define go_import_path  github.com/golangci/misspell

Name:           go-github-golangci-misspell
Version:        0.8.0
Release:        %autorelease
Summary:        English spelling correction library for Golangci-lint
License:        MIT
URL:            https://github.com/golangci/misspell
#!RemoteAsset:  sha256:b54e4975a3756465d4bd95a373c6953d3e292edb0581fb066648cc394024f817
Source0:        https://github.com/golangci/misspell/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.23.0
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/gobwas/glob)

# Export the source module roots and every installed Go package.
Provides:       go(github.com/golangci/misspell) = %{version}
Provides:       go(github.com/golangci/misspell/cmd/misspell) = %{version}
Provides:       go(github.com/golangci/misspell/ignore) = %{version}
Provides:       go(github.com/golangci/misspell/internal/gen) = %{version}

Requires:       go(github.com/gobwas/glob)

%description
English spelling correction library for Golangci-lint. This package contains
the complete upstream repository sources and tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
