# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           astfmt
%define go_import_path  github.com/go-toolsmith/astfmt

Name:           go-github-go-toolsmith-astfmt
Version:        1.1.0
Release:        %autorelease
Summary:        Formatting helpers for Go syntax trees
License:        MIT
URL:            https://github.com/go-toolsmith/astfmt
#!RemoteAsset:  sha256:dad80d1d4dd94c60c7f1d386f12fcbe7090dc5e4f12ad4c9835ef2eae638be90
Source0:        https://github.com/go-toolsmith/astfmt/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.16
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-toolsmith/strparse)

# Export the source module roots and every installed Go package.
Provides:       go(github.com/go-toolsmith/astfmt) = %{version}

%description
Formatting helpers for Go syntax trees. This package contains the complete
upstream repository sources and tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
