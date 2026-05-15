# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           jwt
%define go_import_path  github.com/golang-jwt/jwt/v5

Name:           go-github-golang-jwt-jwt-v5
Version:        5.3.1
Release:        %autorelease
Summary:        Go implementation of JSON Web Tokens (JWT).
License:        MIT
URL:            https://github.com/golang-jwt/jwt
#!RemoteAsset:  sha256:7cb4bbd0b850c52482558d519f4d36f9f3d111d4fb6c93580ae80cb58c6c4444
Source0:        https://github.com/golang-jwt/jwt/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/golang-jwt/jwt/v5) = %{version}

%description
A go (http://www.golang.org) (or 'golang' for search engine
friendliness) implementation of JSON Web Tokens
(https://datatracker.ietf.org/doc/html/rfc7519).

Starting with v4.0.0 (https://github.com/golang-
jwt/jwt/releases/tag/v4.0.0) this project adds Go module support, but
maintains backward compatibility with older v3.x.y tags and upstream
github.com/dgrijalva/jwt-go. See the MIGRATION_GUIDE.md
(/MIGRATION_GUIDE.md) for more information. Version v5.0.0 introduces
major improvements to the validation of tokens, but is not entirely
backward compatible.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
