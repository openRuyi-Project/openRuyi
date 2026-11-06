# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ineffassign
%define go_import_path  github.com/gordonklaus/ineffassign

Name:           go-github-gordonklaus-ineffassign
Version:        0.2.0
Release:        %autorelease
Summary:        Go analyzer for ineffectual assignments
License:        MIT
URL:            https://github.com/gordonklaus/ineffassign
#!RemoteAsset:  sha256:5b0256a4151ec313ce65921f7434c70149aeb3056867a8e502bca4e7a06770a0
Source0:        https://github.com/gordonklaus/ineffassign/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.23.0
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/tools/go/analysis)
BuildRequires:  go(golang.org/x/tools/go/analysis/analysistest)
BuildRequires:  go(golang.org/x/tools/go/packages)

# Export the source module roots and every installed Go package.
Provides:       go(github.com/gordonklaus/ineffassign) = %{version}
Provides:       go(github.com/gordonklaus/ineffassign/pkg/ineffassign) = %{version}

Requires:       go(golang.org/x/tools/go/analysis)
Requires:       go(golang.org/x/tools/go/packages)

%description
Go analyzer for ineffectual assignments. This package contains the complete
upstream repository sources and tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
