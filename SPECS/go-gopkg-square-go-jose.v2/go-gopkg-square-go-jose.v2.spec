# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-jose.v2
%define go_import_path  gopkg.in/square/go-jose.v2

Name:           go-gopkg-square-go-jose.v2
Version:        2.2.2
Release:        %autorelease
Summary:        JSON signing and encryption library for Go
License:        Apache-2.0
URL:            https://github.com/square/go-jose
#!RemoteAsset:  sha256:2c1a56585d5f2a9a38d07d5c2b8feac1fe7b8f594145ccf4bd962dd6a313a169
Source0:        https://github.com/square/go-jose/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Current Go vet rejects non-constant format strings in the examples.
BuildOption(check):  -vet=off
# The certificate fixture only has a Common Name, and modern RSA PKCS1v15
# signing ignores the random reader. Both tests assume older Go behavior.
BuildOption(check):  -skip '^(TestJWSWithCertificateChain|TestSignerWithBrokenRand)$'

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/crypto)

Provides:       go(gopkg.in/square/go-jose.v2) = %{version}

Requires:       go(golang.org/x/crypto)

%description
This library implements JSON Web Signature, JSON Web Encryption and
JSON Web Token standards using the original Square import path.

%prep -a
# The command-line examples are not part of the importable JOSE library.
rm -rf jose-util jwk-keygen

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
