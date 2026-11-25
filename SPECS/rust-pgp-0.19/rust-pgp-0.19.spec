# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pgp
%global full_version 0.19.0
%global pkgname pgp-0.19

Name:           rust-pgp-0.19
Version:        0.19.0
Release:        %autorelease
Summary:        Rust crate "pgp"
License:        MIT OR Apache-2.0
URL:            https://github.com/rpgp/rpgp
#!RemoteAsset:  sha256:eaffe1ec22db286599c30ae6be75b37493b558735d86c8e59ec5c38794415fe4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(aead-0.5/bytes) >= 0.5.0
Requires:       crate(aead-0.5/default) >= 0.5.0
Requires:       crate(aes-0.8/default) >= 0.8.4
Requires:       crate(aes-gcm-0.10/default) >= 0.10.3
Requires:       crate(aes-kw-0.2/default) >= 0.2.1
Requires:       crate(aes-kw-0.2/std) >= 0.2.1
Requires:       crate(argon2-0.5/default) >= 0.5.0
Requires:       crate(argon2-0.5/std) >= 0.5.0
Requires:       crate(argon2-0.5/zeroize) >= 0.5.0
Requires:       crate(base64-0.21/default) >= 0.21.7
Requires:       crate(bitfields-1/default) >= 1.0.0
Requires:       crate(block-padding-0.3/default) >= 0.3.0
Requires:       crate(blowfish-0.9/default) >= 0.9.0
Requires:       crate(buffer-redux-1) >= 1.0.0
Requires:       crate(byteorder-1/default) >= 1.4.0
Requires:       crate(bytes-1/default) >= 1.9.0
Requires:       crate(camellia-0.1/default) >= 0.1.0
Requires:       crate(cast5-0.11/default) >= 0.11.0
Requires:       crate(cfb-mode-0.8/default) >= 0.8.2
Requires:       crate(cipher-0.4/default) >= 0.4.2
Requires:       crate(const-oid-0.9/default) >= 0.9.6
Requires:       crate(crc24-0.1/default) >= 0.1.6
Requires:       crate(curve25519-dalek-4/alloc) >= 4.1.3
Requires:       crate(curve25519-dalek-4/precomputed-tables) >= 4.1.3
Requires:       crate(curve25519-dalek-4/zeroize) >= 4.1.3
Requires:       crate(cx448-0.1/default) >= 0.1.1
Requires:       crate(cx448-0.1/zeroize) >= 0.1.1
Requires:       crate(derive-builder-0.20/default) >= 0.20.0
Requires:       crate(derive-more-2/debug) >= 2.0.1
Requires:       crate(derive-more-2/default) >= 2.0.1
Requires:       crate(derive-more-2/display) >= 2.0.1
Requires:       crate(des-0.8/default) >= 0.8.0
Requires:       crate(digest-0.10/default) >= 0.10.7
Requires:       crate(dsa-0.6/default) >= 0.6.3
Requires:       crate(eax-0.5/default) >= 0.5.0
Requires:       crate(ecdsa-0.16/default) >= 0.16.9
Requires:       crate(ed25519-dalek-2/fast) >= 2.1.1
Requires:       crate(ed25519-dalek-2/rand-core) >= 2.1.1
Requires:       crate(ed25519-dalek-2/std) >= 2.1.1
Requires:       crate(ed25519-dalek-2/zeroize) >= 2.1.1
Requires:       crate(elliptic-curve-0.13/default) >= 0.13.0
Requires:       crate(flate2-1/zlib-rs) >= 1.1.1
Requires:       crate(generic-array-0.14/default) >= 0.14.6
Requires:       crate(hex-0.4/default) >= 0.4.0
Requires:       crate(hkdf-0.12/default) >= 0.12.4
Requires:       crate(idea-0.5/default) >= 0.5.0
Requires:       crate(k256-0.13/default) >= 0.13.0
Requires:       crate(k256-0.13/ecdsa) >= 0.13.0
Requires:       crate(log-0.4/default) >= 0.4.22
Requires:       crate(md-5-0.10/default) >= 0.10.5
Requires:       crate(md-5-0.10/oid) >= 0.10.5
Requires:       crate(nom-8/default) >= 8.0.0
Requires:       crate(num-bigint-dig-0.8/default) >= 0.8.6
Requires:       crate(num-bigint-dig-0.8/i128) >= 0.8.6
Requires:       crate(num-bigint-dig-0.8/prime) >= 0.8.6
Requires:       crate(num-bigint-dig-0.8/rand) >= 0.8.6
Requires:       crate(num-bigint-dig-0.8/u64-digit) >= 0.8.6
Requires:       crate(num-bigint-dig-0.8/zeroize) >= 0.8.6
Requires:       crate(num-enum-0.5/default) >= 0.5.7
Requires:       crate(num-traits-0.2/default) >= 0.2.19
Requires:       crate(ocb3-0.1/default) >= 0.1.0
Requires:       crate(p256-0.13/default) >= 0.13.0
Requires:       crate(p256-0.13/ecdh) >= 0.13.0
Requires:       crate(p256-0.13/ecdsa) >= 0.13.0
Requires:       crate(p384-0.13/default) >= 0.13.0
Requires:       crate(p384-0.13/ecdsa) >= 0.13.0
Requires:       crate(p521-0.13/default) >= 0.13.0
Requires:       crate(p521-0.13/ecdh) >= 0.13.0
Requires:       crate(p521-0.13/ecdsa) >= 0.13.0
Requires:       crate(rand-0.8/default) >= 0.8.5
Requires:       crate(regex-1/default) >= 1.7.0
Requires:       crate(replace-with-0.1/default) >= 0.1.8
Requires:       crate(ripemd-0.1/default) >= 0.1.3
Requires:       crate(ripemd-0.1/oid) >= 0.1.3
Requires:       crate(rsa-0.9/default) >= 0.9.10
Requires:       crate(sha1-0.10/default) >= 0.10.6
Requires:       crate(sha1-0.10/oid) >= 0.10.6
Requires:       crate(sha1-checked-0.10/default) >= 0.10.0
Requires:       crate(sha1-checked-0.10/zeroize) >= 0.10.0
Requires:       crate(sha2-0.10/default) >= 0.10.6
Requires:       crate(sha2-0.10/oid) >= 0.10.6
Requires:       crate(sha3-0.10/default) >= 0.10.8
Requires:       crate(sha3-0.10/oid) >= 0.10.8
Requires:       crate(signature-2/default) >= 2.2.0
Requires:       crate(smallvec-1/default) >= 1.10.0
Requires:       crate(snafu-0.8/default) >= 0.8.5
Requires:       crate(snafu-0.8/rust-1-81) >= 0.8.5
Requires:       crate(twofish-0.7/default) >= 0.7.0
Requires:       crate(x25519-dalek-2/alloc) >= 2.0.1
Requires:       crate(x25519-dalek-2/precomputed-tables) >= 2.0.1
Requires:       crate(x25519-dalek-2/static-secrets) >= 2.0.1
Requires:       crate(x25519-dalek-2/zeroize) >= 2.0.1
Requires:       crate(zeroize-1/default) >= 1.8.0
Requires:       crate(zeroize-1/zeroize-derive) >= 1.8.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/draft-wussler-openpgp-forwarding) = %{version}
Provides:       crate(%{pkgname}/large-rsa) = %{version}
Provides:       crate(%{pkgname}/malformed-artifact-compat) = %{version}

%description
Source code for takopackized Rust crate "pgp"

%package     -n %{name}+asm
Summary:        OpenPGP implementation in Rust - feature "asm"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(md-5-0.10/asm) >= 0.10.5
Requires:       crate(md-5-0.10/oid) >= 0.10.5
Requires:       crate(sha1-0.10/asm) >= 0.10.6
Requires:       crate(sha1-0.10/oid) >= 0.10.6
Requires:       crate(sha1-asm-0.5/default) >= 0.5.3
Requires:       crate(sha2-0.10/asm) >= 0.10.6
Requires:       crate(sha2-0.10/oid) >= 0.10.6
Provides:       crate(%{pkgname}/asm) = %{version}

%description -n %{name}+asm
This metapackage enables feature "asm" for the Rust pgp crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bzip2
Summary:        OpenPGP implementation in Rust - feature "bzip2" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bzip2-0.6/default) >= 0.6.0
Provides:       crate(%{pkgname}/bzip2) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+bzip2
This metapackage enables feature "bzip2" for the Rust pgp crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+draft-pqc
Summary:        OpenPGP implementation in Rust - feature "draft-pqc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ml-dsa-0.0.4/default) >= 0.0.4
Requires:       crate(ml-dsa-0.0.4/zeroize) >= 0.0.4
Requires:       crate(ml-kem-0.2/default) >= 0.2.1
Requires:       crate(ml-kem-0.2/deterministic) >= 0.2.1
Requires:       crate(ml-kem-0.2/zeroize) >= 0.2.1
Requires:       crate(slh-dsa-0.0.3/default) >= 0.0.3
Provides:       crate(%{pkgname}/draft-pqc) = %{version}

%description -n %{name}+draft-pqc
This metapackage enables feature "draft-pqc" for the Rust pgp crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+getrandom
Summary:        OpenPGP implementation in Rust - feature "getrandom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(getrandom-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/getrandom) = %{version}

%description -n %{name}+getrandom
This metapackage enables feature "getrandom" for the Rust pgp crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wasm
Summary:        OpenPGP implementation in Rust - feature "wasm"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/getrandom) = %{version}
Requires:       crate(getrandom-0.2/js) >= 0.2.0
Provides:       crate(%{pkgname}/wasm) = %{version}

%description -n %{name}+wasm
This metapackage enables feature "wasm" for the Rust pgp crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
