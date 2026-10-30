# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-header
%define go_import_path  github.com/denis-tingaikin/go-header

Name:           go-github-denis-tingaikin-go-header
Version:        0.5.0
Release:        %autorelease
Summary:        Go analyzer for source license headers
License:        Apache-2.0 AND GPL-3.0-only
URL:            https://github.com/denis-tingaikin/go-header
#!RemoteAsset:  sha256:bffb5eb71ef30db6503ef40ccad3aff0377e944cd4193dc6d2ad08a66e4ec552
Source0:        https://github.com/denis-tingaikin/go-header/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.21
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/stretchr/testify/require)
BuildRequires:  go(gopkg.in/yaml.v3)

# External commands used by the upstream tests.
BuildRequires:  git

# Export the source module roots and every installed Go package.
Provides:       go(github.com/denis-tingaikin/go-header) = %{version}
Provides:       go(github.com/denis-tingaikin/go-header/cmd/go-header) = %{version}
Provides:       go(github.com/denis-tingaikin/go-header/version) = %{version}

Requires:       go(gopkg.in/yaml.v3)

%description
Go analyzer for source license headers. This package contains the complete
upstream repository sources and tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
