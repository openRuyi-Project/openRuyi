# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sequoia-openpgp
%global full_version 2.4.2
%global pkgname sequoia-openpgp-2

Name:           rust-sequoia-openpgp-2
Version:        2.4.2
Release:        %autorelease
Summary:        Rust crate "sequoia-openpgp"
License:        LGPL-2.0-or-later
URL:            https://sequoia-pgp.org/
#!RemoteAsset:  sha256:1460dbd9c736920a78bd450eaa6902304605c493bd2222121849ba01ab8df997
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1/default) >= 1.0.18
Requires:       crate(argon2-0.5/default) >= 0.5.0
Requires:       crate(base64-0.21/default) >= 0.21.0
Requires:       crate(buffered-reader-1) >= 1.3.0
Requires:       crate(chrono-0.4/clock) >= 0.4.10
Requires:       crate(chrono-0.4/std) >= 0.4.10
Requires:       crate(chrono-0.4/wasmbind) >= 0.4.10
Requires:       crate(dyn-clone-1/default) >= 1.0.0
Requires:       crate(getrandom-0.2/default) >= 0.2.0
Requires:       crate(getrandom-0.2/js) >= 0.2.0
Requires:       crate(idna-1/default) >= 1.0.3
Requires:       crate(lalrpop-0.20) >= 0.20.0
Requires:       crate(lalrpop-util-0.20/default) >= 0.20.0
Requires:       crate(libc-0.2/default) >= 0.2.66
Requires:       crate(memsec-0.5) >= 0.5.0
Requires:       crate(regex-1/default) >= 1.0.0
Requires:       crate(regex-syntax-0.8/default) >= 0.8.0
Requires:       crate(sha1collisiondetection-0.3/std) >= 0.3.1
Requires:       crate(thiserror-1/default) >= 1.0.0
Requires:       crate(xxhash-rust-0.8/default) >= 0.8.0
Requires:       crate(xxhash-rust-0.8/xxh3) >= 0.8.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/allow-experimental-crypto) = %{version}
Provides:       crate(%{pkgname}/allow-variable-time-crypto) = %{version}
Provides:       crate(%{pkgname}/crypto-fuzzing) = %{version}
Provides:       crate(%{pkgname}/implicit-crypto-backend-for-tests) = %{version}

%description
Source code for takopackized Rust crate "sequoia-openpgp"

%package     -n %{name}+compression
Summary:        OpenPGP data types and associated machinery - feature "compression"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/compression-bzip2) = %{version}
Requires:       crate(%{pkgname}/compression-deflate) = %{version}
Provides:       crate(%{pkgname}/compression) = %{version}

%description -n %{name}+compression
This metapackage enables feature "compression" for the Rust sequoia-openpgp crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+compression-bzip2
Summary:        OpenPGP data types and associated machinery - feature "compression-bzip2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(buffered-reader-1/compression-bzip2) >= 1.3.0
Requires:       crate(bzip2-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/compression-bzip2) = %{version}

%description -n %{name}+compression-bzip2
This metapackage enables feature "compression-bzip2" for the Rust sequoia-openpgp crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+compression-deflate
Summary:        OpenPGP data types and associated machinery - feature "compression-deflate"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(buffered-reader-1/compression-deflate) >= 1.3.0
Requires:       crate(flate2-1/default) >= 1.0.1
Provides:       crate(%{pkgname}/compression-deflate) = %{version}

%description -n %{name}+compression-deflate
This metapackage enables feature "compression-deflate" for the Rust sequoia-openpgp crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+crypto-botan
Summary:        OpenPGP data types and associated machinery - feature "crypto-botan"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(botan-0.10/botan3) >= 0.10.6
Requires:       crate(botan-0.10/default) >= 0.10.6
Provides:       crate(%{pkgname}/crypto-botan) = %{version}

%description -n %{name}+crypto-botan
This metapackage enables feature "crypto-botan" for the Rust sequoia-openpgp crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+crypto-botan2
Summary:        OpenPGP data types and associated machinery - feature "crypto-botan2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(botan-0.10/default) >= 0.10.6
Provides:       crate(%{pkgname}/crypto-botan2) = %{version}

%description -n %{name}+crypto-botan2
This metapackage enables feature "crypto-botan2" for the Rust sequoia-openpgp crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+crypto-cng
Summary:        OpenPGP data types and associated machinery - feature "crypto-cng"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(aes-gcm-0.10/default) >= 0.10.0
Requires:       crate(aes-gcm-0.10/std) >= 0.10.0
Requires:       crate(cipher-0.4/default) >= 0.4.0
Requires:       crate(cipher-0.4/std) >= 0.4.0
Requires:       crate(cipher-0.4/zeroize) >= 0.4.0
Requires:       crate(cx448-0.1/signing) >= 0.1.1
Requires:       crate(cx448-0.1/zeroize) >= 0.1.1
Requires:       crate(eax-0.5/default) >= 0.5.0
Requires:       crate(ed25519-2/std) >= 2.0.0
Requires:       crate(ed25519-dalek-2/default) >= 2.0.0
Requires:       crate(ed25519-dalek-2/rand-core) >= 2.0.0
Requires:       crate(ed25519-dalek-2/zeroize) >= 2.0.0
Requires:       crate(hkdf-0.12/default) >= 0.12.0
Requires:       crate(num-bigint-dig-0.8) >= 0.8.0
Requires:       crate(num-integer-0.1) >= 0.1.0
Requires:       crate(ocb3-0.1) >= 0.1.0
Requires:       crate(sha2-0.10/default) >= 0.10.0
Requires:       crate(sha2-0.10/oid) >= 0.10.0
Requires:       crate(win-crypto-ng-0.5/block-cipher) >= 0.5.1
Requires:       crate(win-crypto-ng-0.5/default) >= 0.5.1
Requires:       crate(win-crypto-ng-0.5/rand) >= 0.5.1
Requires:       crate(winapi-0.3/bcrypt) >= 0.3.8
Requires:       crate(zeroize-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/crypto-cng) = %{version}

%description -n %{name}+crypto-cng
This metapackage enables feature "crypto-cng" for the Rust sequoia-openpgp crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+crypto-nettle
Summary:        OpenPGP data types and associated machinery - feature "crypto-nettle"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(nettle-7/default) >= 7.3.0
Provides:       crate(%{pkgname}/crypto-nettle) = %{version}

%description -n %{name}+crypto-nettle
This metapackage enables feature "crypto-nettle" for the Rust sequoia-openpgp crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+crypto-openssl
Summary:        OpenPGP data types and associated machinery - feature "crypto-openssl"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ctor-1/default) >= 1.0.0
Requires:       crate(openssl-sys-0.9/default) >= 0.9.0
Requires:       crate(ossl-1/openssl-sys) >= 1.5.3
Requires:       crate(ossl-1/rfc9580) >= 1.5.3
Provides:       crate(%{pkgname}/crypto-openssl) = %{version}

%description -n %{name}+crypto-openssl
This metapackage enables feature "crypto-openssl" for the Rust sequoia-openpgp crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+crypto-rust
Summary:        OpenPGP data types and associated machinery - feature "crypto-rust"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(aes-0.8/default) >= 0.8.0
Requires:       crate(aes-0.8/zeroize) >= 0.8.0
Requires:       crate(aes-gcm-0.10/default) >= 0.10.0
Requires:       crate(aes-gcm-0.10/std) >= 0.10.0
Requires:       crate(block-padding-0.3/default) >= 0.3.0
Requires:       crate(blowfish-0.9/default) >= 0.9.0
Requires:       crate(blowfish-0.9/zeroize) >= 0.9.0
Requires:       crate(camellia-0.1/default) >= 0.1.0
Requires:       crate(camellia-0.1/zeroize) >= 0.1.0
Requires:       crate(cast5-0.11/default) >= 0.11.0
Requires:       crate(cast5-0.11/zeroize) >= 0.11.0
Requires:       crate(cbc-0.1/default) >= 0.1.0
Requires:       crate(cfb-mode-0.8/default) >= 0.8.0
Requires:       crate(cipher-0.4/default) >= 0.4.0
Requires:       crate(cipher-0.4/std) >= 0.4.0
Requires:       crate(cipher-0.4/zeroize) >= 0.4.0
Requires:       crate(cx448-0.1/signing) >= 0.1.1
Requires:       crate(cx448-0.1/zeroize) >= 0.1.1
Requires:       crate(des-0.8/default) >= 0.8.0
Requires:       crate(des-0.8/zeroize) >= 0.8.0
Requires:       crate(digest-0.10/default) >= 0.10.0
Requires:       crate(dsa-0.6/default) >= 0.6.0
Requires:       crate(eax-0.5/default) >= 0.5.0
Requires:       crate(ecb-0.1/default) >= 0.1.0
Requires:       crate(ecdsa-0.16/arithmetic) >= 0.16.0
Requires:       crate(ecdsa-0.16/default) >= 0.16.0
Requires:       crate(ecdsa-0.16/hazmat) >= 0.16.0
Requires:       crate(ed25519-2/std) >= 2.0.0
Requires:       crate(ed25519-dalek-2/default) >= 2.0.0
Requires:       crate(ed25519-dalek-2/rand-core) >= 2.0.0
Requires:       crate(ed25519-dalek-2/zeroize) >= 2.0.0
Requires:       crate(hkdf-0.12/default) >= 0.12.0
Requires:       crate(idea-0.5/default) >= 0.5.0
Requires:       crate(idea-0.5/zeroize) >= 0.5.0
Requires:       crate(md-5-0.10/default) >= 0.10.0
Requires:       crate(md-5-0.10/oid) >= 0.10.0
Requires:       crate(ml-dsa-0.1/zeroize) >= 0.1.1
Requires:       crate(ml-kem-0.3/zeroize) >= 0.3.2
Requires:       crate(num-bigint-dig-0.8) >= 0.8.0
Requires:       crate(num-integer-0.1) >= 0.1.0
Requires:       crate(ocb3-0.1) >= 0.1.0
Requires:       crate(p256-0.13/default) >= 0.13.0
Requires:       crate(p256-0.13/ecdh) >= 0.13.0
Requires:       crate(p256-0.13/ecdsa) >= 0.13.0
Requires:       crate(p384-0.13/default) >= 0.13.0
Requires:       crate(p384-0.13/ecdh) >= 0.13.0
Requires:       crate(p384-0.13/ecdsa) >= 0.13.0
Requires:       crate(p521-0.13/default) >= 0.13.0
Requires:       crate(p521-0.13/ecdh) >= 0.13.0
Requires:       crate(p521-0.13/ecdsa) >= 0.13.0
Requires:       crate(rand-0.10/sys-rng) >= 0.10.0
Requires:       crate(ripemd-0.1/default) >= 0.1.0
Requires:       crate(ripemd-0.1/oid) >= 0.1.0
Requires:       crate(rsa-0.9/default) >= 0.9.0
Requires:       crate(sha1collisiondetection-0.3/digest-trait) >= 0.3.1
Requires:       crate(sha1collisiondetection-0.3/oid) >= 0.3.1
Requires:       crate(sha1collisiondetection-0.3/std) >= 0.3.1
Requires:       crate(sha2-0.10/default) >= 0.10.0
Requires:       crate(sha2-0.10/oid) >= 0.10.0
Requires:       crate(sha3-0.10/default) >= 0.10.0
Requires:       crate(sha3-0.10/oid) >= 0.10.0
Requires:       crate(slh-dsa-0.0.3) >= 0.0.3
Requires:       crate(twofish-0.7/default) >= 0.7.0
Requires:       crate(twofish-0.7/zeroize) >= 0.7.0
Requires:       crate(typenum-1/default) >= 1.12.0
Requires:       crate(x25519-dalek-2/static-secrets) >= 2.0.0
Requires:       crate(x25519-dalek-2/zeroize) >= 2.0.0
Provides:       crate(%{pkgname}/crypto-rust) = %{version}

%description -n %{name}+crypto-rust
This metapackage enables feature "crypto-rust" for the Rust sequoia-openpgp crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        OpenPGP data types and associated machinery - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/compression) = %{version}
Requires:       crate(%{pkgname}/crypto-nettle) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust sequoia-openpgp crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
