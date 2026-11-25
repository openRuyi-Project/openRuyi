# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name p384
%global full_version 0.14.0-rc.15
%global pkgname p384-0.14.0-rc.15

Name:           rust-p384-0.14.0-rc.15
Version:        0.14.0
Release:        %autorelease
Summary:        Rust crate "p384"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/elliptic-curves/tree/master/p384
#!RemoteAsset:  sha256:492f329d7eb11d22dadc988626b9ea1f503b4ab043a8b1e4e2cc4ae45dabdd70
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(elliptic-curve-0.14/sec1) >= 0.14.1
Requires:       crate(fiat-crypto-0.3) >= 0.3.0

Provides:       crate(%{pkgname}) = %{version}

%description
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
Source code for takopackized Rust crate "p384"

%package     -n %{name}+alloc
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ecdsa-0.17.0-rc.23/alloc) >= 0.17.0-rc.23
Requires:       crate(ecdsa-0.17.0-rc.23/der) >= 0.17.0-rc.23
Requires:       crate(elliptic-curve-0.14/alloc) >= 0.14.1
Requires:       crate(elliptic-curve-0.14/sec1) >= 0.14.1
Requires:       crate(primeorder-0.14.0-rc.15/alloc) >= 0.14.0-rc.15
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "alloc" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+arithmetic
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "arithmetic"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(elliptic-curve-0.14/arithmetic) >= 0.14.1
Requires:       crate(elliptic-curve-0.14/digest) >= 0.14.1
Requires:       crate(elliptic-curve-0.14/sec1) >= 0.14.1
Requires:       crate(primefield-0.14/default) >= 0.14.0
Requires:       crate(primeorder-0.14.0-rc.15/default) >= 0.14.0-rc.15
Provides:       crate(%{pkgname}/arithmetic) = %{version}

%description -n %{name}+arithmetic
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "arithmetic" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/arithmetic) = %{version}
Requires:       crate(%{pkgname}/ecdsa) = %{version}
Requires:       crate(%{pkgname}/pem) = %{version}
Requires:       crate(%{pkgname}/precomputed-tables) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "default" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+digest
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "digest"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ecdsa-0.17.0-rc.23/der) >= 0.17.0-rc.23
Requires:       crate(ecdsa-0.17.0-rc.23/digest) >= 0.17.0-rc.23
Provides:       crate(%{pkgname}/digest) = %{version}

%description -n %{name}+digest
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "digest" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ecdh
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "ecdh"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/arithmetic) = %{version}
Requires:       crate(elliptic-curve-0.14/ecdh) >= 0.14.1
Requires:       crate(elliptic-curve-0.14/sec1) >= 0.14.1
Provides:       crate(%{pkgname}/ecdh) = %{version}

%description -n %{name}+ecdh
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "ecdh" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ecdsa
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "ecdsa"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/arithmetic) = %{version}
Requires:       crate(%{pkgname}/sha384) = %{version}
Requires:       crate(ecdsa-0.17.0-rc.23/algorithm) >= 0.17.0-rc.23
Requires:       crate(ecdsa-0.17.0-rc.23/der) >= 0.17.0-rc.23
Provides:       crate(%{pkgname}/ecdsa) = %{version}

%description -n %{name}+ecdsa
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "ecdsa" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ecdsa-core
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "ecdsa-core"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ecdsa-0.17.0-rc.23/der) >= 0.17.0-rc.23
Provides:       crate(%{pkgname}/ecdsa-core) = %{version}

%description -n %{name}+ecdsa-core
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "ecdsa-core" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+getrandom
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "getrandom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ecdsa-0.17.0-rc.23/der) >= 0.17.0-rc.23
Requires:       crate(ecdsa-0.17.0-rc.23/getrandom) >= 0.17.0-rc.23
Requires:       crate(elliptic-curve-0.14/getrandom) >= 0.14.1
Requires:       crate(elliptic-curve-0.14/sec1) >= 0.14.1
Provides:       crate(%{pkgname}/getrandom) = %{version}

%description -n %{name}+getrandom
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "getrandom" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+group-digest
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "group-digest" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/hash2curve) = %{version}
Requires:       crate(%{pkgname}/sha2) = %{version}
Provides:       crate(%{pkgname}/group-digest) = %{version}
Provides:       crate(%{pkgname}/oprf) = %{version}

%description -n %{name}+group-digest
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "group-digest" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "oprf" feature.

%package     -n %{name}+hash2curve
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "hash2curve"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/arithmetic) = %{version}
Requires:       crate(hash2curve-0.14/default) >= 0.14.0
Requires:       crate(primeorder-0.14.0-rc.15/hash2curve) >= 0.14.0-rc.15
Provides:       crate(%{pkgname}/hash2curve) = %{version}

%description -n %{name}+hash2curve
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "hash2curve" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hex-literal
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "hex-literal" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hex-literal-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/hex-literal) = %{version}
Provides:       crate(%{pkgname}/test-vectors) = %{version}

%description -n %{name}+hex-literal
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "hex-literal" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "test-vectors" feature.

%package     -n %{name}+pem
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "pem"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/pkcs8) = %{version}
Requires:       crate(ecdsa-0.17.0-rc.23/der) >= 0.17.0-rc.23
Requires:       crate(ecdsa-0.17.0-rc.23/pem) >= 0.17.0-rc.23
Requires:       crate(elliptic-curve-0.14/pem) >= 0.14.1
Requires:       crate(elliptic-curve-0.14/sec1) >= 0.14.1
Provides:       crate(%{pkgname}/pem) = %{version}

%description -n %{name}+pem
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "pem" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pkcs8
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "pkcs8"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ecdsa-0.17.0-rc.23/der) >= 0.17.0-rc.23
Requires:       crate(ecdsa-0.17.0-rc.23/pkcs8) >= 0.17.0-rc.23
Requires:       crate(elliptic-curve-0.14/pkcs8) >= 0.14.1
Requires:       crate(elliptic-curve-0.14/sec1) >= 0.14.1
Provides:       crate(%{pkgname}/pkcs8) = %{version}

%description -n %{name}+pkcs8
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "pkcs8" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+precomputed-tables
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "precomputed-tables"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/arithmetic) = %{version}
Requires:       crate(primeorder-0.14.0-rc.15/basepoint-table) >= 0.14.0-rc.15
Provides:       crate(%{pkgname}/precomputed-tables) = %{version}

%description -n %{name}+precomputed-tables
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "precomputed-tables" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serdect) = %{version}
Requires:       crate(ecdsa-0.17.0-rc.23/der) >= 0.17.0-rc.23
Requires:       crate(ecdsa-0.17.0-rc.23/serde) >= 0.17.0-rc.23
Requires:       crate(elliptic-curve-0.14/sec1) >= 0.14.1
Requires:       crate(elliptic-curve-0.14/serde) >= 0.14.1
Requires:       crate(primeorder-0.14.0-rc.15/serde) >= 0.14.0-rc.15
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "serde" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serdect
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "serdect"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serdect-0.4) >= 0.4.0
Provides:       crate(%{pkgname}/serdect) = %{version}

%description -n %{name}+serdect
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "serdect" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sha2
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "sha2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sha2-0.11) >= 0.11.0
Provides:       crate(%{pkgname}/sha2) = %{version}

%description -n %{name}+sha2
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "sha2" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sha384
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "sha384"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/digest) = %{version}
Requires:       crate(%{pkgname}/sha2) = %{version}
Provides:       crate(%{pkgname}/sha384) = %{version}

%description -n %{name}+sha384
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "sha384" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Pure Rust implementation of the NIST P-384 (a.k.a - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/getrandom) = %{version}
Requires:       crate(ecdsa-0.17.0-rc.23/der) >= 0.17.0-rc.23
Requires:       crate(ecdsa-0.17.0-rc.23/std) >= 0.17.0-rc.23
Requires:       crate(elliptic-curve-0.14/sec1) >= 0.14.1
Requires:       crate(elliptic-curve-0.14/std) >= 0.14.1
Requires:       crate(primeorder-0.14.0-rc.15/std) >= 0.14.0-rc.15
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
secp384r1) elliptic curve as defined in SP 800-186 with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic support.
This metapackage enables feature "std" for the Rust p384 crate, by pulling in any additional dependencies needed by that feature.

# Use the complete Cargo version so the release and RC can coexist.
%install -a
mv "%{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{version}" \
   "%{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/

%changelog
%autochangelog
