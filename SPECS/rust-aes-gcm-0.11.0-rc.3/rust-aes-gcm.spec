# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name aes-gcm
%global full_version 0.11.0-rc.3
%global pkgname aes-gcm-0.11.0-rc.3

Name:           rust-aes-gcm-0.11.0-rc.3
Version:        0.11.0
Release:        %autorelease
Summary:        Rust crate "aes-gcm"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/AEADs
#!RemoteAsset:  sha256:e22c0c90bbe8d4f77c3ca9ddabe41a1f8382d6fc1f7cea89459d0f320371f972
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(aead-0.6.0-rc.10) >= 0.6.0-rc.10
Requires:       crate(cipher-0.5/default) >= 0.5.1
Requires:       crate(ctr-0.10/default) >= 0.10.0
Requires:       crate(ghash-0.6) >= 0.6.0
Requires:       crate(subtle-2.0) >= 2.6.1
Provides:       crate(aes-gcm) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/hazmat)

%description
Source code for takopackized Rust crate "aes-gcm"

%package     -n %{name}+aes
Summary:        Pure Rust implementation of the AES-GCM (Galois/Counter Mode) Authenticated Encryption with Associated Data (AEAD) Cipher with optional architecture-specific hardware acceleration - feature "aes"
Requires:       crate(%{pkgname})
Requires:       crate(aes-0.9/default) >= 0.9.0
Provides:       crate(%{pkgname}/aes)

%description -n %{name}+aes
This metapackage enables feature "aes" for the Rust aes-gcm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+alloc
Summary:        Pure Rust implementation of the AES-GCM (Galois/Counter Mode) Authenticated Encryption with Associated Data (AEAD) Cipher with optional architecture-specific hardware acceleration - feature "alloc"
Requires:       crate(%{pkgname})
Requires:       crate(aead-0.6.0-rc.10/alloc) >= 0.6.0-rc.10
Provides:       crate(%{pkgname}/alloc)

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust aes-gcm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+arrayvec
Summary:        Pure Rust implementation of the AES-GCM (Galois/Counter Mode) Authenticated Encryption with Associated Data (AEAD) Cipher with optional architecture-specific hardware acceleration - feature "arrayvec"
Requires:       crate(%{pkgname})
Requires:       crate(aead-0.6.0-rc.10/arrayvec) >= 0.6.0-rc.10
Provides:       crate(%{pkgname}/arrayvec)

%description -n %{name}+arrayvec
This metapackage enables feature "arrayvec" for the Rust aes-gcm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bytes
Summary:        Pure Rust implementation of the AES-GCM (Galois/Counter Mode) Authenticated Encryption with Associated Data (AEAD) Cipher with optional architecture-specific hardware acceleration - feature "bytes"
Requires:       crate(%{pkgname})
Requires:       crate(aead-0.6.0-rc.10/bytes) >= 0.6.0-rc.10
Provides:       crate(%{pkgname}/bytes)

%description -n %{name}+bytes
This metapackage enables feature "bytes" for the Rust aes-gcm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Pure Rust implementation of the AES-GCM (Galois/Counter Mode) Authenticated Encryption with Associated Data (AEAD) Cipher with optional architecture-specific hardware acceleration - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/aes)
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(%{pkgname}/getrandom)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust aes-gcm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+getrandom
Summary:        Pure Rust implementation of the AES-GCM (Galois/Counter Mode) Authenticated Encryption with Associated Data (AEAD) Cipher with optional architecture-specific hardware acceleration - feature "getrandom"
Requires:       crate(%{pkgname})
Requires:       crate(aead-0.6.0-rc.10/getrandom) >= 0.6.0-rc.10
Provides:       crate(%{pkgname}/getrandom)

%description -n %{name}+getrandom
This metapackage enables feature "getrandom" for the Rust aes-gcm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-core
Summary:        Pure Rust implementation of the AES-GCM (Galois/Counter Mode) Authenticated Encryption with Associated Data (AEAD) Cipher with optional architecture-specific hardware acceleration - feature "rand_core"
Requires:       crate(%{pkgname})
Requires:       crate(aead-0.6.0-rc.10/rand-core) >= 0.6.0-rc.10
Provides:       crate(%{pkgname}/rand-core)

%description -n %{name}+rand-core
This metapackage enables feature "rand_core" for the Rust aes-gcm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Pure Rust implementation of the AES-GCM (Galois/Counter Mode) Authenticated Encryption with Associated Data (AEAD) Cipher with optional architecture-specific hardware acceleration - feature "zeroize"
Requires:       crate(%{pkgname})
Requires:       crate(zeroize-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/zeroize)

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust aes-gcm crate, by pulling in any additional dependencies needed by that feature.

%install -a
if [ -d "%{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{version}" ]; then
    mv "%{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{version}" \
       "%{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}"
fi

%files
%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/

%changelog
%autochangelog
