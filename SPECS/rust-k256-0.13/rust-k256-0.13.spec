# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name k256
%global full_version 0.13.4
%global pkgname k256-0.13

Name:           rust-k256-0.13
Version:        0.13.4
Release:        %autorelease
Summary:        Rust crate "k256"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/elliptic-curves/tree/master/k256
#!RemoteAsset:  sha256:f6e3919bbaa2945715f0bb6d3934a173d1e9a59ac23767fbaaef277265a7411b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(elliptic-curve-0.13/hazmat) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.8

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "k256"

%package     -n %{name}+alloc
Summary:        Secp256k1 elliptic curve library written in pure Rust with support for ECDSA signing/verification/public-key recovery, Taproot Schnorr signatures (BIP340), Elliptic Curve Diffie-Hellman (ECDH), and general-purpose secp256k1 elliptic curve group operations which can be used to implement arbitrary protocols - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ecdsa-0.16/alloc) >= 0.16.8
Requires:       crate(ecdsa-0.16/der) >= 0.16.8
Requires:       crate(elliptic-curve-0.13/alloc) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/hazmat) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.8
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust k256 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+arithmetic
Summary:        Secp256k1 elliptic curve library written in pure Rust with support for ECDSA signing/verification/public-key recovery, Taproot Schnorr signatures (BIP340), Elliptic Curve Diffie-Hellman (ECDH), and general-purpose secp256k1 elliptic curve group operations which can be used to implement arbitrary protocols - feature "arithmetic" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(elliptic-curve-0.13/arithmetic) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/hazmat) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.8
Provides:       crate(%{pkgname}/arithmetic) = %{version}
Provides:       crate(%{pkgname}/expose-field) = %{version}

%description -n %{name}+arithmetic
This metapackage enables feature "arithmetic" for the Rust k256 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "expose-field" feature.

%package     -n %{name}+bits
Summary:        Secp256k1 elliptic curve library written in pure Rust with support for ECDSA signing/verification/public-key recovery, Taproot Schnorr signatures (BIP340), Elliptic Curve Diffie-Hellman (ECDH), and general-purpose secp256k1 elliptic curve group operations which can be used to implement arbitrary protocols - feature "bits"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/arithmetic) = %{version}
Requires:       crate(elliptic-curve-0.13/bits) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/hazmat) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.8
Provides:       crate(%{pkgname}/bits) = %{version}

%description -n %{name}+bits
This metapackage enables feature "bits" for the Rust k256 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+critical-section
Summary:        Secp256k1 elliptic curve library written in pure Rust with support for ECDSA signing/verification/public-key recovery, Taproot Schnorr signatures (BIP340), Elliptic Curve Diffie-Hellman (ECDH), and general-purpose secp256k1 elliptic curve group operations which can be used to implement arbitrary protocols - feature "critical-section"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/precomputed-tables) = %{version}
Requires:       crate(once-cell-1/critical-section) >= 1.19.0
Provides:       crate(%{pkgname}/critical-section) = %{version}

%description -n %{name}+critical-section
This metapackage enables feature "critical-section" for the Rust k256 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Secp256k1 elliptic curve library written in pure Rust with support for ECDSA signing/verification/public-key recovery, Taproot Schnorr signatures (BIP340), Elliptic Curve Diffie-Hellman (ECDH), and general-purpose secp256k1 elliptic curve group operations which can be used to implement arbitrary protocols - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/arithmetic) = %{version}
Requires:       crate(%{pkgname}/ecdsa) = %{version}
Requires:       crate(%{pkgname}/pkcs8) = %{version}
Requires:       crate(%{pkgname}/precomputed-tables) = %{version}
Requires:       crate(%{pkgname}/schnorr) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust k256 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+digest
Summary:        Secp256k1 elliptic curve library written in pure Rust with support for ECDSA signing/verification/public-key recovery, Taproot Schnorr signatures (BIP340), Elliptic Curve Diffie-Hellman (ECDH), and general-purpose secp256k1 elliptic curve group operations which can be used to implement arbitrary protocols - feature "digest"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ecdsa-0.16/der) >= 0.16.8
Requires:       crate(ecdsa-0.16/digest) >= 0.16.8
Requires:       crate(ecdsa-0.16/hazmat) >= 0.16.8
Provides:       crate(%{pkgname}/digest) = %{version}

%description -n %{name}+digest
This metapackage enables feature "digest" for the Rust k256 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ecdh
Summary:        Secp256k1 elliptic curve library written in pure Rust with support for ECDSA signing/verification/public-key recovery, Taproot Schnorr signatures (BIP340), Elliptic Curve Diffie-Hellman (ECDH), and general-purpose secp256k1 elliptic curve group operations which can be used to implement arbitrary protocols - feature "ecdh"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/arithmetic) = %{version}
Requires:       crate(elliptic-curve-0.13/ecdh) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/hazmat) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.8
Provides:       crate(%{pkgname}/ecdh) = %{version}

%description -n %{name}+ecdh
This metapackage enables feature "ecdh" for the Rust k256 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ecdsa
Summary:        Secp256k1 elliptic curve library written in pure Rust with support for ECDSA signing/verification/public-key recovery, Taproot Schnorr signatures (BIP340), Elliptic Curve Diffie-Hellman (ECDH), and general-purpose secp256k1 elliptic curve group operations which can be used to implement arbitrary protocols - feature "ecdsa"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/arithmetic) = %{version}
Requires:       crate(%{pkgname}/sha256) = %{version}
Requires:       crate(ecdsa-0.16/der) >= 0.16.8
Requires:       crate(ecdsa-0.16/signing) >= 0.16.8
Requires:       crate(ecdsa-0.16/verifying) >= 0.16.8
Provides:       crate(%{pkgname}/ecdsa) = %{version}

%description -n %{name}+ecdsa
This metapackage enables feature "ecdsa" for the Rust k256 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ecdsa-core
Summary:        Secp256k1 elliptic curve library written in pure Rust with support for ECDSA signing/verification/public-key recovery, Taproot Schnorr signatures (BIP340), Elliptic Curve Diffie-Hellman (ECDH), and general-purpose secp256k1 elliptic curve group operations which can be used to implement arbitrary protocols - feature "ecdsa-core"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ecdsa-0.16/der) >= 0.16.8
Provides:       crate(%{pkgname}/ecdsa-core) = %{version}

%description -n %{name}+ecdsa-core
This metapackage enables feature "ecdsa-core" for the Rust k256 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hash2curve
Summary:        Secp256k1 elliptic curve library written in pure Rust with support for ECDSA signing/verification/public-key recovery, Taproot Schnorr signatures (BIP340), Elliptic Curve Diffie-Hellman (ECDH), and general-purpose secp256k1 elliptic curve group operations which can be used to implement arbitrary protocols - feature "hash2curve"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/arithmetic) = %{version}
Requires:       crate(elliptic-curve-0.13/hash2curve) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/hazmat) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.8
Provides:       crate(%{pkgname}/hash2curve) = %{version}

%description -n %{name}+hash2curve
This metapackage enables feature "hash2curve" for the Rust k256 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hex-literal
Summary:        Secp256k1 elliptic curve library written in pure Rust with support for ECDSA signing/verification/public-key recovery, Taproot Schnorr signatures (BIP340), Elliptic Curve Diffie-Hellman (ECDH), and general-purpose secp256k1 elliptic curve group operations which can be used to implement arbitrary protocols - feature "hex-literal" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hex-literal-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/hex-literal) = %{version}
Provides:       crate(%{pkgname}/test-vectors) = %{version}

%description -n %{name}+hex-literal
This metapackage enables feature "hex-literal" for the Rust k256 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "test-vectors" feature.

%package     -n %{name}+jwk
Summary:        Secp256k1 elliptic curve library written in pure Rust with support for ECDSA signing/verification/public-key recovery, Taproot Schnorr signatures (BIP340), Elliptic Curve Diffie-Hellman (ECDH), and general-purpose secp256k1 elliptic curve group operations which can be used to implement arbitrary protocols - feature "jwk"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(elliptic-curve-0.13/hazmat) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/jwk) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.8
Provides:       crate(%{pkgname}/jwk) = %{version}

%description -n %{name}+jwk
This metapackage enables feature "jwk" for the Rust k256 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+once-cell
Summary:        Secp256k1 elliptic curve library written in pure Rust with support for ECDSA signing/verification/public-key recovery, Taproot Schnorr signatures (BIP340), Elliptic Curve Diffie-Hellman (ECDH), and general-purpose secp256k1 elliptic curve group operations which can be used to implement arbitrary protocols - feature "once_cell"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(once-cell-1) >= 1.19.0
Provides:       crate(%{pkgname}/once-cell) = %{version}

%description -n %{name}+once-cell
This metapackage enables feature "once_cell" for the Rust k256 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pem
Summary:        Secp256k1 elliptic curve library written in pure Rust with support for ECDSA signing/verification/public-key recovery, Taproot Schnorr signatures (BIP340), Elliptic Curve Diffie-Hellman (ECDH), and general-purpose secp256k1 elliptic curve group operations which can be used to implement arbitrary protocols - feature "pem"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/pkcs8) = %{version}
Requires:       crate(ecdsa-0.16/der) >= 0.16.8
Requires:       crate(ecdsa-0.16/pem) >= 0.16.8
Requires:       crate(elliptic-curve-0.13/hazmat) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/pem) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.8
Provides:       crate(%{pkgname}/pem) = %{version}

%description -n %{name}+pem
This metapackage enables feature "pem" for the Rust k256 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pkcs8
Summary:        Secp256k1 elliptic curve library written in pure Rust with support for ECDSA signing/verification/public-key recovery, Taproot Schnorr signatures (BIP340), Elliptic Curve Diffie-Hellman (ECDH), and general-purpose secp256k1 elliptic curve group operations which can be used to implement arbitrary protocols - feature "pkcs8"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ecdsa-0.16/der) >= 0.16.8
Requires:       crate(ecdsa-0.16/pkcs8) >= 0.16.8
Requires:       crate(elliptic-curve-0.13/hazmat) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/pkcs8) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.8
Provides:       crate(%{pkgname}/pkcs8) = %{version}

%description -n %{name}+pkcs8
This metapackage enables feature "pkcs8" for the Rust k256 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+precomputed-tables
Summary:        Secp256k1 elliptic curve library written in pure Rust with support for ECDSA signing/verification/public-key recovery, Taproot Schnorr signatures (BIP340), Elliptic Curve Diffie-Hellman (ECDH), and general-purpose secp256k1 elliptic curve group operations which can be used to implement arbitrary protocols - feature "precomputed-tables"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/arithmetic) = %{version}
Requires:       crate(%{pkgname}/once-cell) = %{version}
Provides:       crate(%{pkgname}/precomputed-tables) = %{version}

%description -n %{name}+precomputed-tables
This metapackage enables feature "precomputed-tables" for the Rust k256 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+schnorr
Summary:        Secp256k1 elliptic curve library written in pure Rust with support for ECDSA signing/verification/public-key recovery, Taproot Schnorr signatures (BIP340), Elliptic Curve Diffie-Hellman (ECDH), and general-purpose secp256k1 elliptic curve group operations which can be used to implement arbitrary protocols - feature "schnorr"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/arithmetic) = %{version}
Requires:       crate(%{pkgname}/sha256) = %{version}
Requires:       crate(%{pkgname}/signature) = %{version}
Provides:       crate(%{pkgname}/schnorr) = %{version}

%description -n %{name}+schnorr
This metapackage enables feature "schnorr" for the Rust k256 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Secp256k1 elliptic curve library written in pure Rust with support for ECDSA signing/verification/public-key recovery, Taproot Schnorr signatures (BIP340), Elliptic Curve Diffie-Hellman (ECDH), and general-purpose secp256k1 elliptic curve group operations which can be used to implement arbitrary protocols - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serdect) = %{version}
Requires:       crate(ecdsa-0.16/der) >= 0.16.8
Requires:       crate(ecdsa-0.16/serde) >= 0.16.8
Requires:       crate(elliptic-curve-0.13/hazmat) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/serde) >= 0.13.8
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust k256 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serdect
Summary:        Secp256k1 elliptic curve library written in pure Rust with support for ECDSA signing/verification/public-key recovery, Taproot Schnorr signatures (BIP340), Elliptic Curve Diffie-Hellman (ECDH), and general-purpose secp256k1 elliptic curve group operations which can be used to implement arbitrary protocols - feature "serdect"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serdect-0.2) >= 0.2.0
Provides:       crate(%{pkgname}/serdect) = %{version}

%description -n %{name}+serdect
This metapackage enables feature "serdect" for the Rust k256 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sha2
Summary:        Secp256k1 elliptic curve library written in pure Rust with support for ECDSA signing/verification/public-key recovery, Taproot Schnorr signatures (BIP340), Elliptic Curve Diffie-Hellman (ECDH), and general-purpose secp256k1 elliptic curve group operations which can be used to implement arbitrary protocols - feature "sha2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sha2-0.10) >= 0.10.0
Provides:       crate(%{pkgname}/sha2) = %{version}

%description -n %{name}+sha2
This metapackage enables feature "sha2" for the Rust k256 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sha256
Summary:        Secp256k1 elliptic curve library written in pure Rust with support for ECDSA signing/verification/public-key recovery, Taproot Schnorr signatures (BIP340), Elliptic Curve Diffie-Hellman (ECDH), and general-purpose secp256k1 elliptic curve group operations which can be used to implement arbitrary protocols - feature "sha256"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/digest) = %{version}
Requires:       crate(%{pkgname}/sha2) = %{version}
Provides:       crate(%{pkgname}/sha256) = %{version}

%description -n %{name}+sha256
This metapackage enables feature "sha256" for the Rust k256 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+signature
Summary:        Secp256k1 elliptic curve library written in pure Rust with support for ECDSA signing/verification/public-key recovery, Taproot Schnorr signatures (BIP340), Elliptic Curve Diffie-Hellman (ECDH), and general-purpose secp256k1 elliptic curve group operations which can be used to implement arbitrary protocols - feature "signature"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(signature-2/default) >= 2.0.0
Provides:       crate(%{pkgname}/signature) = %{version}

%description -n %{name}+signature
This metapackage enables feature "signature" for the Rust k256 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Secp256k1 elliptic curve library written in pure Rust with support for ECDSA signing/verification/public-key recovery, Taproot Schnorr signatures (BIP340), Elliptic Curve Diffie-Hellman (ECDH), and general-purpose secp256k1 elliptic curve group operations which can be used to implement arbitrary protocols - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(ecdsa-0.16/der) >= 0.16.8
Requires:       crate(ecdsa-0.16/std) >= 0.16.8
Requires:       crate(elliptic-curve-0.13/hazmat) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/std) >= 0.13.8
Requires:       crate(once-cell-1/std) >= 1.19.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust k256 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
