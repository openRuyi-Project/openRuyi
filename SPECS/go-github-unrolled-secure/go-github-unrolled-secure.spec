# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           secure
%define go_import_path  github.com/unrolled/secure

Name:           go-github-unrolled-secure
Version:        1.17.0
Release:        %autorelease
Summary:        HTTP security middleware for Go
License:        MIT
URL:            https://github.com/unrolled/secure
#!RemoteAsset:  sha256:4ea7735c83f88e9dc9c68534bc3a6fc43928aae6e7d2ddfe8f4c80b59f13c39e
Source0:        https://github.com/unrolled/secure/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/unrolled/secure) = %{version}

%description
secure is HTTP middleware that sets security headers such as CSP,
HSTS, and XSS protection.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
