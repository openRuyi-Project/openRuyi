# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           astp
%define go_import_path  github.com/go-toolsmith/astp

Name:           go-github-go-toolsmith-astp
Version:        1.1.0
Release:        %autorelease
Summary:        Predicates for Go syntax trees
License:        MIT
URL:            https://github.com/go-toolsmith/astp
#!RemoteAsset:  sha256:8b0b2af9a1384d87add2a39c448d20971e8774c149135595f852094749b4705b
Source0:        https://github.com/go-toolsmith/astp/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.16
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-toolsmith/strparse)

# Export the source module roots and every installed Go package.
Provides:       go(github.com/go-toolsmith/astp) = %{version}

%description
Predicates for Go syntax trees. This package contains the complete upstream
repository sources and tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
