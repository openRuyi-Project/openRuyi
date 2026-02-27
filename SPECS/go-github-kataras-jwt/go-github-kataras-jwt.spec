# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           jwt
%define go_import_path  github.com/kataras/jwt

Name:           go-github-kataras-jwt
Version:        0.1.17
Release:        %autorelease
Summary:        A fast and simple JWT implementation for Go
License:        MIT
URL:            https://github.com/kataras/jwt
#!RemoteAsset
Source0:        https://github.com/kataras/jwt/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/kataras/jwt) = %{version}

%description
Zero-dependency lighweight, fast and simple JWT & JWKS
implementation written in Go. This package was designed
with security, performance and simplicity in mind, it
protects your tokens from critical vulnerabilities that
you may find in other libraries.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%{?autochangelog}
