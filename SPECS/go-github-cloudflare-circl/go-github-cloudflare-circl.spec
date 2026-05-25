# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           circl
%define go_import_path  github.com/cloudflare/circl

Name:           go-github-cloudflare-circl
Version:        1.6.3
Release:        %autorelease
Summary:        CIRCL: Cloudflare Interoperable Reusable Cryptographic Library
License:        BSD-3-Clause
URL:            https://github.com/cloudflare/circl
#!RemoteAsset:  sha256:1bf5a8618060d189780981675ef41fadf80da00069e80fa85c79554ed339d955
Source0:        https://github.com/cloudflare/circl/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n circl-1.6.3

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/bwesterb/go-ristretto)
BuildRequires:  go(github.com/mmcloughlin/avo/build)
BuildRequires:  go(github.com/mmcloughlin/avo/operand)
BuildRequires:  go(github.com/mmcloughlin/avo/reg)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/crypto/blake2b)
BuildRequires:  go(golang.org/x/crypto/blake2s)
BuildRequires:  go(golang.org/x/crypto/chacha20poly1305)
BuildRequires:  go(golang.org/x/crypto/cryptobyte)
BuildRequires:  go(golang.org/x/crypto/cryptobyte/asn1)
BuildRequires:  go(golang.org/x/crypto/hkdf)
BuildRequires:  go(golang.org/x/crypto/nacl/box)
BuildRequires:  go(golang.org/x/crypto/sha3)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/sys/cpu)

Provides:       go(github.com/cloudflare/circl) = %{version}
Provides:       go(github.com/cloudflare/circl/abe) = %{version}
Provides:       go(github.com/cloudflare/circl/abe/cpabe) = %{version}
Provides:       go(github.com/cloudflare/circl/abe/cpabe/tkn20) = %{version}
Provides:       go(github.com/cloudflare/circl/abe/cpabe/tkn20/internal/dsl) = %{version}
Provides:       go(github.com/cloudflare/circl/abe/cpabe/tkn20/internal/tkn) = %{version}
Provides:       go(github.com/cloudflare/circl/blindsign) = %{version}
Provides:       go(github.com/cloudflare/circl/blindsign/blindrsa) = %{version}
Provides:       go(github.com/cloudflare/circl/blindsign/blindrsa/internal/common) = %{version}
Provides:       go(github.com/cloudflare/circl/blindsign/blindrsa/internal/keys) = %{version}
Provides:       go(github.com/cloudflare/circl/blindsign/blindrsa/partiallyblindrsa) = %{version}
Provides:       go(github.com/cloudflare/circl/cipher) = %{version}
Provides:       go(github.com/cloudflare/circl/cipher/ascon) = %{version}
Provides:       go(github.com/cloudflare/circl/dh) = %{version}
Provides:       go(github.com/cloudflare/circl/dh/csidh) = %{version}
Provides:       go(github.com/cloudflare/circl/dh/curve4q) = %{version}
Provides:       go(github.com/cloudflare/circl/dh/sidh) = %{version}
Provides:       go(github.com/cloudflare/circl/dh/sidh/internal/common) = %{version}
Provides:       go(github.com/cloudflare/circl/dh/sidh/internal/p434) = %{version}
Provides:       go(github.com/cloudflare/circl/dh/sidh/internal/p503) = %{version}
Provides:       go(github.com/cloudflare/circl/dh/sidh/internal/p751) = %{version}
Provides:       go(github.com/cloudflare/circl/dh/x25519) = %{version}
Provides:       go(github.com/cloudflare/circl/dh/x448) = %{version}
Provides:       go(github.com/cloudflare/circl/ecc) = %{version}
Provides:       go(github.com/cloudflare/circl/ecc/bls12381) = %{version}
Provides:       go(github.com/cloudflare/circl/ecc/bls12381/ff) = %{version}
Provides:       go(github.com/cloudflare/circl/ecc/fourq) = %{version}
Provides:       go(github.com/cloudflare/circl/ecc/goldilocks) = %{version}
Provides:       go(github.com/cloudflare/circl/ecc/p384) = %{version}
Provides:       go(github.com/cloudflare/circl/expander) = %{version}
Provides:       go(github.com/cloudflare/circl/group) = %{version}
Provides:       go(github.com/cloudflare/circl/hpke) = %{version}
Provides:       go(github.com/cloudflare/circl/internal/conv) = %{version}
Provides:       go(github.com/cloudflare/circl/internal/nist) = %{version}
Provides:       go(github.com/cloudflare/circl/internal/sha3) = %{version}
Provides:       go(github.com/cloudflare/circl/internal/test) = %{version}
Provides:       go(github.com/cloudflare/circl/kem) = %{version}
Provides:       go(github.com/cloudflare/circl/kem/frodo) = %{version}
Provides:       go(github.com/cloudflare/circl/kem/frodo/frodo640shake) = %{version}
Provides:       go(github.com/cloudflare/circl/kem/hybrid) = %{version}
Provides:       go(github.com/cloudflare/circl/kem/kyber) = %{version}
Provides:       go(github.com/cloudflare/circl/kem/kyber/kyber1024) = %{version}
Provides:       go(github.com/cloudflare/circl/kem/kyber/kyber512) = %{version}
Provides:       go(github.com/cloudflare/circl/kem/kyber/kyber768) = %{version}
Provides:       go(github.com/cloudflare/circl/kem/mlkem) = %{version}
Provides:       go(github.com/cloudflare/circl/kem/mlkem/mlkem1024) = %{version}
Provides:       go(github.com/cloudflare/circl/kem/mlkem/mlkem512) = %{version}
Provides:       go(github.com/cloudflare/circl/kem/mlkem/mlkem768) = %{version}
Provides:       go(github.com/cloudflare/circl/kem/schemes) = %{version}
Provides:       go(github.com/cloudflare/circl/kem/sike) = %{version}
Provides:       go(github.com/cloudflare/circl/kem/sike/sikep434) = %{version}
Provides:       go(github.com/cloudflare/circl/kem/sike/sikep503) = %{version}
Provides:       go(github.com/cloudflare/circl/kem/sike/sikep751) = %{version}
Provides:       go(github.com/cloudflare/circl/kem/xwing) = %{version}
Provides:       go(github.com/cloudflare/circl/math) = %{version}
Provides:       go(github.com/cloudflare/circl/math/fp25519) = %{version}
Provides:       go(github.com/cloudflare/circl/math/fp448) = %{version}
Provides:       go(github.com/cloudflare/circl/math/mlsbset) = %{version}
Provides:       go(github.com/cloudflare/circl/math/polynomial) = %{version}
Provides:       go(github.com/cloudflare/circl/oprf) = %{version}
Provides:       go(github.com/cloudflare/circl/ot) = %{version}
Provides:       go(github.com/cloudflare/circl/ot/simot) = %{version}
Provides:       go(github.com/cloudflare/circl/pke) = %{version}
Provides:       go(github.com/cloudflare/circl/pke/kyber) = %{version}
Provides:       go(github.com/cloudflare/circl/pke/kyber/internal/common) = %{version}
Provides:       go(github.com/cloudflare/circl/pke/kyber/internal/common/params) = %{version}
Provides:       go(github.com/cloudflare/circl/pke/kyber/kyber1024) = %{version}
Provides:       go(github.com/cloudflare/circl/pke/kyber/kyber1024/internal) = %{version}
Provides:       go(github.com/cloudflare/circl/pke/kyber/kyber512) = %{version}
Provides:       go(github.com/cloudflare/circl/pke/kyber/kyber512/internal) = %{version}
Provides:       go(github.com/cloudflare/circl/pke/kyber/kyber768) = %{version}
Provides:       go(github.com/cloudflare/circl/pke/kyber/kyber768/internal) = %{version}
Provides:       go(github.com/cloudflare/circl/pki) = %{version}
Provides:       go(github.com/cloudflare/circl/secretsharing) = %{version}
Provides:       go(github.com/cloudflare/circl/sign) = %{version}
Provides:       go(github.com/cloudflare/circl/sign/bls) = %{version}
Provides:       go(github.com/cloudflare/circl/sign/dilithium) = %{version}
Provides:       go(github.com/cloudflare/circl/sign/dilithium/mode2) = %{version}
Provides:       go(github.com/cloudflare/circl/sign/dilithium/mode2/internal) = %{version}
Provides:       go(github.com/cloudflare/circl/sign/dilithium/mode3) = %{version}
Provides:       go(github.com/cloudflare/circl/sign/dilithium/mode3/internal) = %{version}
Provides:       go(github.com/cloudflare/circl/sign/dilithium/mode5) = %{version}
Provides:       go(github.com/cloudflare/circl/sign/dilithium/mode5/internal) = %{version}
Provides:       go(github.com/cloudflare/circl/sign/ed25519) = %{version}
Provides:       go(github.com/cloudflare/circl/sign/ed448) = %{version}
Provides:       go(github.com/cloudflare/circl/sign/eddilithium2) = %{version}
Provides:       go(github.com/cloudflare/circl/sign/eddilithium3) = %{version}
Provides:       go(github.com/cloudflare/circl/sign/internal/dilithium) = %{version}
Provides:       go(github.com/cloudflare/circl/sign/internal/dilithium/params) = %{version}
Provides:       go(github.com/cloudflare/circl/sign/mldsa) = %{version}
Provides:       go(github.com/cloudflare/circl/sign/mldsa/mldsa44) = %{version}
Provides:       go(github.com/cloudflare/circl/sign/mldsa/mldsa44/internal) = %{version}
Provides:       go(github.com/cloudflare/circl/sign/mldsa/mldsa65) = %{version}
Provides:       go(github.com/cloudflare/circl/sign/mldsa/mldsa65/internal) = %{version}
Provides:       go(github.com/cloudflare/circl/sign/mldsa/mldsa87) = %{version}
Provides:       go(github.com/cloudflare/circl/sign/mldsa/mldsa87/internal) = %{version}
Provides:       go(github.com/cloudflare/circl/sign/schemes) = %{version}
Provides:       go(github.com/cloudflare/circl/sign/slhdsa) = %{version}
Provides:       go(github.com/cloudflare/circl/simd) = %{version}
Provides:       go(github.com/cloudflare/circl/simd/keccakf1600) = %{version}
Provides:       go(github.com/cloudflare/circl/tss) = %{version}
Provides:       go(github.com/cloudflare/circl/tss/rsa) = %{version}
Provides:       go(github.com/cloudflare/circl/tss/rsa/internal) = %{version}
Provides:       go(github.com/cloudflare/circl/tss/rsa/internal/pss) = %{version}
Provides:       go(github.com/cloudflare/circl/vdaf) = %{version}
Provides:       go(github.com/cloudflare/circl/vdaf/prio3) = %{version}
Provides:       go(github.com/cloudflare/circl/vdaf/prio3/arith) = %{version}
Provides:       go(github.com/cloudflare/circl/vdaf/prio3/arith/fp128) = %{version}
Provides:       go(github.com/cloudflare/circl/vdaf/prio3/arith/fp64) = %{version}
Provides:       go(github.com/cloudflare/circl/vdaf/prio3/count) = %{version}
Provides:       go(github.com/cloudflare/circl/vdaf/prio3/histogram) = %{version}
Provides:       go(github.com/cloudflare/circl/vdaf/prio3/internal/cursor) = %{version}
Provides:       go(github.com/cloudflare/circl/vdaf/prio3/internal/flp) = %{version}
Provides:       go(github.com/cloudflare/circl/vdaf/prio3/internal/flp_test) = %{version}
Provides:       go(github.com/cloudflare/circl/vdaf/prio3/internal/prio3) = %{version}
Provides:       go(github.com/cloudflare/circl/vdaf/prio3/mhcv) = %{version}
Provides:       go(github.com/cloudflare/circl/vdaf/prio3/sum) = %{version}
Provides:       go(github.com/cloudflare/circl/vdaf/prio3/sumvec) = %{version}
Provides:       go(github.com/cloudflare/circl/xof) = %{version}
Provides:       go(github.com/cloudflare/circl/xof/k12) = %{version}
Provides:       go(github.com/cloudflare/circl/zk) = %{version}
Provides:       go(github.com/cloudflare/circl/zk/dl) = %{version}
Provides:       go(github.com/cloudflare/circl/zk/dleq) = %{version}
Provides:       go(github.com/cloudflare/circl/zk/qndleq) = %{version}

Requires:       go(github.com/bwesterb/go-ristretto)
Requires:       go(github.com/mmcloughlin/avo/build)
Requires:       go(github.com/mmcloughlin/avo/operand)
Requires:       go(github.com/mmcloughlin/avo/reg)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/crypto/blake2b)
Requires:       go(golang.org/x/crypto/blake2s)
Requires:       go(golang.org/x/crypto/chacha20poly1305)
Requires:       go(golang.org/x/crypto/cryptobyte)
Requires:       go(golang.org/x/crypto/cryptobyte/asn1)
Requires:       go(golang.org/x/crypto/hkdf)
Requires:       go(golang.org/x/crypto/sha3)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/sys/cpu)


%description
CIRCL

[Image: GitHub release]
(https://img.shields.io/github/release/cloudflare/circl.svg)
(https://GitHub.com/cloudflare/circl/releases/) [Image: CIRCL]
(https://github.com/cloudflare/circl/workflows/CIRCL/badge.svg)
(https://github.com/cloudflare/circl/actions) [Image: GoDoc]
(https://godoc.org/github.com/cloudflare/circl?status.svg)
(https://pkg.go.dev/github.com/cloudflare/circl?tab=overview) [Image: Go
Report Card]
(https://goreportcard.com/badge/github.com/cloudflare/circl)

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
