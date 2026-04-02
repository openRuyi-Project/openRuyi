# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
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
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(base16ct-0.2/default) >= 0.2.0
Requires:       crate(crypto-bigint-0.5/generic-array) >= 0.5.5
Requires:       crate(crypto-bigint-0.5/rand-core) >= 0.5.5
Requires:       crate(crypto-bigint-0.5/zeroize) >= 0.5.5
Requires:       crate(generic-array-0.14/zeroize) >= 0.14.9
Requires:       crate(rand-core-0.6) >= 0.6.4
Requires:       crate(subtle-2.0) >= 2.6.1
Requires:       crate(zeroize-1.0) >= 1.8.2
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/hazmat)

%description
Source code for takopackized Rust crate "elliptic-curve"

%package     -n %{name}+alloc
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including types and traits for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "alloc"
Requires:       crate(%{pkgname})
Requires:       crate(base16ct-0.2/alloc) >= 0.2.0
Requires:       crate(ff-0.13/alloc) >= 0.13.1
Requires:       crate(group-0.13/alloc) >= 0.13.0
Requires:       crate(pkcs8-0.10/alloc) >= 0.10.2
Requires:       crate(sec1-0.7/alloc) >= 0.7.3
Requires:       crate(sec1-0.7/subtle) >= 0.7.3
Requires:       crate(sec1-0.7/zeroize) >= 0.7.3
Requires:       crate(zeroize-1.0/alloc) >= 1.8.2
Provides:       crate(%{pkgname}/alloc)

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bits
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including types and traits for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "bits"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/arithmetic)
Requires:       crate(ff-0.13/bits) >= 0.13.1
Requires:       crate(tap-1.0) >= 1.0.1
Provides:       crate(%{pkgname}/bits)

%description -n %{name}+bits
This metapackage enables feature "bits" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dev
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including types and traits for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "dev"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/arithmetic)
Requires:       crate(%{pkgname}/pem)
Requires:       crate(%{pkgname}/pkcs8)
Requires:       crate(hex-literal-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/dev)

%description -n %{name}+dev
This metapackage enables feature "dev" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+digest
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including types and traits for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "digest" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(digest-0.10/default) >= 0.10.7
Provides:       crate(%{pkgname}/digest)
Provides:       crate(%{pkgname}/voprf)

%description -n %{name}+digest
This metapackage enables feature "digest" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "voprf" feature.

%package     -n %{name}+ecdh
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including types and traits for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "ecdh"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/arithmetic)
Requires:       crate(%{pkgname}/digest)
Requires:       crate(hkdf-0.12) >= 0.12.4
Provides:       crate(%{pkgname}/ecdh)

%description -n %{name}+ecdh
This metapackage enables feature "ecdh" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ff
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including types and traits for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "ff"
Requires:       crate(%{pkgname})
Requires:       crate(ff-0.13) >= 0.13.1
Provides:       crate(%{pkgname}/ff)

%description -n %{name}+ff
This metapackage enables feature "ff" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+group
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including types and traits for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "group" and 2 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/ff)
Requires:       crate(group-0.13) >= 0.13.0
Provides:       crate(%{pkgname}/arithmetic)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/group)

%description -n %{name}+group
This metapackage enables feature "group" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "arithmetic", and "default" features.

%package     -n %{name}+hash2curve
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including types and traits for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "hash2curve"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/arithmetic)
Requires:       crate(%{pkgname}/digest)
Provides:       crate(%{pkgname}/hash2curve)

%description -n %{name}+hash2curve
This metapackage enables feature "hash2curve" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+jwk
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including types and traits for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "jwk"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(%{pkgname}/serde)
Requires:       crate(base64ct-1.0/alloc) >= 1.0.0
Requires:       crate(serde-json-1.0/alloc) >= 1.0.47
Requires:       crate(zeroize-1.0/alloc) >= 1.8.2
Provides:       crate(%{pkgname}/jwk)

%description -n %{name}+jwk
This metapackage enables feature "jwk" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pem
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including types and traits for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "pem"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(%{pkgname}/arithmetic)
Requires:       crate(%{pkgname}/pkcs8)
Requires:       crate(pem-rfc7468-0.7/alloc) >= 0.7.0
Requires:       crate(pem-rfc7468-0.7/default) >= 0.7.0
Requires:       crate(sec1-0.7/pem) >= 0.7.3
Requires:       crate(sec1-0.7/subtle) >= 0.7.3
Requires:       crate(sec1-0.7/zeroize) >= 0.7.3
Provides:       crate(%{pkgname}/pem)

%description -n %{name}+pem
This metapackage enables feature "pem" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pkcs8
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including types and traits for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "pkcs8"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/sec1)
Requires:       crate(pkcs8-0.10) >= 0.10.2
Provides:       crate(%{pkgname}/pkcs8)

%description -n %{name}+pkcs8
This metapackage enables feature "pkcs8" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sec1
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including types and traits for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "sec1"
Requires:       crate(%{pkgname})
Requires:       crate(sec1-0.7/default) >= 0.7.3
Requires:       crate(sec1-0.7/subtle) >= 0.7.3
Requires:       crate(sec1-0.7/zeroize) >= 0.7.3
Provides:       crate(%{pkgname}/sec1)

%description -n %{name}+sec1
This metapackage enables feature "sec1" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including types and traits for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(%{pkgname}/pkcs8)
Requires:       crate(sec1-0.7/serde) >= 0.7.3
Requires:       crate(sec1-0.7/subtle) >= 0.7.3
Requires:       crate(sec1-0.7/zeroize) >= 0.7.3
Requires:       crate(serdect-0.2/alloc) >= 0.2.0
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including types and traits for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(pkcs8-0.10/std) >= 0.10.2
Requires:       crate(rand-core-0.6/std) >= 0.6.4
Requires:       crate(sec1-0.7/std) >= 0.7.3
Requires:       crate(sec1-0.7/subtle) >= 0.7.3
Requires:       crate(sec1-0.7/zeroize) >= 0.7.3
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
