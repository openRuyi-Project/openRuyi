# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           typep
%define go_import_path  github.com/go-toolsmith/typep

Name:           go-github-go-toolsmith-typep
Version:        1.1.0
Release:        %autorelease
Summary:        Predicates for Go type information
License:        MIT
URL:            https://github.com/go-toolsmith/typep
#!RemoteAsset:  sha256:a54f3dc060569a6e12b815d6538ebd47d5413b34cbcc4119fae3022274097377
Source0:        https://github.com/go-toolsmith/typep/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.16
BuildRequires:  go-rpm-macros

# Export the source module roots and every installed Go package.
Provides:       go(github.com/go-toolsmith/typep) = %{version}

%description
Predicates for Go type information. This package contains the complete
upstream repository sources and tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
