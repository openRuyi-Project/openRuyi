# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           pbkdf2
%define go_import_path  github.com/xdg-go/pbkdf2

Name:           go-github-xdg-go-pbkdf2
Version:        1.0.0
Release:        %autorelease
Summary:        Password-based key derivation for Go
License:        Apache-2.0
URL:            https://github.com/xdg-go/pbkdf2
#!RemoteAsset:  sha256:2eec55146447215eb58190e04c546c93cad7f369ac9b5aacd9dc11330d756757
Source0:        https://github.com/xdg-go/pbkdf2/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/xdg-go/pbkdf2) = %{version}

%description
PBKDF2 derives keys from passwords using a pseudorandom function, following
RFC 2898 and RFC 8018.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
