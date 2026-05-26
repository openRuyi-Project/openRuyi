# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name elliptic-curve
%global full_version 0.14.0-rc.28
%global pkgname elliptic-curve-0.14.0-rc.28

Name:           rust-elliptic-curve-0.14.0-rc.28
Version:        0.14.0
Release:        %autorelease
Summary:        Rust crate "elliptic-curve"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/traits
#!RemoteAsset:  sha256:bde7860544606d222fd6bd6d9f9a0773321bf78072a637e1d560a058c0031978
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(base16ct-1.0/default) >= 1.0.0
Requires:       crate(crypto-bigint-0.7.0-rc.28/hybrid-array) >= 0.7.0-rc.28
Requires:       crate(crypto-bigint-0.7.0-rc.28/rand-core) >= 0.7.0-rc.28
Requires:       crate(crypto-bigint-0.7.0-rc.28/subtle) >= 0.7.0-rc.28
Requires:       crate(crypto-bigint-0.7.0-rc.28/zeroize) >= 0.7.0-rc.28
Requires:       crate(crypto-common-0.2/default) >= 0.2.1
Requires:       crate(crypto-common-0.2/rand-core) >= 0.2.1
Requires:       crate(hybrid-array-0.4/zeroize) >= 0.4.11
Requires:       crate(rand-core-0.10) >= 0.10.1
Requires:       crate(subtle-2.0) >= 2.6.1
Requires:       crate(zeroize-1.0) >= 1.8.2
Provides:       crate(elliptic-curve) = %{version}
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "elliptic-curve"

%package     -n %{name}+alloc
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including types and traits for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "alloc"
Requires:       crate(%{pkgname})
Requires:       crate(base16ct-1.0/alloc) >= 1.0.0
Requires:       crate(hybrid-array-0.4/alloc) >= 0.4.11
Requires:       crate(hybrid-array-0.4/zeroize) >= 0.4.11
Requires:       crate(pkcs8-0.11.0-rc.11/alloc) >= 0.11.0-rc.11
Requires:       crate(rustcrypto-ff-0.14.0-rc.1/alloc) >= 0.14.0-rc.1
Requires:       crate(rustcrypto-group-0.14.0-rc.1/alloc) >= 0.14.0-rc.1
Requires:       crate(sec1-0.8/alloc) >= 0.8.1
Requires:       crate(sec1-0.8/ctutils) >= 0.8.1
Requires:       crate(sec1-0.8/subtle) >= 0.8.1
Requires:       crate(sec1-0.8/zeroize) >= 0.8.1
Requires:       crate(zeroize-1.0/alloc) >= 1.8.2
Provides:       crate(%{pkgname}/alloc)

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bits
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including types and traits for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "bits"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/arithmetic)
Requires:       crate(rustcrypto-ff-0.14.0-rc.1/bits) >= 0.14.0-rc.1
Provides:       crate(%{pkgname}/bits)

%description -n %{name}+bits
This metapackage enables feature "bits" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+critical-section
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including types and traits for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "critical-section"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/basepoint-table)
Requires:       crate(once-cell-1.0/critical-section) >= 1.21.4
Provides:       crate(%{pkgname}/critical-section)

%description -n %{name}+critical-section
This metapackage enables feature "critical-section" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dev
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including types and traits for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "dev"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/arithmetic)
Requires:       crate(%{pkgname}/pem)
Requires:       crate(%{pkgname}/pkcs8)
Requires:       crate(hex-literal-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/dev)

%description -n %{name}+dev
This metapackage enables feature "dev" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+digest
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including types and traits for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "digest"
Requires:       crate(%{pkgname})
Requires:       crate(digest-0.11/default) >= 0.11.3
Provides:       crate(%{pkgname}/digest)

%description -n %{name}+digest
This metapackage enables feature "digest" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ecdh
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including types and traits for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "ecdh"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/arithmetic)
Requires:       crate(%{pkgname}/digest)
Requires:       crate(hkdf-0.13) >= 0.13.0
Provides:       crate(%{pkgname}/ecdh)

%description -n %{name}+ecdh
This metapackage enables feature "ecdh" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ff
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including types and traits for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "ff"
Requires:       crate(%{pkgname})
Requires:       crate(rustcrypto-ff-0.14.0-rc.1) >= 0.14.0-rc.1
Provides:       crate(%{pkgname}/ff)

%description -n %{name}+ff
This metapackage enables feature "ff" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+getrandom
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including types and traits for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "getrandom"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/arithmetic)
Requires:       crate(crypto-bigint-0.7.0-rc.28/getrandom) >= 0.7.0-rc.28
Requires:       crate(crypto-bigint-0.7.0-rc.28/hybrid-array) >= 0.7.0-rc.28
Requires:       crate(crypto-bigint-0.7.0-rc.28/rand-core) >= 0.7.0-rc.28
Requires:       crate(crypto-bigint-0.7.0-rc.28/subtle) >= 0.7.0-rc.28
Requires:       crate(crypto-bigint-0.7.0-rc.28/zeroize) >= 0.7.0-rc.28
Requires:       crate(crypto-common-0.2/getrandom) >= 0.2.1
Requires:       crate(crypto-common-0.2/rand-core) >= 0.2.1
Provides:       crate(%{pkgname}/getrandom)

%description -n %{name}+getrandom
This metapackage enables feature "getrandom" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+group
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including types and traits for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "group" and 3 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/ff)
Requires:       crate(rustcrypto-group-0.14.0-rc.1) >= 0.14.0-rc.1
Provides:       crate(%{pkgname}/arithmetic)
Provides:       crate(%{pkgname}/basepoint-table)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/group)

%description -n %{name}+group
This metapackage enables feature "group" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "arithmetic", "basepoint-table", and "default" features.

%package     -n %{name}+once-cell
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including types and traits for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "once_cell"
Requires:       crate(%{pkgname})
Requires:       crate(once-cell-1.0) >= 1.21.4
Provides:       crate(%{pkgname}/once-cell)

%description -n %{name}+once-cell
This metapackage enables feature "once_cell" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pem
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including types and traits for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "pem"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(%{pkgname}/arithmetic)
Requires:       crate(pem-rfc7468-1.0/alloc) >= 1.0.0
Requires:       crate(pem-rfc7468-1.0/default) >= 1.0.0
Requires:       crate(pkcs8-0.11.0-rc.11/pem) >= 0.11.0-rc.11
Requires:       crate(sec1-0.8/ctutils) >= 0.8.1
Requires:       crate(sec1-0.8/pem) >= 0.8.1
Requires:       crate(sec1-0.8/subtle) >= 0.8.1
Requires:       crate(sec1-0.8/zeroize) >= 0.8.1
Provides:       crate(%{pkgname}/pem)

%description -n %{name}+pem
This metapackage enables feature "pem" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pkcs8
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including types and traits for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "pkcs8"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/sec1)
Requires:       crate(pkcs8-0.11.0-rc.11) >= 0.11.0-rc.11
Provides:       crate(%{pkgname}/pkcs8)

%description -n %{name}+pkcs8
This metapackage enables feature "pkcs8" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sec1
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including types and traits for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "sec1"
Requires:       crate(%{pkgname})
Requires:       crate(sec1-0.8/ctutils) >= 0.8.1
Requires:       crate(sec1-0.8/default) >= 0.8.1
Requires:       crate(sec1-0.8/subtle) >= 0.8.1
Requires:       crate(sec1-0.8/zeroize) >= 0.8.1
Provides:       crate(%{pkgname}/sec1)

%description -n %{name}+sec1
This metapackage enables feature "sec1" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including types and traits for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(%{pkgname}/pkcs8)
Requires:       crate(sec1-0.8/ctutils) >= 0.8.1
Requires:       crate(sec1-0.8/serde) >= 0.8.1
Requires:       crate(sec1-0.8/subtle) >= 0.8.1
Requires:       crate(sec1-0.8/zeroize) >= 0.8.1
Requires:       crate(serdect-0.4/alloc) >= 0.4.0
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        General purpose Elliptic Curve Cryptography (ECC) support, including types and traits for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(once-cell-1.0/std) >= 1.21.4
Requires:       crate(pkcs8-0.11.0-rc.11/std) >= 0.11.0-rc.11
Requires:       crate(sec1-0.8/ctutils) >= 0.8.1
Requires:       crate(sec1-0.8/std) >= 0.8.1
Requires:       crate(sec1-0.8/subtle) >= 0.8.1
Requires:       crate(sec1-0.8/zeroize) >= 0.8.1
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust elliptic-curve crate, by pulling in any additional dependencies needed by that feature.

%install -a
if [ -d "%{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{version}" ]; then
    mv "%{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{version}" \
       "%{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}"
fi

%files
%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/

%changelog
%autochangelog
