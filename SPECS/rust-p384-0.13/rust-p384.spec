# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name p384
%global full_version 0.13.1
%global pkgname p384-0.13

Name:           rust-p384-0.13
Version:        0.13.1
Release:        %autorelease
Summary:        Rust crate "p384"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/elliptic-curves/tree/master/p384
#!RemoteAsset:  sha256:fe42f1670a52a47d448f14b6a5c61dd78fce51856e68edaa38f7ae3a46b8d6b6
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(elliptic-curve-0.13/hazmat) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.8
Requires:       crate(primeorder-0.13/default) >= 0.13.6
Provides:       crate(%{pkgname})

%description
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
Source code for takopackized Rust crate "p384"

%package     -n %{name}+alloc
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "alloc"
Requires:       crate(%{pkgname})
Requires:       crate(ecdsa-0.16/alloc) >= 0.16.9
Requires:       crate(ecdsa-0.16/der) >= 0.16.9
Requires:       crate(elliptic-curve-0.13/alloc) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/hazmat) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.8
Provides:       crate(%{pkgname}/alloc)

%description -n %{name}+alloc
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "alloc" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+arithmetic
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "arithmetic" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(elliptic-curve-0.13/arithmetic) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/digest) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/hazmat) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.8
Provides:       crate(%{pkgname}/arithmetic)
Provides:       crate(%{pkgname}/expose-field)

%description -n %{name}+arithmetic
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "arithmetic" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "expose-field" feature.

%package     -n %{name}+bits
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "bits"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/arithmetic)
Requires:       crate(elliptic-curve-0.13/bits) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/hazmat) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.8
Provides:       crate(%{pkgname}/bits)

%description -n %{name}+bits
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "bits" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/arithmetic)
Requires:       crate(%{pkgname}/ecdh)
Requires:       crate(%{pkgname}/ecdsa)
Requires:       crate(%{pkgname}/pem)
Requires:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "default" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+digest
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "digest"
Requires:       crate(%{pkgname})
Requires:       crate(ecdsa-0.16/der) >= 0.16.9
Requires:       crate(ecdsa-0.16/digest) >= 0.16.9
Requires:       crate(ecdsa-0.16/hazmat) >= 0.16.9
Provides:       crate(%{pkgname}/digest)

%description -n %{name}+digest
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "digest" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ecdh
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "ecdh"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/arithmetic)
Requires:       crate(elliptic-curve-0.13/ecdh) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/hazmat) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.8
Provides:       crate(%{pkgname}/ecdh)

%description -n %{name}+ecdh
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "ecdh" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ecdsa
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "ecdsa"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/arithmetic)
Requires:       crate(%{pkgname}/sha384)
Requires:       crate(ecdsa-0.16/der) >= 0.16.9
Requires:       crate(ecdsa-0.16/signing) >= 0.16.9
Requires:       crate(ecdsa-0.16/verifying) >= 0.16.9
Provides:       crate(%{pkgname}/ecdsa)

%description -n %{name}+ecdsa
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "ecdsa" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ecdsa-core
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "ecdsa-core"
Requires:       crate(%{pkgname})
Requires:       crate(ecdsa-0.16/der) >= 0.16.9
Provides:       crate(%{pkgname}/ecdsa-core)

%description -n %{name}+ecdsa-core
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "ecdsa-core" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hash2curve
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "hash2curve"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/arithmetic)
Requires:       crate(elliptic-curve-0.13/hash2curve) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/hazmat) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.8
Provides:       crate(%{pkgname}/hash2curve)

%description -n %{name}+hash2curve
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "hash2curve" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hex-literal
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "hex-literal" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(hex-literal-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/hex-literal)
Provides:       crate(%{pkgname}/test-vectors)

%description -n %{name}+hex-literal
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "hex-literal" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "test-vectors" feature.

%package     -n %{name}+jwk
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "jwk"
Requires:       crate(%{pkgname})
Requires:       crate(elliptic-curve-0.13/hazmat) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/jwk) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.8
Provides:       crate(%{pkgname}/jwk)

%description -n %{name}+jwk
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "jwk" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pem
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "pem"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/pkcs8)
Requires:       crate(ecdsa-0.16/der) >= 0.16.9
Requires:       crate(ecdsa-0.16/pem) >= 0.16.9
Requires:       crate(elliptic-curve-0.13/hazmat) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/pem) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.8
Provides:       crate(%{pkgname}/pem)

%description -n %{name}+pem
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "pem" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pkcs8
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "pkcs8"
Requires:       crate(%{pkgname})
Requires:       crate(ecdsa-0.16/der) >= 0.16.9
Requires:       crate(ecdsa-0.16/pkcs8) >= 0.16.9
Requires:       crate(elliptic-curve-0.13/hazmat) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/pkcs8) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.8
Provides:       crate(%{pkgname}/pkcs8)

%description -n %{name}+pkcs8
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "pkcs8" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/serdect)
Requires:       crate(ecdsa-0.16/der) >= 0.16.9
Requires:       crate(ecdsa-0.16/serde) >= 0.16.9
Requires:       crate(elliptic-curve-0.13/hazmat) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/serde) >= 0.13.8
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "serde" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serdect
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "serdect"
Requires:       crate(%{pkgname})
Requires:       crate(serdect-0.2) >= 0.2.0
Provides:       crate(%{pkgname}/serdect)

%description -n %{name}+serdect
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "serdect" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sha2
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "sha2"
Requires:       crate(%{pkgname})
Requires:       crate(sha2-0.10) >= 0.10.9
Provides:       crate(%{pkgname}/sha2)

%description -n %{name}+sha2
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "sha2" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sha384
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "sha384"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/digest)
Requires:       crate(%{pkgname}/sha2)
Provides:       crate(%{pkgname}/sha384)

%description -n %{name}+sha384
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "sha384" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(ecdsa-0.16/der) >= 0.16.9
Requires:       crate(ecdsa-0.16/std) >= 0.16.9
Requires:       crate(elliptic-curve-0.13/hazmat) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/std) >= 0.13.8
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "std" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+voprf
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "voprf"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/sha2)
Requires:       crate(elliptic-curve-0.13/hazmat) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/voprf) >= 0.13.8
Provides:       crate(%{pkgname}/voprf)

%description -n %{name}+voprf
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "voprf" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
