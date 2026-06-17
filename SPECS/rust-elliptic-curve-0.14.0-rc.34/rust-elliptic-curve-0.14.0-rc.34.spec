# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name elliptic-curve
%global full_version 0.14.0-rc.34
%global pkgname elliptic-curve-0.14.0-rc.34

Name:           rust-elliptic-curve-0.14.0-rc.34
Version:        0.14.0
Release:        %autorelease
Summary:        Rust crate "elliptic-curve"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/traits
#!RemoteAsset:  sha256:88a44d097c9f3e494ddc19f77af5aab89f0b3b2652cde370ec8c6064faca5bd2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(base16ct-1/default) >= 1.0.0
Requires:       crate(crypto-bigint-0.7/hybrid-array) >= 0.7.0
Requires:       crate(crypto-bigint-0.7/rand-core) >= 0.7.0
Requires:       crate(crypto-bigint-0.7/subtle) >= 0.7.0
Requires:       crate(crypto-bigint-0.7/zeroize) >= 0.7.0
Requires:       crate(crypto-common-0.2/default) >= 0.2.0
Requires:       crate(crypto-common-0.2/rand-core) >= 0.2.0
Requires:       crate(hybrid-array-0.4/zeroize) >= 0.4.0
Requires:       crate(rand-core-0.10) >= 0.10.0
Requires:       crate(subtle-2) >= 2.6.0
Requires:       crate(zeroize-1) >= 1.7.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "elliptic-curve"

%package     -n %{name}+alloc
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including traits and generic types for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(base16ct-1/alloc) >= 1.0.0
Requires:       crate(ff-0.14/alloc) >= 0.14.0
Requires:       crate(hybrid-array-0.4/alloc) >= 0.4.0
Requires:       crate(hybrid-array-0.4/zeroize) >= 0.4.0
Requires:       crate(pkcs8-0.11/alloc) >= 0.11.0
Requires:       crate(sec1-0.8/alloc) >= 0.8.0
Requires:       crate(sec1-0.8/ctutils) >= 0.8.0
Requires:       crate(sec1-0.8/subtle) >= 0.8.0
Requires:       crate(sec1-0.8/zeroize) >= 0.8.0
Requires:       crate(zeroize-1/alloc) >= 1.7.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+critical-section
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including traits and generic types for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "critical-section"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/basepoint-table) = %{version}
Requires:       crate(once-cell-1/critical-section) >= 1.21.0
Provides:       crate(%{pkgname}/critical-section) = %{version}

%description -n %{name}+critical-section
This metapackage enables feature "critical-section" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dev
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including traits and generic types for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "dev"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/arithmetic) = %{version}
Requires:       crate(%{pkgname}/pem) = %{version}
Requires:       crate(%{pkgname}/pkcs8) = %{version}
Requires:       crate(hex-literal-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/dev) = %{version}

%description -n %{name}+dev
This metapackage enables feature "dev" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+digest
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including traits and generic types for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "digest"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(digest-0.11/default) >= 0.11.0
Provides:       crate(%{pkgname}/digest) = %{version}

%description -n %{name}+digest
This metapackage enables feature "digest" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ecdh
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including traits and generic types for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "ecdh"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/arithmetic) = %{version}
Requires:       crate(%{pkgname}/digest) = %{version}
Requires:       crate(hkdf-0.13) >= 0.13.0
Provides:       crate(%{pkgname}/ecdh) = %{version}

%description -n %{name}+ecdh
This metapackage enables feature "ecdh" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ff
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including traits and generic types for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "ff"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ff-0.14) >= 0.14.0
Provides:       crate(%{pkgname}/ff) = %{version}

%description -n %{name}+ff
This metapackage enables feature "ff" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+getrandom
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including traits and generic types for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "getrandom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/arithmetic) = %{version}
Requires:       crate(crypto-bigint-0.7/getrandom) >= 0.7.0
Requires:       crate(crypto-bigint-0.7/hybrid-array) >= 0.7.0
Requires:       crate(crypto-bigint-0.7/rand-core) >= 0.7.0
Requires:       crate(crypto-bigint-0.7/subtle) >= 0.7.0
Requires:       crate(crypto-bigint-0.7/zeroize) >= 0.7.0
Requires:       crate(crypto-common-0.2/getrandom) >= 0.2.0
Requires:       crate(crypto-common-0.2/rand-core) >= 0.2.0
Provides:       crate(%{pkgname}/getrandom) = %{version}

%description -n %{name}+getrandom
This metapackage enables feature "getrandom" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+group
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including traits and generic types for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "group" and 3 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/ff) = %{version}
Requires:       crate(group-0.14) >= 0.14.0
Provides:       crate(%{pkgname}/arithmetic) = %{version}
Provides:       crate(%{pkgname}/basepoint-table) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/group) = %{version}

%description -n %{name}+group
This metapackage enables feature "group" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "arithmetic", "basepoint-table", and "default" features.

%package     -n %{name}+once-cell
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including traits and generic types for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "once_cell"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(once-cell-1) >= 1.21.0
Provides:       crate(%{pkgname}/once-cell) = %{version}

%description -n %{name}+once-cell
This metapackage enables feature "once_cell" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pem
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including traits and generic types for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "pem"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/arithmetic) = %{version}
Requires:       crate(pem-rfc7468-1/alloc) >= 1.0.0
Requires:       crate(pem-rfc7468-1/default) >= 1.0.0
Requires:       crate(pkcs8-0.11/pem) >= 0.11.0
Requires:       crate(sec1-0.8/ctutils) >= 0.8.0
Requires:       crate(sec1-0.8/pem) >= 0.8.0
Requires:       crate(sec1-0.8/subtle) >= 0.8.0
Requires:       crate(sec1-0.8/zeroize) >= 0.8.0
Provides:       crate(%{pkgname}/pem) = %{version}

%description -n %{name}+pem
This metapackage enables feature "pem" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pkcs8
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including traits and generic types for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "pkcs8"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/sec1) = %{version}
Requires:       crate(pkcs8-0.11) >= 0.11.0
Provides:       crate(%{pkgname}/pkcs8) = %{version}

%description -n %{name}+pkcs8
This metapackage enables feature "pkcs8" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sec1
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including traits and generic types for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "sec1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sec1-0.8/ctutils) >= 0.8.0
Requires:       crate(sec1-0.8/default) >= 0.8.0
Requires:       crate(sec1-0.8/subtle) >= 0.8.0
Requires:       crate(sec1-0.8/zeroize) >= 0.8.0
Provides:       crate(%{pkgname}/sec1) = %{version}

%description -n %{name}+sec1
This metapackage enables feature "sec1" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including traits and generic types for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/pkcs8) = %{version}
Requires:       crate(sec1-0.8/ctutils) >= 0.8.0
Requires:       crate(sec1-0.8/serde) >= 0.8.0
Requires:       crate(sec1-0.8/subtle) >= 0.8.0
Requires:       crate(sec1-0.8/zeroize) >= 0.8.0
Requires:       crate(serdect-0.4/alloc) >= 0.4.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including traits and generic types for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(once-cell-1/std) >= 1.21.0
Requires:       crate(pkcs8-0.11/std) >= 0.11.0
Requires:       crate(sec1-0.8/ctutils) >= 0.8.0
Requires:       crate(sec1-0.8/std) >= 0.8.0
Requires:       crate(sec1-0.8/subtle) >= 0.8.0
Requires:       crate(sec1-0.8/zeroize) >= 0.8.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wnaf
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including traits and generic types for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "wnaf"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/arithmetic) = %{version}
Requires:       crate(wnaf-0.14.0-pre.0/default) >= 0.14.0-pre.0
Provides:       crate(%{pkgname}/wnaf) = %{version}

%description -n %{name}+wnaf
This metapackage enables feature "wnaf" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
