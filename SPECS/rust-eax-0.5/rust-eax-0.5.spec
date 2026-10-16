# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name eax
%global full_version 0.5.0
%global pkgname eax-0.5

Name:           rust-eax-0.5
Version:        0.5.0
Release:        %autorelease
Summary:        Rust crate "eax"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/AEADs
#!RemoteAsset:  sha256:9954fabd903b82b9d7a68f65f97dc96dd9ad368e40ccc907a7c19d53e6bfac28
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(aead-0.5) >= 0.5.0
Requires:       crate(cipher-0.4/default) >= 0.4.0
Requires:       crate(cmac-0.7/default) >= 0.7.0
Requires:       crate(ctr-0.9/default) >= 0.9.0
Requires:       crate(subtle-2) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}

%description
This scheme is only based on a block cipher. It uses counter mode (CTR) for encryption and CBC mode for generating a OMAC/CMAC/CBCMAC (all names for the same thing).
Source code for takopackized Rust crate "eax"

%package     -n %{name}+alloc
Summary:        Pure Rust implementation of the EAX Authenticated Encryption with Associated Data (AEAD) Cipher with optional architecture-specific hardware acceleration - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(aead-0.5/alloc) >= 0.5.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This scheme is only based on a block cipher. It uses counter mode (CTR) for encryption and CBC mode for generating a OMAC/CMAC/CBCMAC (all names for the same thing).
This metapackage enables feature "alloc" for the Rust eax crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Pure Rust implementation of the EAX Authenticated Encryption with Associated Data (AEAD) Cipher with optional architecture-specific hardware acceleration - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/getrandom) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This scheme is only based on a block cipher. It uses counter mode (CTR) for encryption and CBC mode for generating a OMAC/CMAC/CBCMAC (all names for the same thing).
This metapackage enables feature "default" for the Rust eax crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+getrandom
Summary:        Pure Rust implementation of the EAX Authenticated Encryption with Associated Data (AEAD) Cipher with optional architecture-specific hardware acceleration - feature "getrandom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(aead-0.5/getrandom) >= 0.5.0
Provides:       crate(%{pkgname}/getrandom) = %{version}

%description -n %{name}+getrandom
This scheme is only based on a block cipher. It uses counter mode (CTR) for encryption and CBC mode for generating a OMAC/CMAC/CBCMAC (all names for the same thing).
This metapackage enables feature "getrandom" for the Rust eax crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+heapless
Summary:        Pure Rust implementation of the EAX Authenticated Encryption with Associated Data (AEAD) Cipher with optional architecture-specific hardware acceleration - feature "heapless"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(aead-0.5/heapless) >= 0.5.0
Provides:       crate(%{pkgname}/heapless) = %{version}

%description -n %{name}+heapless
This scheme is only based on a block cipher. It uses counter mode (CTR) for encryption and CBC mode for generating a OMAC/CMAC/CBCMAC (all names for the same thing).
This metapackage enables feature "heapless" for the Rust eax crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Pure Rust implementation of the EAX Authenticated Encryption with Associated Data (AEAD) Cipher with optional architecture-specific hardware acceleration - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(aead-0.5/std) >= 0.5.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This scheme is only based on a block cipher. It uses counter mode (CTR) for encryption and CBC mode for generating a OMAC/CMAC/CBCMAC (all names for the same thing).
This metapackage enables feature "std" for the Rust eax crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+stream
Summary:        Pure Rust implementation of the EAX Authenticated Encryption with Associated Data (AEAD) Cipher with optional architecture-specific hardware acceleration - feature "stream"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(aead-0.5/stream) >= 0.5.0
Provides:       crate(%{pkgname}/stream) = %{version}

%description -n %{name}+stream
This scheme is only based on a block cipher. It uses counter mode (CTR) for encryption and CBC mode for generating a OMAC/CMAC/CBCMAC (all names for the same thing).
This metapackage enables feature "stream" for the Rust eax crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
