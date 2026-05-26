# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ecdsa
%global full_version 0.17.0-rc.16
%global pkgname ecdsa-0.17.0-rc.16

Name:           rust-ecdsa-0.17.0-rc.16
Version:        0.17.0
Release:        %autorelease
Summary:        Rust crate "ecdsa"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/signatures/tree/master/ecdsa
#!RemoteAsset:  sha256:91bbdd377139884fafcad8dc43a760a3e1e681aa26db910257fa6535b70e1829
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(elliptic-curve-0.14.0-rc.28/sec1) >= 0.14.0-rc.28
Requires:       crate(signature-3.0/rand-core) >= 3.0.0
Requires:       crate(zeroize-1.0) >= 1.8.2
Provides:       crate(ecdsa) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/hazmat)

%description
Source code for takopackized Rust crate "ecdsa"

%package     -n %{name}+algorithm
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "algorithm"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/digest)
Requires:       crate(%{pkgname}/hazmat)
Requires:       crate(elliptic-curve-0.14.0-rc.28/arithmetic) >= 0.14.0-rc.28
Requires:       crate(elliptic-curve-0.14.0-rc.28/sec1) >= 0.14.0-rc.28
Requires:       crate(rfc6979-0.5.0-rc.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/algorithm)

%description -n %{name}+algorithm
This metapackage enables feature "algorithm" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+alloc
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "alloc"
Requires:       crate(%{pkgname})
Requires:       crate(elliptic-curve-0.14.0-rc.28/alloc) >= 0.14.0-rc.28
Requires:       crate(elliptic-curve-0.14.0-rc.28/sec1) >= 0.14.0-rc.28
Requires:       crate(signature-3.0/alloc) >= 3.0.0
Requires:       crate(signature-3.0/rand-core) >= 3.0.0
Requires:       crate(spki-0.8.0-rc.4/alloc) >= 0.8.0-rc.4
Provides:       crate(%{pkgname}/alloc)

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+der
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "der"
Requires:       crate(%{pkgname})
Requires:       crate(der-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/der)

%description -n %{name}+der
This metapackage enables feature "der" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dev
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "dev"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/algorithm)
Requires:       crate(digest-0.11/dev) >= 0.11.3
Requires:       crate(digest-0.11/oid) >= 0.11.3
Requires:       crate(elliptic-curve-0.14.0-rc.28/dev) >= 0.14.0-rc.28
Requires:       crate(elliptic-curve-0.14.0-rc.28/sec1) >= 0.14.0-rc.28
Provides:       crate(%{pkgname}/dev)

%description -n %{name}+dev
This metapackage enables feature "dev" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+digest
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "digest" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(digest-0.11/oid) >= 0.11.3
Requires:       crate(elliptic-curve-0.14.0-rc.28/digest) >= 0.14.0-rc.28
Requires:       crate(elliptic-curve-0.14.0-rc.28/sec1) >= 0.14.0-rc.28
Requires:       crate(signature-3.0/digest) >= 3.0.0
Requires:       crate(signature-3.0/rand-core) >= 3.0.0
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/digest)

%description -n %{name}+digest
This metapackage enables feature "digest" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+getrandom
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "getrandom"
Requires:       crate(%{pkgname})
Requires:       crate(elliptic-curve-0.14.0-rc.28/getrandom) >= 0.14.0-rc.28
Requires:       crate(elliptic-curve-0.14.0-rc.28/sec1) >= 0.14.0-rc.28
Provides:       crate(%{pkgname}/getrandom)

%description -n %{name}+getrandom
This metapackage enables feature "getrandom" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pem
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "pem"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/pkcs8)
Requires:       crate(elliptic-curve-0.14.0-rc.28/pem) >= 0.14.0-rc.28
Requires:       crate(elliptic-curve-0.14.0-rc.28/sec1) >= 0.14.0-rc.28
Provides:       crate(%{pkgname}/pem)

%description -n %{name}+pem
This metapackage enables feature "pem" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pkcs8
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "pkcs8"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/der)
Requires:       crate(%{pkgname}/digest)
Requires:       crate(elliptic-curve-0.14.0-rc.28/pkcs8) >= 0.14.0-rc.28
Requires:       crate(elliptic-curve-0.14.0-rc.28/sec1) >= 0.14.0-rc.28
Provides:       crate(%{pkgname}/pkcs8)

%description -n %{name}+pkcs8
This metapackage enables feature "pkcs8" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/pkcs8)
Requires:       crate(elliptic-curve-0.14.0-rc.28/sec1) >= 0.14.0-rc.28
Requires:       crate(elliptic-curve-0.14.0-rc.28/serde) >= 0.14.0-rc.28
Requires:       crate(serdect-0.4/alloc) >= 0.4.0
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sha2
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "sha2"
Requires:       crate(%{pkgname})
Requires:       crate(sha2-0.11.0-rc.5/oid) >= 0.11.0-rc.5
Provides:       crate(%{pkgname}/sha2)

%description -n %{name}+sha2
This metapackage enables feature "sha2" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+spki
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "spki"
Requires:       crate(%{pkgname})
Requires:       crate(spki-0.8.0-rc.4) >= 0.8.0-rc.4
Provides:       crate(%{pkgname}/spki)

%description -n %{name}+spki
This metapackage enables feature "spki" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(elliptic-curve-0.14.0-rc.28/sec1) >= 0.14.0-rc.28
Requires:       crate(elliptic-curve-0.14.0-rc.28/std) >= 0.14.0-rc.28
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust ecdsa crate, by pulling in any additional dependencies needed by that feature.

%install -a
if [ -d "%{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{version}" ]; then
    mv "%{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{version}" \
       "%{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}"
fi

%files
%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/

%changelog
%autochangelog
