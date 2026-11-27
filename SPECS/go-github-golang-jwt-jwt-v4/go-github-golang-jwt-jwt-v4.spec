# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           jwt
%define go_import_path  github.com/golang-jwt/jwt/v4

Name:           go-github-golang-jwt-jwt-v4
Version:        4.5.2
Release:        %autorelease
Summary:        JSON Web Token implementation for Go
License:        MIT
URL:            https://github.com/golang-jwt/jwt
#!RemoteAsset:  sha256:afbc9dcfa1a78496eec86782ea4aa8a829339d5debc3cf7efe121d506679b0b9
Source0:        https://github.com/golang-jwt/jwt/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
Package jwt implements JSON Web Tokens in Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
