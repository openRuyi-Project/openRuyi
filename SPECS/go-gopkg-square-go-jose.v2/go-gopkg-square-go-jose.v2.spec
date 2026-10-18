# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-jose
%define go_import_path  gopkg.in/square/go-jose.v2

Name:           go-gopkg-square-go-jose.v2
Version:        2.6.0
Release:        %autorelease
Summary:        Legacy Go implementation of JSON Web Signature and Encryption
License:        Apache-2.0 AND BSD-3-Clause
URL:            https://github.com/square/go-jose
#!RemoteAsset:  sha256:0c1556d9675158342ca7ed875b3b40ea534861b96a5a75b1eb3f6637503b9a76
Source0:        https://github.com/square/go-jose/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/alecthomas/kingpin/v2)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/crypto)

Provides:       go(gopkg.in/square/go-jose.v2) = %{version}
Provides:       go(gopkg.in/square/go-jose.v2/cipher) = %{version}
Provides:       go(gopkg.in/square/go-jose.v2/cryptosigner) = %{version}
Provides:       go(gopkg.in/square/go-jose.v2/json) = %{version}
Provides:       go(gopkg.in/square/go-jose.v2/jwt) = %{version}

Requires:       go(github.com/alecthomas/kingpin/v2)
Requires:       go(golang.org/x/crypto)

%patchlist
# https://github.com/go-jose/go-jose/pull/87
1000-tests-support-Go-1.20-RSA-randomness.patch
# Limit attacker-controlled PBES2 work to prevent decryption denial of service.
# https://github.com/go-jose/go-jose/pull/76
1001-limit-PBES2-iteration-count.patch
# CVE-2024-28180: limit JWE decompression memory and CPU use.
# https://github.com/go-jose/go-jose/pull/109
1002-limit-JWE-decompression.patch
# Use constant format strings in examples with current Go vet.
2000-fix-non-constant-format-strings-in-examples.patch
# Use the packaged kingpin v2 module in both command packages.
2001-use-packaged-kingpin-module.patch

%description
Go JOSE implements JSON Web Signature, Encryption, Key, and Token standards.
This compatibility package installs the historical square import path;
the newer gopkg.in/go-jose/go-jose.v2 package uses a different source path.

%files
%doc README.md
%license LICENSE json/LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
