# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ecdsa
%global full_version 0.17.0-rc.23
%global pkgname ecdsa-0.17.0-rc.23

Name:           rust-ecdsa-0.17.0-rc.23
Version:        0.17.0
Release:        %autorelease
Summary:        Rust crate "ecdsa"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/signatures/tree/master/ecdsa
#!RemoteAsset:  sha256:dfa0176db12735e38bffeaa3c19ba4470216007496b2088632369bcee6eb5069
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(elliptic-curve-0.14/sec1) >= 0.14.0
Requires:       crate(signature-3/rand-core) >= 3.0.0
Requires:       crate(zeroize-1) >= 1.5.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "ecdsa"

%package     -n %{name}+algorithm
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "algorithm"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/digest) = %{version}
Requires:       crate(elliptic-curve-0.14/arithmetic) >= 0.14.0
Requires:       crate(elliptic-curve-0.14/sec1) >= 0.14.0
Requires:       crate(rfc6979-0.6.0-rc.0/default) >= 0.6.0-rc.0
Provides:       crate(%{pkgname}/algorithm) = %{version}

%description -n %{name}+algorithm
This metapackage enables feature "algorithm" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+alloc
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(elliptic-curve-0.14/alloc) >= 0.14.0
Requires:       crate(elliptic-curve-0.14/sec1) >= 0.14.0
Requires:       crate(signature-3/alloc) >= 3.0.0
Requires:       crate(signature-3/rand-core) >= 3.0.0
Requires:       crate(spki-0.8/alloc) >= 0.8.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+der
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "der"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(der-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/der) = %{version}

%description -n %{name}+der
This metapackage enables feature "der" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dev
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "dev"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/algorithm) = %{version}
Requires:       crate(digest-0.11/dev) >= 0.11.0
Requires:       crate(digest-0.11/oid) >= 0.11.0
Requires:       crate(elliptic-curve-0.14/dev) >= 0.14.0
Requires:       crate(elliptic-curve-0.14/sec1) >= 0.14.0
Provides:       crate(%{pkgname}/dev) = %{version}

%description -n %{name}+dev
This metapackage enables feature "dev" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+digest
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "digest" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(digest-0.11/oid) >= 0.11.0
Requires:       crate(elliptic-curve-0.14/digest) >= 0.14.0
Requires:       crate(elliptic-curve-0.14/sec1) >= 0.14.0
Requires:       crate(signature-3/digest) >= 3.0.0
Requires:       crate(signature-3/rand-core) >= 3.0.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/digest) = %{version}

%description -n %{name}+digest
This metapackage enables feature "digest" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+getrandom
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "getrandom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(elliptic-curve-0.14/getrandom) >= 0.14.0
Requires:       crate(elliptic-curve-0.14/sec1) >= 0.14.0
Provides:       crate(%{pkgname}/getrandom) = %{version}

%description -n %{name}+getrandom
This metapackage enables feature "getrandom" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pem
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "pem"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/pkcs8) = %{version}
Requires:       crate(elliptic-curve-0.14/pem) >= 0.14.0
Requires:       crate(elliptic-curve-0.14/sec1) >= 0.14.0
Provides:       crate(%{pkgname}/pem) = %{version}

%description -n %{name}+pem
This metapackage enables feature "pem" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pkcs8
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "pkcs8"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/der) = %{version}
Requires:       crate(%{pkgname}/digest) = %{version}
Requires:       crate(elliptic-curve-0.14/pkcs8) >= 0.14.0
Requires:       crate(elliptic-curve-0.14/sec1) >= 0.14.0
Provides:       crate(%{pkgname}/pkcs8) = %{version}

%description -n %{name}+pkcs8
This metapackage enables feature "pkcs8" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/pkcs8) = %{version}
Requires:       crate(elliptic-curve-0.14/sec1) >= 0.14.0
Requires:       crate(elliptic-curve-0.14/serde) >= 0.14.0
Requires:       crate(serdect-0.4/alloc) >= 0.4.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sha2
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "sha2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sha2-0.11/oid) >= 0.11.0
Provides:       crate(%{pkgname}/sha2) = %{version}

%description -n %{name}+sha2
This metapackage enables feature "sha2" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+spki
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "spki"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(spki-0.8) >= 0.8.0
Provides:       crate(%{pkgname}/spki) = %{version}

%description -n %{name}+spki
This metapackage enables feature "spki" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(elliptic-curve-0.14/sec1) >= 0.14.0
Requires:       crate(elliptic-curve-0.14/std) >= 0.14.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

# Use the complete Cargo version so the release and RC can coexist.
%install -a
mv "%{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{version}" \
   "%{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/

%changelog
%autochangelog
