# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           strparse
%define go_import_path  github.com/go-toolsmith/strparse

Name:           go-github-go-toolsmith-strparse
Version:        1.1.0
Release:        %autorelease
Summary:        Go syntax parser helpers for strings
License:        MIT
URL:            https://github.com/go-toolsmith/strparse
#!RemoteAsset:  sha256:822c63bb396f5a0d75a5a24136355593cc4d72afe71f019b4128577598e62680
Source0:        https://github.com/go-toolsmith/strparse/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.16
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-toolsmith/astequal)

# Export the source module roots and every installed Go package.
Provides:       go(github.com/go-toolsmith/strparse) = %{version}

%description
Go syntax parser helpers for strings. This package contains the complete
upstream repository sources and tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
