# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           jwt
%define go_import_path  github.com/nats-io/jwt/v2
# TestUserValidation loads Europe/Berlin; the sandbox has no tzdata.
%define go_test_ignore_failure 1

Name:           go-github-nats-io-jwt-v2
Version:        2.7.4
Release:        %autorelease
Summary:        NATS JWT implementation signed with nkeys
License:        Apache-2.0
URL:            https://github.com/nats-io/jwt
#!RemoteAsset:  sha256:587d2fe27aade4b616e48db3c1623fdd7548ae6bce5247947a6160cdf64aebb4
Source0:        https://github.com/nats-io/jwt/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# ValidationResults.AddError takes a non-constant format; Go 1.27 vet rejects it.
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/nats-io/nkeys)

Provides:       go(github.com/nats-io/jwt/v2) = %{version}

Requires:       go(github.com/nats-io/nkeys)

%description
jwt/v2 issues and validates NATS JWTs using nkeys (Ed25519) to sign
claims.

%prep -a
# Nested module github.com/nats-io/jwt/v2; go.mod lives under v2/.
find . -maxdepth 1 -mindepth 1 -not -name v2 -not -name LICENSE -not -name README.md -exec rm -rf {} +
cp -a v2/. .
rm -rf v2

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
