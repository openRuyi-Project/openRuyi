# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ecdsa
%global full_version 0.16.9
%global pkgname ecdsa-0.16

Name:           rust-ecdsa-0.16
Version:        0.16.9
Release:        %autorelease
Summary:        Rust crate "ecdsa"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/signatures/tree/master/ecdsa
#!RemoteAsset:  sha256:ee27f32b5c5292967d2d4a9d7f1e0b0aed2c15daded5a60300e4abb9d8020bca
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(elliptic-curve-0.13/digest) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.8
Requires:       crate(signature-2.0/rand-core) >= 2.2.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/hazmat)

%description
Source code for takopackized Rust crate "ecdsa"

%package     -n %{name}+alloc
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "alloc"
Requires:       crate(%{pkgname})
Requires:       crate(elliptic-curve-0.13/alloc) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/digest) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.8
Requires:       crate(signature-2.0/alloc) >= 2.2.0
Requires:       crate(signature-2.0/rand-core) >= 2.2.0
Requires:       crate(spki-0.7/alloc) >= 0.7.3
Provides:       crate(%{pkgname}/alloc)

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+arithmetic
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "arithmetic"
Requires:       crate(%{pkgname})
Requires:       crate(elliptic-curve-0.13/arithmetic) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/digest) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.8
Provides:       crate(%{pkgname}/arithmetic)

%description -n %{name}+arithmetic
This metapackage enables feature "arithmetic" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+der
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "der"
Requires:       crate(%{pkgname})
Requires:       crate(der-0.7/default) >= 0.7.10
Provides:       crate(%{pkgname}/der)

%description -n %{name}+der
This metapackage enables feature "der" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dev
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "dev"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/arithmetic)
Requires:       crate(%{pkgname}/digest)
Requires:       crate(%{pkgname}/hazmat)
Requires:       crate(elliptic-curve-0.13/dev) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/digest) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.8
Provides:       crate(%{pkgname}/dev)

%description -n %{name}+dev
This metapackage enables feature "dev" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+digest
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "digest" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(digest-0.10/oid) >= 0.10.7
Requires:       crate(signature-2.0/digest) >= 2.2.0
Requires:       crate(signature-2.0/rand-core) >= 2.2.0
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/digest)

%description -n %{name}+digest
This metapackage enables feature "digest" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+pem
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "pem"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/pkcs8)
Requires:       crate(elliptic-curve-0.13/digest) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/pem) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.8
Provides:       crate(%{pkgname}/pem)

%description -n %{name}+pem
This metapackage enables feature "pem" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pkcs8
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "pkcs8"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/der)
Requires:       crate(%{pkgname}/digest)
Requires:       crate(elliptic-curve-0.13/digest) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/pkcs8) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.8
Provides:       crate(%{pkgname}/pkcs8)

%description -n %{name}+pkcs8
This metapackage enables feature "pkcs8" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rfc6979
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "rfc6979"
Requires:       crate(%{pkgname})
Requires:       crate(rfc6979-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/rfc6979)

%description -n %{name}+rfc6979
This metapackage enables feature "rfc6979" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/serdect)
Requires:       crate(elliptic-curve-0.13/digest) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/serde) >= 0.13.8
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serdect
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "serdect"
Requires:       crate(%{pkgname})
Requires:       crate(serdect-0.2/alloc) >= 0.2.0
Provides:       crate(%{pkgname}/serdect)

%description -n %{name}+serdect
This metapackage enables feature "serdect" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sha2
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "sha2"
Requires:       crate(%{pkgname})
Requires:       crate(sha2-0.10/oid) >= 0.10.0
Provides:       crate(%{pkgname}/sha2)

%description -n %{name}+sha2
This metapackage enables feature "sha2" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+signing
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "signing"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/arithmetic)
Requires:       crate(%{pkgname}/digest)
Requires:       crate(%{pkgname}/hazmat)
Requires:       crate(%{pkgname}/rfc6979)
Provides:       crate(%{pkgname}/signing)

%description -n %{name}+signing
This metapackage enables feature "signing" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+spki
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "spki"
Requires:       crate(%{pkgname})
Requires:       crate(spki-0.7) >= 0.7.3
Provides:       crate(%{pkgname}/spki)

%description -n %{name}+spki
This metapackage enables feature "spki" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(elliptic-curve-0.13/digest) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.8
Requires:       crate(elliptic-curve-0.13/std) >= 0.13.8
Requires:       crate(signature-2.0/rand-core) >= 2.2.0
Requires:       crate(signature-2.0/std) >= 2.2.0
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+verifying
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "verifying"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/arithmetic)
Requires:       crate(%{pkgname}/digest)
Requires:       crate(%{pkgname}/hazmat)
Provides:       crate(%{pkgname}/verifying)

%description -n %{name}+verifying
This metapackage enables feature "verifying" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
