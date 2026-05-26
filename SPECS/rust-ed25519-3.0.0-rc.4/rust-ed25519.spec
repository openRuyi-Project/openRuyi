# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ed25519
%global full_version 3.0.0-rc.4
%global pkgname ed25519-3.0.0-rc.4

Name:           rust-ed25519-3.0.0-rc.4
Version:        3.0.0
Release:        %autorelease
Summary:        Rust crate "ed25519"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/signatures/tree/master/ed25519
#!RemoteAsset:  sha256:c6e914c7c52decb085cea910552e24c63ac019e3ab8bf001ff736da9a9d9d890
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(signature-3.0) >= 3.0.0
Provides:       crate(ed25519) = %{version}
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "ed25519"

%package     -n %{name}+alloc
Summary:        Edwards Digital Signature Algorithm (EdDSA) over Curve25519 (as specified in RFC 8032) support library providing signature type definitions and PKCS#8 private key decoding/encoding support - feature "alloc" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(pkcs8-0.11.0-rc.11/alloc) >= 0.11.0-rc.11
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust ed25519 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+pem
Summary:        Edwards Digital Signature Algorithm (EdDSA) over Curve25519 (as specified in RFC 8032) support library providing signature type definitions and PKCS#8 private key decoding/encoding support - feature "pem"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(pkcs8-0.11.0-rc.11/pem) >= 0.11.0-rc.11
Provides:       crate(%{pkgname}/pem)

%description -n %{name}+pem
This metapackage enables feature "pem" for the Rust ed25519 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pkcs8
Summary:        Edwards Digital Signature Algorithm (EdDSA) over Curve25519 (as specified in RFC 8032) support library providing signature type definitions and PKCS#8 private key decoding/encoding support - feature "pkcs8"
Requires:       crate(%{pkgname})
Requires:       crate(pkcs8-0.11.0-rc.11/default) >= 0.11.0-rc.11
Provides:       crate(%{pkgname}/pkcs8)

%description -n %{name}+pkcs8
This metapackage enables feature "pkcs8" for the Rust ed25519 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Edwards Digital Signature Algorithm (EdDSA) over Curve25519 (as specified in RFC 8032) support library providing signature type definitions and PKCS#8 private key decoding/encoding support - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust ed25519 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-bytes
Summary:        Edwards Digital Signature Algorithm (EdDSA) over Curve25519 (as specified in RFC 8032) support library providing signature type definitions and PKCS#8 private key decoding/encoding support - feature "serde_bytes"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/serde)
Requires:       crate(serde-bytes-0.11) >= 0.11.0
Provides:       crate(%{pkgname}/serde-bytes)

%description -n %{name}+serde-bytes
This metapackage enables feature "serde_bytes" for the Rust ed25519 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zerocopy
Summary:        Edwards Digital Signature Algorithm (EdDSA) over Curve25519 (as specified in RFC 8032) support library providing signature type definitions and PKCS#8 private key decoding/encoding support - feature "zerocopy"
Requires:       crate(%{pkgname})
Requires:       crate(zerocopy-0.8/default) >= 0.8.0
Requires:       crate(zerocopy-0.8/derive) >= 0.8.0
Provides:       crate(%{pkgname}/zerocopy)

%description -n %{name}+zerocopy
This metapackage enables feature "zerocopy" for the Rust ed25519 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Edwards Digital Signature Algorithm (EdDSA) over Curve25519 (as specified in RFC 8032) support library providing signature type definitions and PKCS#8 private key decoding/encoding support - feature "zeroize"
Requires:       crate(%{pkgname})
Requires:       crate(zeroize-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/zeroize)

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust ed25519 crate, by pulling in any additional dependencies needed by that feature.

%install -a
if [ -d "%{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{version}" ]; then
    mv "%{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{version}" \
       "%{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}"
fi

%files
%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/

%changelog
%autochangelog
