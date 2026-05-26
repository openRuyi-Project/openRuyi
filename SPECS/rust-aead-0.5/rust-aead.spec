# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name aead
%global full_version 0.5.2
%global pkgname aead-0.5

Name:           rust-aead-0.5
Version:        0.5.2
Release:        %autorelease
Summary:        Rust crate "aead"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/traits
#!RemoteAsset:  sha256:d122413f284cf2d62fb1b7db97e02edb8cda96d769b16e443a4f6195e35662b0
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(crypto-common-0.1/default) >= 0.1.7
Requires:       crate(generic-array-0.14) >= 0.14.7
Provides:       crate(aead) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/stream)

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
Summary:        Traits for Authenticated Encryption with Associated Data (AEAD) algorithms, such as AES-GCM as ChaCha20Poly1305, which provide a high-level API - feature "blobby" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(blobby-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/blobby)
Provides:       crate(%{pkgname}/dev)

%description -n %{name}+blobby
This metapackage enables feature "blobby" for the Rust aead crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "dev" feature.

%package     -n %{name}+bytes
Summary:        Traits for Authenticated Encryption with Associated Data (AEAD) algorithms, such as AES-GCM as ChaCha20Poly1305, which provide a high-level API - feature "bytes"
Requires:       crate(%{pkgname})
Requires:       crate(bytes-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/bytes)

%description -n %{name}+bytes
This metapackage enables feature "bytes" for the Rust aead crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+getrandom
Summary:        Traits for Authenticated Encryption with Associated Data (AEAD) algorithms, such as AES-GCM as ChaCha20Poly1305, which provide a high-level API - feature "getrandom"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/rand-core)
Requires:       crate(crypto-common-0.1/getrandom) >= 0.1.7
Provides:       crate(%{pkgname}/getrandom)

%description -n %{name}+getrandom
This metapackage enables feature "getrandom" for the Rust aead crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+heapless
Summary:        Traits for Authenticated Encryption with Associated Data (AEAD) algorithms, such as AES-GCM as ChaCha20Poly1305, which provide a high-level API - feature "heapless"
Requires:       crate(%{pkgname})
Requires:       crate(heapless-0.7) >= 0.7.0
Provides:       crate(%{pkgname}/heapless)

%description -n %{name}+heapless
This metapackage enables feature "heapless" for the Rust aead crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-core
Summary:        Traits for Authenticated Encryption with Associated Data (AEAD) algorithms, such as AES-GCM as ChaCha20Poly1305, which provide a high-level API - feature "rand_core" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(crypto-common-0.1/rand-core) >= 0.1.7
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/rand-core)

%description -n %{name}+rand-core
This metapackage enables feature "rand_core" for the Rust aead crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+std
Summary:        Traits for Authenticated Encryption with Associated Data (AEAD) algorithms, such as AES-GCM as ChaCha20Poly1305, which provide a high-level API - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(crypto-common-0.1/std) >= 0.1.7
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust aead crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
