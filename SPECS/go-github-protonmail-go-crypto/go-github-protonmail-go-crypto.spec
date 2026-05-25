# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-crypto
%define go_import_path  github.com/ProtonMail/go-crypto

Name:           go-github-protonmail-go-crypto
Version:        1.4.1~proton
Release:        %autorelease
Summary:        Fork of go/x/crypto, providing an up-to-date OpenPGP implementation
License:        BSD-3-Clause
URL:            https://github.com/ProtonMail/go-crypto
#!RemoteAsset:  sha256:2b7f353dca703b103c23fc2b378bcdc448abe7fb1bae0a0713ea61c5f29013f9
Source0:        https://github.com/ProtonMail/go-crypto/archive/refs/tags/v1.4.1-proton.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# The forwarding test should use this module's OpenPGP armor package; current
# golang.org/x/crypto no longer ships golang.org/x/crypto/openpgp/armor.
Patch0:         2000-use-local-openpgp-armor-in-forwarding-test.patch

BuildOption(prep):  -n go-crypto-1.4.1-proton

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/cloudflare/circl)
BuildRequires:  go(github.com/cloudflare/circl/dh/x25519)
BuildRequires:  go(github.com/cloudflare/circl/dh/x448)
BuildRequires:  go(github.com/cloudflare/circl/kem)
BuildRequires:  go(github.com/cloudflare/circl/kem/mlkem/mlkem1024)
BuildRequires:  go(github.com/cloudflare/circl/kem/mlkem/mlkem768)
BuildRequires:  go(github.com/cloudflare/circl/sign)
BuildRequires:  go(github.com/cloudflare/circl/sign/ed25519)
BuildRequires:  go(github.com/cloudflare/circl/sign/ed448)
BuildRequires:  go(github.com/cloudflare/circl/sign/mldsa/mldsa65)
BuildRequires:  go(github.com/cloudflare/circl/sign/mldsa/mldsa87)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/crypto/argon2)
BuildRequires:  go(golang.org/x/crypto/cast5)
BuildRequires:  go(golang.org/x/crypto/hkdf)
BuildRequires:  go(golang.org/x/crypto/ripemd160)
BuildRequires:  go(golang.org/x/crypto/sha3)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/ProtonMail/go-crypto) = %{version}
Provides:       go(github.com/ProtonMail/go-crypto/bitcurves) = %{version}
Provides:       go(github.com/ProtonMail/go-crypto/brainpool) = %{version}
Provides:       go(github.com/ProtonMail/go-crypto/eax) = %{version}
Provides:       go(github.com/ProtonMail/go-crypto/internal/byteutil) = %{version}
Provides:       go(github.com/ProtonMail/go-crypto/ocb) = %{version}
Provides:       go(github.com/ProtonMail/go-crypto/openpgp) = %{version}
Provides:       go(github.com/ProtonMail/go-crypto/openpgp/aes/keywrap) = %{version}
Provides:       go(github.com/ProtonMail/go-crypto/openpgp/armor) = %{version}
Provides:       go(github.com/ProtonMail/go-crypto/openpgp/clearsign) = %{version}
Provides:       go(github.com/ProtonMail/go-crypto/openpgp/ecdh) = %{version}
Provides:       go(github.com/ProtonMail/go-crypto/openpgp/ecdsa) = %{version}
Provides:       go(github.com/ProtonMail/go-crypto/openpgp/ed25519) = %{version}
Provides:       go(github.com/ProtonMail/go-crypto/openpgp/ed448) = %{version}
Provides:       go(github.com/ProtonMail/go-crypto/openpgp/eddsa) = %{version}
Provides:       go(github.com/ProtonMail/go-crypto/openpgp/elgamal) = %{version}
Provides:       go(github.com/ProtonMail/go-crypto/openpgp/errors) = %{version}
Provides:       go(github.com/ProtonMail/go-crypto/openpgp/integration_tests) = %{version}
Provides:       go(github.com/ProtonMail/go-crypto/openpgp/integration_tests/v2) = %{version}
Provides:       go(github.com/ProtonMail/go-crypto/openpgp/internal/algorithm) = %{version}
Provides:       go(github.com/ProtonMail/go-crypto/openpgp/internal/ecc) = %{version}
Provides:       go(github.com/ProtonMail/go-crypto/openpgp/internal/ecc/curve25519) = %{version}
Provides:       go(github.com/ProtonMail/go-crypto/openpgp/internal/ecc/curve25519/field) = %{version}
Provides:       go(github.com/ProtonMail/go-crypto/openpgp/internal/encoding) = %{version}
Provides:       go(github.com/ProtonMail/go-crypto/openpgp/mldsa_eddsa) = %{version}
Provides:       go(github.com/ProtonMail/go-crypto/openpgp/mlkem_ecdh) = %{version}
Provides:       go(github.com/ProtonMail/go-crypto/openpgp/packet) = %{version}
Provides:       go(github.com/ProtonMail/go-crypto/openpgp/s2k) = %{version}
Provides:       go(github.com/ProtonMail/go-crypto/openpgp/symmetric) = %{version}
Provides:       go(github.com/ProtonMail/go-crypto/openpgp/v2) = %{version}
Provides:       go(github.com/ProtonMail/go-crypto/openpgp/x25519) = %{version}
Provides:       go(github.com/ProtonMail/go-crypto/openpgp/x448) = %{version}

Requires:       go(github.com/cloudflare/circl)
Requires:       go(github.com/cloudflare/circl/dh/x25519)
Requires:       go(github.com/cloudflare/circl/dh/x448)
Requires:       go(github.com/cloudflare/circl/kem)
Requires:       go(github.com/cloudflare/circl/kem/mlkem/mlkem1024)
Requires:       go(github.com/cloudflare/circl/kem/mlkem/mlkem768)
Requires:       go(github.com/cloudflare/circl/sign)
Requires:       go(github.com/cloudflare/circl/sign/ed25519)
Requires:       go(github.com/cloudflare/circl/sign/ed448)
Requires:       go(github.com/cloudflare/circl/sign/mldsa/mldsa65)
Requires:       go(github.com/cloudflare/circl/sign/mldsa/mldsa87)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/crypto/argon2)
Requires:       go(golang.org/x/crypto/cast5)
Requires:       go(golang.org/x/crypto/hkdf)
Requires:       go(golang.org/x/crypto/sha3)
Requires:       go(golang.org/x/sys)


%description
go get github.com/ProtonMail/go-crypto

This module is backwards compatible with x/crypto/openpgp, so you can
simply replace all imports of golang.org/x/crypto/openpgp with
github.com/ProtonMail/go-crypto/openpgp.

A partial list of changes is here: (https://github.com/ProtonMail/go-
crypto/issues/21#issuecomment-492792917).

For the more extended API for reading and writing OpenPGP messages use
github.com/ProtonMail/go-crypto/openpgp/v2, but it is not fully

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
