# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           decimal
%define go_import_path  github.com/shopspring/decimal

Name:           go-github-shopspring-decimal
Version:        1.4.0
Release:        %autorelease
Summary:        Implements an arbitrary precision fixed-point decimal
License:        MIT
URL:            https://github.com/shopspring/decimal
#!RemoteAsset:  sha256:6ddc6bc4e94a0b3a8366bdd5674b4c2890faca1171afc3f7d20aec95e2c8d413
Source0:        https://github.com/shopspring/decimal/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/shopspring/decimal) = %{version}

%description
Arbitrary-precision fixed-point decimal numbers in go.

Features

 * The zero-value is 0, and is safe to use without initialization
 * Addition, subtraction, multiplication with no loss of precision
 * Division with specified precision
 * Database/sql serialization/deserialization
 * JSON and XML serialization/deserialization

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
