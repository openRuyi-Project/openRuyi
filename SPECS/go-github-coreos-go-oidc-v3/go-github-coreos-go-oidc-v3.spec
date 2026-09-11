# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-oidc
%define go_import_path  github.com/coreos/go-oidc/v3
# Provider tests contact live OIDC discovery endpoints.
%define go_test_ignore_failure 1

Name:           go-github-coreos-go-oidc-v3
Version:        3.14.1
Release:        %autorelease
Summary:        OpenID Connect client for Go
License:        Apache-2.0
URL:            https://github.com/coreos/go-oidc
#!RemoteAsset:  sha256:9d48558e18521a819bedf60dde068f8be4dedc5a3bca3bb85ad20318d1577307
Source0:        https://github.com/coreos/go-oidc/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-jose/go-jose/v4)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/oauth2)

Provides:       go(github.com/coreos/go-oidc/v3) = %{version}

Requires:       go(github.com/go-jose/go-jose/v4)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/oauth2)

%description
go-oidc/v3 is an OpenID Connect client on top of OAuth 2.0. MinIO uses
the v3 import path; the unversioned go-oidc package is already in the
distro.

%prep -a
# example/ holds sample web apps, not the library.
rm -rf example

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
