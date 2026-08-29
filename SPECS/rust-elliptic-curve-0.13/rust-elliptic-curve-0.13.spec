# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name elliptic-curve
%global full_version 0.13.8
%global pkgname elliptic-curve-0.13

Name:           rust-elliptic-curve-0.13
Version:        0.13.8
Release:        %autorelease
Summary:        Rust crate "elliptic-curve"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/traits/tree/master/elliptic-curve
#!RemoteAsset:  sha256:b5e6043086bf7973472e0c7dff2142ea0b680d30e18d9cc40f267efbf222bd47
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(base16ct-0.2/default) >= 0.2.0
Requires:       crate(crypto-bigint-0.5/generic-array) >= 0.5.0
Requires:       crate(crypto-bigint-0.5/rand-core) >= 0.5.0
Requires:       crate(crypto-bigint-0.5/zeroize) >= 0.5.0
Requires:       crate(generic-array-0.14/zeroize) >= 0.14.6
Requires:       crate(rand-core-0.6) >= 0.6.4
Requires:       crate(subtle-2) >= 2.0.0
Requires:       crate(zeroize-1) >= 1.7.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/hazmat) = %{version}

%description
Source code for takopackized Rust crate "elliptic-curve"

%package     -n %{name}+alloc
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including types and traits for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(base16ct-0.2/alloc) >= 0.2.0
Requires:       crate(ff-0.13/alloc) >= 0.13.0
Requires:       crate(group-0.13/alloc) >= 0.13.0
Requires:       crate(pkcs8-0.10/alloc) >= 0.10.2
Requires:       crate(sec1-0.7/alloc) >= 0.7.1
Requires:       crate(sec1-0.7/subtle) >= 0.7.1
Requires:       crate(sec1-0.7/zeroize) >= 0.7.1
Requires:       crate(zeroize-1/alloc) >= 1.7.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bits
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including types and traits for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "bits"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/arithmetic) = %{version}
Requires:       crate(ff-0.13/bits) >= 0.13.0
Requires:       crate(tap-1) >= 1.0.1
Provides:       crate(%{pkgname}/bits) = %{version}

%description -n %{name}+bits
This metapackage enables feature "bits" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dev
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including types and traits for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "dev"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/arithmetic) = %{version}
Requires:       crate(%{pkgname}/pem) = %{version}
Requires:       crate(%{pkgname}/pkcs8) = %{version}
Requires:       crate(hex-literal-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/dev) = %{version}

%description -n %{name}+dev
This metapackage enables feature "dev" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+digest
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including types and traits for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "digest" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(digest-0.10/default) >= 0.10.0
Provides:       crate(%{pkgname}/digest) = %{version}
Provides:       crate(%{pkgname}/voprf) = %{version}

%description -n %{name}+digest
This metapackage enables feature "digest" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "voprf" feature.

%package     -n %{name}+ecdh
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including types and traits for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "ecdh"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/arithmetic) = %{version}
Requires:       crate(%{pkgname}/digest) = %{version}
Requires:       crate(hkdf-0.12) >= 0.12.1
Provides:       crate(%{pkgname}/ecdh) = %{version}

%description -n %{name}+ecdh
This metapackage enables feature "ecdh" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ff
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including types and traits for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "ff"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ff-0.13) >= 0.13.0
Provides:       crate(%{pkgname}/ff) = %{version}

%description -n %{name}+ff
This metapackage enables feature "ff" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+group
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including types and traits for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "group" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/ff) = %{version}
Requires:       crate(group-0.13) >= 0.13.0
Provides:       crate(%{pkgname}/arithmetic) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/group) = %{version}

%description -n %{name}+group
This metapackage enables feature "group" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "arithmetic", and "default" features.

%package     -n %{name}+hash2curve
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including types and traits for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "hash2curve"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/arithmetic) = %{version}
Requires:       crate(%{pkgname}/digest) = %{version}
Provides:       crate(%{pkgname}/hash2curve) = %{version}

%description -n %{name}+hash2curve
This metapackage enables feature "hash2curve" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+jwk
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including types and traits for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "jwk"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(base64ct-1/alloc) >= 1.0.0
Requires:       crate(serde-json-1/alloc) >= 1.0.47
Requires:       crate(zeroize-1/alloc) >= 1.7.0
Provides:       crate(%{pkgname}/jwk) = %{version}

%description -n %{name}+jwk
This metapackage enables feature "jwk" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pem
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including types and traits for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "pem"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/arithmetic) = %{version}
Requires:       crate(%{pkgname}/pkcs8) = %{version}
Requires:       crate(pem-rfc7468-0.7/alloc) >= 0.7.0
Requires:       crate(pem-rfc7468-0.7/default) >= 0.7.0
Requires:       crate(sec1-0.7/pem) >= 0.7.1
Requires:       crate(sec1-0.7/subtle) >= 0.7.1
Requires:       crate(sec1-0.7/zeroize) >= 0.7.1
Provides:       crate(%{pkgname}/pem) = %{version}

%description -n %{name}+pem
This metapackage enables feature "pem" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pkcs8
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including types and traits for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "pkcs8"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/sec1) = %{version}
Requires:       crate(pkcs8-0.10) >= 0.10.2
Provides:       crate(%{pkgname}/pkcs8) = %{version}

%description -n %{name}+pkcs8
This metapackage enables feature "pkcs8" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sec1
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including types and traits for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "sec1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sec1-0.7/default) >= 0.7.1
Requires:       crate(sec1-0.7/subtle) >= 0.7.1
Requires:       crate(sec1-0.7/zeroize) >= 0.7.1
Provides:       crate(%{pkgname}/sec1) = %{version}

%description -n %{name}+sec1
This metapackage enables feature "sec1" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including types and traits for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/pkcs8) = %{version}
Requires:       crate(sec1-0.7/serde) >= 0.7.1
Requires:       crate(sec1-0.7/subtle) >= 0.7.1
Requires:       crate(sec1-0.7/zeroize) >= 0.7.1
Requires:       crate(serdect-0.2/alloc) >= 0.2.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including types and traits for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(pkcs8-0.10/std) >= 0.10.2
Requires:       crate(rand-core-0.6/std) >= 0.6.4
Requires:       crate(sec1-0.7/std) >= 0.7.1
Requires:       crate(sec1-0.7/subtle) >= 0.7.1
Requires:       crate(sec1-0.7/zeroize) >= 0.7.1
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
