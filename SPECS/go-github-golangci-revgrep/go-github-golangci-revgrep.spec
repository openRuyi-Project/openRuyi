# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           revgrep
%define go_import_path  github.com/golangci/revgrep

Name:           go-github-golangci-revgrep
Version:        0.8.0
Release:        %autorelease
Summary:        Filter static analysis results by changed lines
License:        Apache-2.0
URL:            https://github.com/golangci/revgrep
#!RemoteAsset:  sha256:42116ab4c63de31474cf01b41891fe7707a7e239669422684804ae2d1475dfe6
Source0:        https://github.com/golangci/revgrep/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.21
BuildRequires:  go-rpm-macros

# External commands used by the upstream tests.
BuildRequires:  bash
BuildRequires:  git

# Export the source module roots and every installed Go package.
Provides:       go(github.com/golangci/revgrep) = %{version}
Provides:       go(github.com/golangci/revgrep/cmd/revgrep) = %{version}

%description
Filter static analysis results by changed lines. This package contains the
complete upstream repository sources and tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
