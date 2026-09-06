# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gobreaker
%define go_import_path  github.com/sony/gobreaker

Name:           go-github-sony-gobreaker
Version:        1.0.0
Release:        %autorelease
Summary:        Circuit breaker implementation for Go
License:        MIT
URL:            https://github.com/sony/gobreaker
#!RemoteAsset:  sha256:3c86c1eabb0b5c95776f9fa04bb856d4cdd021a0a0674bc6b27a1de6d98e7deb
Source0:        https://github.com/sony/gobreaker/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Go 1.26 vet rejects a non-constant format string in an upstream test;
# continue running the test without that vet check. - HNO3Miracle
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
Package gobreaker implements the circuit breaker pattern for Go services.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
