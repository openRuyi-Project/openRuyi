# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ed25519
%global full_version 2.2.3
%global pkgname ed25519-2

Name:           rust-ed25519-2
Version:        2.2.3
Release:        %autorelease
Summary:        Rust crate "ed25519"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/signatures/tree/master/ed25519
#!RemoteAsset:  sha256:115531babc129696a58c64a4fef0a8bf9e9698629fb97e9e40767d235cfbcd53
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(signature-2) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "ed25519"

%package     -n %{name}+alloc
Summary:        Edwards Digital Signature Algorithm (EdDSA) over Curve25519 (as specified in RFC 8032) support library providing signature type definitions and PKCS#8 private key decoding/encoding support - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pkcs8-0.10/alloc) >= 0.10.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust ed25519 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pem
Summary:        Edwards Digital Signature Algorithm (EdDSA) over Curve25519 (as specified in RFC 8032) support library providing signature type definitions and PKCS#8 private key decoding/encoding support - feature "pem"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(pkcs8-0.10/pem) >= 0.10.0
Provides:       crate(%{pkgname}/pem) = %{version}

%description -n %{name}+pem
This metapackage enables feature "pem" for the Rust ed25519 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pkcs8
Summary:        Edwards Digital Signature Algorithm (EdDSA) over Curve25519 (as specified in RFC 8032) support library providing signature type definitions and PKCS#8 private key decoding/encoding support - feature "pkcs8"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pkcs8-0.10/default) >= 0.10.0
Provides:       crate(%{pkgname}/pkcs8) = %{version}

%description -n %{name}+pkcs8
This metapackage enables feature "pkcs8" for the Rust ed25519 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Edwards Digital Signature Algorithm (EdDSA) over Curve25519 (as specified in RFC 8032) support library providing signature type definitions and PKCS#8 private key decoding/encoding support - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust ed25519 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-bytes
Summary:        Edwards Digital Signature Algorithm (EdDSA) over Curve25519 (as specified in RFC 8032) support library providing signature type definitions and PKCS#8 private key decoding/encoding support - feature "serde_bytes"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(serde-bytes-0.11/default) >= 0.11.0
Provides:       crate(%{pkgname}/serde-bytes) = %{version}

%description -n %{name}+serde-bytes
This metapackage enables feature "serde_bytes" for the Rust ed25519 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Edwards Digital Signature Algorithm (EdDSA) over Curve25519 (as specified in RFC 8032) support library providing signature type definitions and PKCS#8 private key decoding/encoding support - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pkcs8-0.10/std) >= 0.10.0
Requires:       crate(signature-2/std) >= 2.0.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust ed25519 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

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
