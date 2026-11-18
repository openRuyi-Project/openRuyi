# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           plugin-module-register
%define go_import_path  github.com/golangci/plugin-module-register

Name:           go-github-golangci-plugin-module-register
Version:        0.1.2
Release:        %autorelease
Summary:        Module plugin registration library for Golangci-lint
License:        Apache-2.0
URL:            https://github.com/golangci/plugin-module-register
#!RemoteAsset:  sha256:b3830c2f2f6ce5666c46f696348fdd65c0794a5a92d9417a5943749afffeaa36
Source0:        https://github.com/golangci/plugin-module-register/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.23.0
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/tools/go/analysis)

# Export the source module roots and every installed Go package.
Provides:       go(github.com/golangci/plugin-module-register) = %{version}
Provides:       go(github.com/golangci/plugin-module-register/register) = %{version}

Requires:       go(golang.org/x/tools/go/analysis)

%description
Module plugin registration library for Golangci-lint. This package contains
the complete upstream repository sources and tests.

%files
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
