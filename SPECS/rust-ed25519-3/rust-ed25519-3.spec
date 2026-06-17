# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ed25519
%global full_version 3.0.0
%global pkgname ed25519-3

Name:           rust-ed25519-3
Version:        3.0.0
Release:        %autorelease
Summary:        Rust crate "ed25519"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/signatures/tree/master/ed25519
#!RemoteAsset:  sha256:29fcf32e6c73d1079f83ab4d782de2d81620346a5f38c6237a86a22f8368980a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(signature-3) >= 3.0.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "ed25519"

%package     -n %{name}+alloc
Summary:        Edwards Digital Signature Algorithm (EdDSA) over Curve25519 (as specified in RFC 8032) support library providing signature type definitions and PKCS#8 private key decoding/encoding support - feature "alloc" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pkcs8-0.11/alloc) >= 0.11.0
Requires:       crate(signature-3/alloc) >= 3.0.0
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust ed25519 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+pem
Summary:        Edwards Digital Signature Algorithm (EdDSA) over Curve25519 (as specified in RFC 8032) support library providing signature type definitions and PKCS#8 private key decoding/encoding support - feature "pem"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(pkcs8-0.11/pem) >= 0.11.0
Provides:       crate(%{pkgname}/pem) = %{version}

%description -n %{name}+pem
This metapackage enables feature "pem" for the Rust ed25519 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pkcs8
Summary:        Edwards Digital Signature Algorithm (EdDSA) over Curve25519 (as specified in RFC 8032) support library providing signature type definitions and PKCS#8 private key decoding/encoding support - feature "pkcs8"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pkcs8-0.11/default) >= 0.11.0
Provides:       crate(%{pkgname}/pkcs8) = %{version}

%description -n %{name}+pkcs8
This metapackage enables feature "pkcs8" for the Rust ed25519 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Edwards Digital Signature Algorithm (EdDSA) over Curve25519 (as specified in RFC 8032) support library providing signature type definitions and PKCS#8 private key decoding/encoding support - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serdect-0.4) >= 0.4.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust ed25519 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zerocopy
Summary:        Edwards Digital Signature Algorithm (EdDSA) over Curve25519 (as specified in RFC 8032) support library providing signature type definitions and PKCS#8 private key decoding/encoding support - feature "zerocopy"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zerocopy-0.8/default) >= 0.8.0
Requires:       crate(zerocopy-0.8/derive) >= 0.8.0
Provides:       crate(%{pkgname}/zerocopy) = %{version}

%description -n %{name}+zerocopy
This metapackage enables feature "zerocopy" for the Rust ed25519 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Edwards Digital Signature Algorithm (EdDSA) over Curve25519 (as specified in RFC 8032) support library providing signature type definitions and PKCS#8 private key decoding/encoding support - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zeroize-1) >= 1.0.0
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust ed25519 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
