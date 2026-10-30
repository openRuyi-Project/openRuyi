# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gocyclo
%define go_import_path  github.com/fzipp/gocyclo

Name:           go-github-fzipp-gocyclo
Version:        0.6.0
Release:        %autorelease
Summary:        Cyclomatic complexity analyzer for Go functions
License:        BSD-3-Clause
URL:            https://github.com/fzipp/gocyclo
#!RemoteAsset:  sha256:2cf9b301b6582f11bb41c4fcc24c50b74ea49db21704f1e4ba1f9c1d614f223a
Source0:        https://github.com/fzipp/gocyclo/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.18
BuildRequires:  go-rpm-macros

# Export the source module roots and every installed Go package.
Provides:       go(github.com/fzipp/gocyclo) = %{version}
Provides:       go(github.com/fzipp/gocyclo/cmd/gocyclo) = %{version}

%description
Cyclomatic complexity analyzer for Go functions. This package contains the
complete upstream repository sources and tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
