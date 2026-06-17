# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
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
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(elliptic-curve-0.13/digest) >= 0.13.6
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.6
Requires:       crate(signature-2/rand-core) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/hazmat) = %{version}

%description
Source code for takopackized Rust crate "ecdsa"

%package     -n %{name}+alloc
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(elliptic-curve-0.13/alloc) >= 0.13.6
Requires:       crate(elliptic-curve-0.13/digest) >= 0.13.6
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.6
Requires:       crate(signature-2/alloc) >= 2.0.0
Requires:       crate(signature-2/rand-core) >= 2.0.0
Requires:       crate(spki-0.7/alloc) >= 0.7.2
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+arithmetic
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "arithmetic"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(elliptic-curve-0.13/arithmetic) >= 0.13.6
Requires:       crate(elliptic-curve-0.13/digest) >= 0.13.6
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.6
Provides:       crate(%{pkgname}/arithmetic) = %{version}

%description -n %{name}+arithmetic
This metapackage enables feature "arithmetic" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+der
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "der"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(der-0.7/default) >= 0.7.0
Provides:       crate(%{pkgname}/der) = %{version}

%description -n %{name}+der
This metapackage enables feature "der" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dev
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "dev"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/arithmetic) = %{version}
Requires:       crate(%{pkgname}/digest) = %{version}
Requires:       crate(%{pkgname}/hazmat) = %{version}
Requires:       crate(elliptic-curve-0.13/dev) >= 0.13.6
Requires:       crate(elliptic-curve-0.13/digest) >= 0.13.6
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.6
Provides:       crate(%{pkgname}/dev) = %{version}

%description -n %{name}+dev
This metapackage enables feature "dev" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+digest
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "digest" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(digest-0.10/oid) >= 0.10.7
Requires:       crate(signature-2/digest) >= 2.0.0
Requires:       crate(signature-2/rand-core) >= 2.0.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/digest) = %{version}

%description -n %{name}+digest
This metapackage enables feature "digest" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+pem
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "pem"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/pkcs8) = %{version}
Requires:       crate(elliptic-curve-0.13/digest) >= 0.13.6
Requires:       crate(elliptic-curve-0.13/pem) >= 0.13.6
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.6
Provides:       crate(%{pkgname}/pem) = %{version}

%description -n %{name}+pem
This metapackage enables feature "pem" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pkcs8
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "pkcs8"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/der) = %{version}
Requires:       crate(%{pkgname}/digest) = %{version}
Requires:       crate(elliptic-curve-0.13/digest) >= 0.13.6
Requires:       crate(elliptic-curve-0.13/pkcs8) >= 0.13.6
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.6
Provides:       crate(%{pkgname}/pkcs8) = %{version}

%description -n %{name}+pkcs8
This metapackage enables feature "pkcs8" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rfc6979
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "rfc6979"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rfc6979-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/rfc6979) = %{version}

%description -n %{name}+rfc6979
This metapackage enables feature "rfc6979" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serdect) = %{version}
Requires:       crate(elliptic-curve-0.13/digest) >= 0.13.6
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.6
Requires:       crate(elliptic-curve-0.13/serde) >= 0.13.6
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serdect
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "serdect"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serdect-0.2/alloc) >= 0.2.0
Provides:       crate(%{pkgname}/serdect) = %{version}

%description -n %{name}+serdect
This metapackage enables feature "serdect" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sha2
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "sha2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sha2-0.10/oid) >= 0.10.0
Provides:       crate(%{pkgname}/sha2) = %{version}

%description -n %{name}+sha2
This metapackage enables feature "sha2" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+signing
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "signing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/arithmetic) = %{version}
Requires:       crate(%{pkgname}/digest) = %{version}
Requires:       crate(%{pkgname}/hazmat) = %{version}
Requires:       crate(%{pkgname}/rfc6979) = %{version}
Provides:       crate(%{pkgname}/signing) = %{version}

%description -n %{name}+signing
This metapackage enables feature "signing" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+spki
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "spki"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(spki-0.7) >= 0.7.2
Provides:       crate(%{pkgname}/spki) = %{version}

%description -n %{name}+spki
This metapackage enables feature "spki" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(elliptic-curve-0.13/digest) >= 0.13.6
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.6
Requires:       crate(elliptic-curve-0.13/std) >= 0.13.6
Requires:       crate(signature-2/rand-core) >= 2.0.0
Requires:       crate(signature-2/std) >= 2.0.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+verifying
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "verifying"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/arithmetic) = %{version}
Requires:       crate(%{pkgname}/digest) = %{version}
Requires:       crate(%{pkgname}/hazmat) = %{version}
Provides:       crate(%{pkgname}/verifying) = %{version}

%description -n %{name}+verifying
This metapackage enables feature "verifying" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
