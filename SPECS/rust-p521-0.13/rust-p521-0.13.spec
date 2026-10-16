# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name p521
%global full_version 0.13.3
%global pkgname p521-0.13

Name:           rust-p521-0.13
Version:        0.13.3
Release:        %autorelease
Summary:        Rust crate "p521"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/elliptic-curves/tree/master/p521
#!RemoteAsset:  sha256:0fc9e2161f1f215afdfce23677034ae137bbd45016a880c2eb3ba8eb95f085b2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(base16ct-0.2/default) >= 0.2.0
Requires:       crate(elliptic-curve-0.13/hazmat) >= 0.13.0
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.0

Provides:       crate(%{pkgname}) = %{version}

%description
secp521r1) elliptic curve as defined in SP 800-186
Source code for takopackized Rust crate "p521"

%package     -n %{name}+alloc
Summary:        Pure Rust implementation of the NIST P-521 (a.k.a - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ecdsa-0.16/alloc) >= 0.16.5
Requires:       crate(ecdsa-0.16/der) >= 0.16.5
Requires:       crate(elliptic-curve-0.13/alloc) >= 0.13.0
Requires:       crate(elliptic-curve-0.13/hazmat) >= 0.13.0
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
secp521r1) elliptic curve as defined in SP 800-186
This metapackage enables feature "alloc" for the Rust p521 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+arithmetic
Summary:        Pure Rust implementation of the NIST P-521 (a.k.a - feature "arithmetic"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(primeorder-0.13/default) >= 0.13.3
Provides:       crate(%{pkgname}/arithmetic) = %{version}

%description -n %{name}+arithmetic
secp521r1) elliptic curve as defined in SP 800-186
This metapackage enables feature "arithmetic" for the Rust p521 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Pure Rust implementation of the NIST P-521 (a.k.a - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/arithmetic) = %{version}
Requires:       crate(%{pkgname}/ecdsa) = %{version}
Requires:       crate(%{pkgname}/getrandom) = %{version}
Requires:       crate(%{pkgname}/pem) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
secp521r1) elliptic curve as defined in SP 800-186
This metapackage enables feature "default" for the Rust p521 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+digest
Summary:        Pure Rust implementation of the NIST P-521 (a.k.a - feature "digest"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ecdsa-0.16/der) >= 0.16.5
Requires:       crate(ecdsa-0.16/digest) >= 0.16.5
Requires:       crate(ecdsa-0.16/hazmat) >= 0.16.5
Provides:       crate(%{pkgname}/digest) = %{version}

%description -n %{name}+digest
secp521r1) elliptic curve as defined in SP 800-186
This metapackage enables feature "digest" for the Rust p521 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ecdh
Summary:        Pure Rust implementation of the NIST P-521 (a.k.a - feature "ecdh"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/arithmetic) = %{version}
Requires:       crate(elliptic-curve-0.13/ecdh) >= 0.13.0
Requires:       crate(elliptic-curve-0.13/hazmat) >= 0.13.0
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.0
Provides:       crate(%{pkgname}/ecdh) = %{version}

%description -n %{name}+ecdh
secp521r1) elliptic curve as defined in SP 800-186
This metapackage enables feature "ecdh" for the Rust p521 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ecdsa
Summary:        Pure Rust implementation of the NIST P-521 (a.k.a - feature "ecdsa"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/arithmetic) = %{version}
Requires:       crate(%{pkgname}/sha512) = %{version}
Requires:       crate(ecdsa-0.16/der) >= 0.16.5
Requires:       crate(ecdsa-0.16/signing) >= 0.16.5
Requires:       crate(ecdsa-0.16/verifying) >= 0.16.5
Provides:       crate(%{pkgname}/ecdsa) = %{version}

%description -n %{name}+ecdsa
secp521r1) elliptic curve as defined in SP 800-186
This metapackage enables feature "ecdsa" for the Rust p521 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ecdsa-core
Summary:        Pure Rust implementation of the NIST P-521 (a.k.a - feature "ecdsa-core"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ecdsa-0.16/der) >= 0.16.5
Provides:       crate(%{pkgname}/ecdsa-core) = %{version}

%description -n %{name}+ecdsa-core
secp521r1) elliptic curve as defined in SP 800-186
This metapackage enables feature "ecdsa-core" for the Rust p521 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+getrandom
Summary:        Pure Rust implementation of the NIST P-521 (a.k.a - feature "getrandom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-core-0.6/getrandom) >= 0.6.0
Provides:       crate(%{pkgname}/getrandom) = %{version}

%description -n %{name}+getrandom
secp521r1) elliptic curve as defined in SP 800-186
This metapackage enables feature "getrandom" for the Rust p521 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hash2curve
Summary:        Pure Rust implementation of the NIST P-521 (a.k.a - feature "hash2curve"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/arithmetic) = %{version}
Requires:       crate(elliptic-curve-0.13/hash2curve) >= 0.13.0
Requires:       crate(elliptic-curve-0.13/hazmat) >= 0.13.0
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.0
Provides:       crate(%{pkgname}/hash2curve) = %{version}

%description -n %{name}+hash2curve
secp521r1) elliptic curve as defined in SP 800-186
This metapackage enables feature "hash2curve" for the Rust p521 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+jwk
Summary:        Pure Rust implementation of the NIST P-521 (a.k.a - feature "jwk"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(elliptic-curve-0.13/hazmat) >= 0.13.0
Requires:       crate(elliptic-curve-0.13/jwk) >= 0.13.0
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.0
Provides:       crate(%{pkgname}/jwk) = %{version}

%description -n %{name}+jwk
secp521r1) elliptic curve as defined in SP 800-186
This metapackage enables feature "jwk" for the Rust p521 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pem
Summary:        Pure Rust implementation of the NIST P-521 (a.k.a - feature "pem"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/pkcs8) = %{version}
Requires:       crate(elliptic-curve-0.13/hazmat) >= 0.13.0
Requires:       crate(elliptic-curve-0.13/pem) >= 0.13.0
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.0
Provides:       crate(%{pkgname}/pem) = %{version}

%description -n %{name}+pem
secp521r1) elliptic curve as defined in SP 800-186
This metapackage enables feature "pem" for the Rust p521 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pkcs8
Summary:        Pure Rust implementation of the NIST P-521 (a.k.a - feature "pkcs8"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ecdsa-0.16/der) >= 0.16.5
Requires:       crate(ecdsa-0.16/pkcs8) >= 0.16.5
Requires:       crate(elliptic-curve-0.13/hazmat) >= 0.13.0
Requires:       crate(elliptic-curve-0.13/pkcs8) >= 0.13.0
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.0
Provides:       crate(%{pkgname}/pkcs8) = %{version}

%description -n %{name}+pkcs8
secp521r1) elliptic curve as defined in SP 800-186
This metapackage enables feature "pkcs8" for the Rust p521 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-core
Summary:        Pure Rust implementation of the NIST P-521 (a.k.a - feature "rand_core"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-core-0.6) >= 0.6.0
Provides:       crate(%{pkgname}/rand-core) = %{version}

%description -n %{name}+rand-core
secp521r1) elliptic curve as defined in SP 800-186
This metapackage enables feature "rand_core" for the Rust p521 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Pure Rust implementation of the NIST P-521 (a.k.a - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serdect) = %{version}
Requires:       crate(ecdsa-0.16/der) >= 0.16.5
Requires:       crate(ecdsa-0.16/serde) >= 0.16.5
Requires:       crate(elliptic-curve-0.13/hazmat) >= 0.13.0
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.0
Requires:       crate(elliptic-curve-0.13/serde) >= 0.13.0
Requires:       crate(primeorder-0.13/serde) >= 0.13.3
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
secp521r1) elliptic curve as defined in SP 800-186
This metapackage enables feature "serde" for the Rust p521 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serdect
Summary:        Pure Rust implementation of the NIST P-521 (a.k.a - feature "serdect"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serdect-0.2) >= 0.2.0
Provides:       crate(%{pkgname}/serdect) = %{version}

%description -n %{name}+serdect
secp521r1) elliptic curve as defined in SP 800-186
This metapackage enables feature "serdect" for the Rust p521 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sha512
Summary:        Pure Rust implementation of the NIST P-521 (a.k.a - feature "sha512"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/digest) = %{version}
Requires:       crate(sha2-0.10) >= 0.10.0
Provides:       crate(%{pkgname}/sha512) = %{version}

%description -n %{name}+sha512
secp521r1) elliptic curve as defined in SP 800-186
This metapackage enables feature "sha512" for the Rust p521 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Pure Rust implementation of the NIST P-521 (a.k.a - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(ecdsa-0.16/der) >= 0.16.5
Requires:       crate(ecdsa-0.16/std) >= 0.16.5
Requires:       crate(elliptic-curve-0.13/hazmat) >= 0.13.0
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.0
Requires:       crate(elliptic-curve-0.13/std) >= 0.13.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
secp521r1) elliptic curve as defined in SP 800-186
This metapackage enables feature "std" for the Rust p521 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+test-vectors
Summary:        Pure Rust implementation of the NIST P-521 (a.k.a - feature "test-vectors"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hex-literal-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/test-vectors) = %{version}

%description -n %{name}+test-vectors
secp521r1) elliptic curve as defined in SP 800-186
This metapackage enables feature "test-vectors" for the Rust p521 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+voprf
Summary:        Pure Rust implementation of the NIST P-521 (a.k.a - feature "voprf"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(elliptic-curve-0.13/hazmat) >= 0.13.0
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.0
Requires:       crate(elliptic-curve-0.13/voprf) >= 0.13.0
Requires:       crate(sha2-0.10) >= 0.10.0
Provides:       crate(%{pkgname}/voprf) = %{version}

%description -n %{name}+voprf
secp521r1) elliptic curve as defined in SP 800-186
This metapackage enables feature "voprf" for the Rust p521 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
