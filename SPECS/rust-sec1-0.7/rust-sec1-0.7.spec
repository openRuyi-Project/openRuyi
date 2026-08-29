# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sec1
%global full_version 0.7.3
%global pkgname sec1-0.7

Name:           rust-sec1-0.7
Version:        0.7.3
Release:        %autorelease
Summary:        Rust crate "sec1"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/formats/tree/master/sec1
#!RemoteAsset:  sha256:d3e97a565f76233a6003f9f5c54be1d9c5bdfa3eccfb189469f11ec4901c47dc
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "sec1"

%package     -n %{name}+alloc
Summary:        Pure Rust implementation of SEC1: Elliptic Curve Cryptography encoding formats including ASN.1 DER-serialized private keys as well as the Elliptic-Curve-Point-to-Octet-String encoding - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(der-0.7/alloc) >= 0.7.0
Requires:       crate(der-0.7/oid) >= 0.7.0
Requires:       crate(pkcs8-0.10/alloc) >= 0.10.0
Requires:       crate(zeroize-1/alloc) >= 1.0.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust sec1 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Pure Rust implementation of SEC1: Elliptic Curve Cryptography encoding formats including ASN.1 DER-serialized private keys as well as the Elliptic-Curve-Point-to-Octet-String encoding - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/der) = %{version}
Requires:       crate(%{pkgname}/point) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust sec1 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+der
Summary:        Pure Rust implementation of SEC1: Elliptic Curve Cryptography encoding formats including ASN.1 DER-serialized private keys as well as the Elliptic-Curve-Point-to-Octet-String encoding - feature "der"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/zeroize) = %{version}
Requires:       crate(der-0.7/default) >= 0.7.0
Requires:       crate(der-0.7/oid) >= 0.7.0
Provides:       crate(%{pkgname}/der) = %{version}

%description -n %{name}+der
This metapackage enables feature "der" for the Rust sec1 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pem
Summary:        Pure Rust implementation of SEC1: Elliptic Curve Cryptography encoding formats including ASN.1 DER-serialized private keys as well as the Elliptic-Curve-Point-to-Octet-String encoding - feature "pem"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(der-0.7/oid) >= 0.7.0
Requires:       crate(der-0.7/pem) >= 0.7.0
Requires:       crate(pkcs8-0.10/pem) >= 0.10.0
Provides:       crate(%{pkgname}/pem) = %{version}

%description -n %{name}+pem
This metapackage enables feature "pem" for the Rust sec1 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pkcs8
Summary:        Pure Rust implementation of SEC1: Elliptic Curve Cryptography encoding formats including ASN.1 DER-serialized private keys as well as the Elliptic-Curve-Point-to-Octet-String encoding - feature "pkcs8"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pkcs8-0.10) >= 0.10.0
Provides:       crate(%{pkgname}/pkcs8) = %{version}

%description -n %{name}+pkcs8
This metapackage enables feature "pkcs8" for the Rust sec1 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+point
Summary:        Pure Rust implementation of SEC1: Elliptic Curve Cryptography encoding formats including ASN.1 DER-serialized private keys as well as the Elliptic-Curve-Point-to-Octet-String encoding - feature "point"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(base16ct-0.2) >= 0.2.0
Requires:       crate(generic-array-0.14) >= 0.14.7
Provides:       crate(%{pkgname}/point) = %{version}

%description -n %{name}+point
This metapackage enables feature "point" for the Rust sec1 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Pure Rust implementation of SEC1: Elliptic Curve Cryptography encoding formats including ASN.1 DER-serialized private keys as well as the Elliptic-Curve-Point-to-Octet-String encoding - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serdect-0.2/alloc) >= 0.2.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust sec1 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Pure Rust implementation of SEC1: Elliptic Curve Cryptography encoding formats including ASN.1 DER-serialized private keys as well as the Elliptic-Curve-Point-to-Octet-String encoding - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(der-0.7/oid) >= 0.7.0
Requires:       crate(der-0.7/std) >= 0.7.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust sec1 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+subtle
Summary:        Pure Rust implementation of SEC1: Elliptic Curve Cryptography encoding formats including ASN.1 DER-serialized private keys as well as the Elliptic-Curve-Point-to-Octet-String encoding - feature "subtle"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(subtle-2) >= 2.0.0
Provides:       crate(%{pkgname}/subtle) = %{version}

%description -n %{name}+subtle
This metapackage enables feature "subtle" for the Rust sec1 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Pure Rust implementation of SEC1: Elliptic Curve Cryptography encoding formats including ASN.1 DER-serialized private keys as well as the Elliptic-Curve-Point-to-Octet-String encoding - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(der-0.7/oid) >= 0.7.0
Requires:       crate(der-0.7/zeroize) >= 0.7.0
Requires:       crate(zeroize-1) >= 1.0.0
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust sec1 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
