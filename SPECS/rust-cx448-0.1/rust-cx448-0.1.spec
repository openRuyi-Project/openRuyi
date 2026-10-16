# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cx448
%global full_version 0.1.1
%global pkgname cx448-0.1

Name:           rust-cx448-0.1
Version:        0.1.1
Release:        %autorelease
Summary:        Rust crate "cx448"
License:        BSD-3-Clause
URL:            https://docs.rs/cx448
#!RemoteAsset:  sha256:b4c0cf476284b03eb6c10e78787b21c7abb7d7d43cb2f02532ba6b831ed892fa
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(crypto-bigint-0.5/generic-array) >= 0.5.5
Requires:       crate(elliptic-curve-0.13/arithmetic) >= 0.13.0
Requires:       crate(elliptic-curve-0.13/bits) >= 0.13.0
Requires:       crate(elliptic-curve-0.13/default) >= 0.13.0
Requires:       crate(elliptic-curve-0.13/hash2curve) >= 0.13.0
Requires:       crate(elliptic-curve-0.13/jwk) >= 0.13.0
Requires:       crate(elliptic-curve-0.13/pem) >= 0.13.0
Requires:       crate(elliptic-curve-0.13/pkcs8) >= 0.13.0
Requires:       crate(elliptic-curve-0.13/sec1) >= 0.13.0
Requires:       crate(rand-core-0.6) >= 0.6.0
Requires:       crate(sha3-0.10) >= 0.10.0
Requires:       crate(subtle-2) >= 2.6.0

Provides:       crate(%{pkgname}) = %{version}

%description
This crate also includes signing and verifying of Ed448 signatures, and x448.
Source code for takopackized Rust crate "cx448"

%package     -n %{name}+alloc
Summary:        Pure-Rust implementation of Ed448 and Curve448 and Decaf - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serdect-0.3/alloc) >= 0.3.0
Requires:       crate(zeroize-1/alloc) >= 1.8.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This crate also includes signing and verifying of Ed448 signatures, and x448.
This metapackage enables feature "alloc" for the Rust cx448 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Pure-Rust implementation of Ed448 and Curve448 and Decaf - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/pkcs8) = %{version}
Requires:       crate(%{pkgname}/signing) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This crate also includes signing and verifying of Ed448 signatures, and x448.
This metapackage enables feature "default" for the Rust cx448 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pkcs8
Summary:        Pure-Rust implementation of Ed448 and Curve448 and Decaf - feature "pkcs8"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pkcs8-0.10/alloc) >= 0.10.0
Requires:       crate(pkcs8-0.10/default) >= 0.10.0
Provides:       crate(%{pkgname}/pkcs8) = %{version}

%description -n %{name}+pkcs8
This crate also includes signing and verifying of Ed448 signatures, and x448.
This metapackage enables feature "pkcs8" for the Rust cx448 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Pure-Rust implementation of Ed448 and Curve448 and Decaf - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serdect-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This crate also includes signing and verifying of Ed448 signatures, and x448.
This metapackage enables feature "serde" for the Rust cx448 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+signing
Summary:        Pure-Rust implementation of Ed448 and Curve448 and Decaf - feature "signing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/zeroize) = %{version}
Requires:       crate(signature-2/digest) >= 2.2.0
Requires:       crate(signature-2/rand-core) >= 2.2.0
Provides:       crate(%{pkgname}/signing) = %{version}

%description -n %{name}+signing
This crate also includes signing and verifying of Ed448 signatures, and x448.
This metapackage enables feature "signing" for the Rust cx448 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Pure-Rust implementation of Ed448 and Curve448 and Decaf - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serdect-0.3/default) >= 0.3.0
Requires:       crate(signature-2/digest) >= 2.2.0
Requires:       crate(signature-2/rand-core) >= 2.2.0
Requires:       crate(signature-2/std) >= 2.2.0
Requires:       crate(zeroize-1/default) >= 1.8.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This crate also includes signing and verifying of Ed448 signatures, and x448.
This metapackage enables feature "std" for the Rust cx448 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Pure-Rust implementation of Ed448 and Curve448 and Decaf - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zeroize-1) >= 1.8.0
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This crate also includes signing and verifying of Ed448 signatures, and x448.
This metapackage enables feature "zeroize" for the Rust cx448 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
