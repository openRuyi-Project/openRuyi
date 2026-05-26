# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name aead
%global full_version 0.6.0-rc.10
%global pkgname aead-0.6.0-rc.10

Name:           rust-aead-0.6.0-rc.10
Version:        0.6.0
Release:        %autorelease
Summary:        Rust crate "aead"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/traits
#!RemoteAsset:  sha256:6b657e772794c6b04730ea897b66a058ccd866c16d1967da05eeeecec39043fe
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(crypto-common-0.2/default) >= 0.2.1
Requires:       crate(inout-0.2/default) >= 0.2.2
Provides:       crate(aead) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)

%description
Source code for takopackized Rust crate "aead"

%package     -n %{name}+arrayvec
Summary:        Traits for Authenticated Encryption with Associated Data (AEAD) algorithms, such as AES-GCM as ChaCha20Poly1305, which provide a high-level API - feature "arrayvec"
Requires:       crate(%{pkgname})
Requires:       crate(arrayvec-0.7) >= 0.7.0
Provides:       crate(%{pkgname}/arrayvec)

%description -n %{name}+arrayvec
This metapackage enables feature "arrayvec" for the Rust aead crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+blobby
Summary:        Traits for Authenticated Encryption with Associated Data (AEAD) algorithms, such as AES-GCM as ChaCha20Poly1305, which provide a high-level API - feature "blobby"
Requires:       crate(%{pkgname})
Requires:       crate(blobby-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/blobby)

%description -n %{name}+blobby
This metapackage enables feature "blobby" for the Rust aead crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bytes
Summary:        Traits for Authenticated Encryption with Associated Data (AEAD) algorithms, such as AES-GCM as ChaCha20Poly1305, which provide a high-level API - feature "bytes"
Requires:       crate(%{pkgname})
Requires:       crate(bytes-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/bytes)

%description -n %{name}+bytes
This metapackage enables feature "bytes" for the Rust aead crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dev
Summary:        Traits for Authenticated Encryption with Associated Data (AEAD) algorithms, such as AES-GCM as ChaCha20Poly1305, which provide a high-level API - feature "dev"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(%{pkgname}/blobby)
Provides:       crate(%{pkgname}/dev)

%description -n %{name}+dev
This metapackage enables feature "dev" for the Rust aead crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+getrandom
Summary:        Traits for Authenticated Encryption with Associated Data (AEAD) algorithms, such as AES-GCM as ChaCha20Poly1305, which provide a high-level API - feature "getrandom"
Requires:       crate(%{pkgname})
Requires:       crate(crypto-common-0.2/getrandom) >= 0.2.1
Provides:       crate(%{pkgname}/getrandom)

%description -n %{name}+getrandom
This metapackage enables feature "getrandom" for the Rust aead crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-core
Summary:        Traits for Authenticated Encryption with Associated Data (AEAD) algorithms, such as AES-GCM as ChaCha20Poly1305, which provide a high-level API - feature "rand_core" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(crypto-common-0.2/rand-core) >= 0.2.1
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/rand-core)

%description -n %{name}+rand-core
This metapackage enables feature "rand_core" for the Rust aead crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%install -a
if [ -d "%{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{version}" ]; then
    mv "%{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{version}" \
       "%{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}"
fi

%files
%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/

%changelog
%autochangelog
