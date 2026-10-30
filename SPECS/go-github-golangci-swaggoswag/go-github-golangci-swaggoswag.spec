# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           swaggoswag
%define go_import_path  github.com/golangci/swaggoswag

Name:           go-github-golangci-swaggoswag
Version:        0+git20261022.77f2aca
Release:        %autorelease
Summary:        Swagger annotation parser adapter for Golangci-lint
License:        MIT
URL:            https://github.com/golangci/swaggoswag
#!RemoteAsset:  sha256:9bdae1eee3de78402ebdb8fcd15ac09caff747cb9a27ddffa44dde001330131f
Source0:        https://codeload.github.com/golangci/swaggoswag/tar.gz/77f2aca3143e3e68e6cd086926f61bb1fd6584cc#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.23.0
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/stretchr/testify/assert)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/tools/imports)
BuildRequires:  go(gopkg.in/yaml.v3)

# Export the source module roots and every installed Go package.
Provides:       go(github.com/golangci/swaggoswag) = %{version}

Requires:       go(golang.org/x/tools/imports)

%description
Swagger annotation parser adapter for Golangci-lint. This package contains
the complete upstream repository sources and tests.

%prep
%autosetup -n swaggoswag-77f2aca3143e3e68e6cd086926f61bb1fd6584cc

%files
%doc readme.md
%license license
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
