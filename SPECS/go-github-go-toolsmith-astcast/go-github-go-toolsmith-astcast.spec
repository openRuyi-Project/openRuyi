# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           astcast
%define go_import_path  github.com/go-toolsmith/astcast

Name:           go-github-go-toolsmith-astcast
Version:        1.1.0
Release:        %autorelease
Summary:        Convenient type assertions for Go syntax trees
License:        MIT
URL:            https://github.com/go-toolsmith/astcast
#!RemoteAsset:  sha256:ecb8c5a624c0d4c2d9728e02cf22c065adf8c0208f34bca85c5045a3c1085850
Source0:        https://github.com/go-toolsmith/astcast/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.16
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-toolsmith/strparse)

# Export the source module roots and every installed Go package.
Provides:       go(github.com/go-toolsmith/astcast) = %{version}

%description
Convenient type assertions for Go syntax trees. This package contains the
complete upstream repository sources and tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
