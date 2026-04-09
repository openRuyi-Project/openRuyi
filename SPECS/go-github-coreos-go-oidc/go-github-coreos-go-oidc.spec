# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-oidc
%define go_import_path  github.com/coreos/go-oidc

Name:           go-github-coreos-go-oidc
Version:        3.17.0
Release:        %autorelease
Summary:        A Go OpenID Connect client.
License:        Apache-2.0
URL:            https://github.com/coreos/go-oidc
#!RemoteAsset
Source0:        https://github.com/coreos/go-oidc/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-jose/go-jose/v4)
BuildRequires:  go(golang.org/x/oauth2)

Provides:       go(github.com/coreos/go-oidc) = %{version}

Requires:       go(github.com/go-jose/go-jose/v4)
Requires:       go(golang.org/x/oauth2)

%description
OpenID Connect support for Go

This package enables OpenID Connect support for the golang.org/x/oauth2
(https://godoc.org/golang.org/x/oauth2) package.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
