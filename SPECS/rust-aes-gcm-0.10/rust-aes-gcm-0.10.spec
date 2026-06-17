# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name aes-gcm
%global full_version 0.10.3
%global pkgname aes-gcm-0.10

Name:           rust-aes-gcm-0.10
Version:        0.10.3
Release:        %autorelease
Summary:        Rust crate "aes-gcm"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/AEADs
#!RemoteAsset:  sha256:831010a0f742e1209b3bcea8fab6a8e149051ba6099432c8cb2cc117dec3ead1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(aead-0.5) >= 0.5.0
Requires:       crate(cipher-0.4/default) >= 0.4.0
Requires:       crate(ctr-0.9/default) >= 0.9.0
Requires:       crate(ghash-0.5) >= 0.5.0
Requires:       crate(subtle-2) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "aes-gcm"

%package     -n %{name}+aes
Summary:        Pure Rust implementation of the AES-GCM (Galois/Counter Mode) Authenticated Encryption with Associated Data (AEAD) Cipher with optional architecture-specific hardware acceleration - feature "aes"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(aes-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/aes) = %{version}

%description -n %{name}+aes
This metapackage enables feature "aes" for the Rust aes-gcm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+alloc
Summary:        Pure Rust implementation of the AES-GCM (Galois/Counter Mode) Authenticated Encryption with Associated Data (AEAD) Cipher with optional architecture-specific hardware acceleration - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(aead-0.5/alloc) >= 0.5.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust aes-gcm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+arrayvec
Summary:        Pure Rust implementation of the AES-GCM (Galois/Counter Mode) Authenticated Encryption with Associated Data (AEAD) Cipher with optional architecture-specific hardware acceleration - feature "arrayvec"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(aead-0.5/arrayvec) >= 0.5.0
Provides:       crate(%{pkgname}/arrayvec) = %{version}

%description -n %{name}+arrayvec
This metapackage enables feature "arrayvec" for the Rust aes-gcm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Pure Rust implementation of the AES-GCM (Galois/Counter Mode) Authenticated Encryption with Associated Data (AEAD) Cipher with optional architecture-specific hardware acceleration - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/aes) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/getrandom) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust aes-gcm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+getrandom
Summary:        Pure Rust implementation of the AES-GCM (Galois/Counter Mode) Authenticated Encryption with Associated Data (AEAD) Cipher with optional architecture-specific hardware acceleration - feature "getrandom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rand-core) = %{version}
Requires:       crate(aead-0.5/getrandom) >= 0.5.0
Provides:       crate(%{pkgname}/getrandom) = %{version}

%description -n %{name}+getrandom
This metapackage enables feature "getrandom" for the Rust aes-gcm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+heapless
Summary:        Pure Rust implementation of the AES-GCM (Galois/Counter Mode) Authenticated Encryption with Associated Data (AEAD) Cipher with optional architecture-specific hardware acceleration - feature "heapless"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(aead-0.5/heapless) >= 0.5.0
Provides:       crate(%{pkgname}/heapless) = %{version}

%description -n %{name}+heapless
This metapackage enables feature "heapless" for the Rust aes-gcm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-core
Summary:        Pure Rust implementation of the AES-GCM (Galois/Counter Mode) Authenticated Encryption with Associated Data (AEAD) Cipher with optional architecture-specific hardware acceleration - feature "rand_core"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(aead-0.5/rand-core) >= 0.5.0
Provides:       crate(%{pkgname}/rand-core) = %{version}

%description -n %{name}+rand-core
This metapackage enables feature "rand_core" for the Rust aes-gcm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Pure Rust implementation of the AES-GCM (Galois/Counter Mode) Authenticated Encryption with Associated Data (AEAD) Cipher with optional architecture-specific hardware acceleration - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(aead-0.5/std) >= 0.5.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust aes-gcm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+stream
Summary:        Pure Rust implementation of the AES-GCM (Galois/Counter Mode) Authenticated Encryption with Associated Data (AEAD) Cipher with optional architecture-specific hardware acceleration - feature "stream"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(aead-0.5/stream) >= 0.5.0
Provides:       crate(%{pkgname}/stream) = %{version}

%description -n %{name}+stream
This metapackage enables feature "stream" for the Rust aes-gcm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Pure Rust implementation of the AES-GCM (Galois/Counter Mode) Authenticated Encryption with Associated Data (AEAD) Cipher with optional architecture-specific hardware acceleration - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zeroize-1) >= 1.0.0
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust aes-gcm crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
