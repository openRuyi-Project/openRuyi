# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ghinstallation
%define go_import_path  github.com/bradleyfalzon/ghinstallation/v2

Name:           go-github-bradleyfalzon-ghinstallation-v2
Version:        2.0.4
Release:        %autorelease
Summary:        GitHub App authentication transport for Go
License:        Apache-2.0
URL:            https://github.com/bradleyfalzon/ghinstallation
#!RemoteAsset:  sha256:42c04ca5e18b9567a1e2744afcd291f9f8bde9f678a58b170af4583d6a9d0d92
Source0:        https://github.com/bradleyfalzon/ghinstallation/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/golang-jwt/jwt/v4)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/go-github/v41)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/golang-jwt/jwt/v4)
Requires:       go(github.com/google/go-github/v41)

%description
Ghinstallation provides HTTP transports for authenticating GitHub Apps and
installation clients with the GitHub API.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
