# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           jwt
%define go_import_path  github.com/nats-io/jwt/v2

Name:           go-github-nats-io-jwt-v2
Version:        2.8.2
Release:        %autorelease
Summary:        JWT support for NATS
License:        Apache-2.0
URL:            https://github.com/nats-io/jwt
#!RemoteAsset:  sha256:91fe30f13adbe66e8bdb45bdcb4b50505415ab93c6b5a9fdb2487af777723838
Source0:        https://github.com/nats-io/jwt/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/nats-io/nkeys)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  tzdata

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/nats-io/nkeys)

%description
JWT encoding and validation support for NATS accounts, users, and operators.

%install
pushd v2
%buildsystem_golangmodules_install
popd

%check
pushd v2
%buildsystem_golangmodules_check
popd

%files
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
