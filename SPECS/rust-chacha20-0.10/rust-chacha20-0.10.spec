# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name chacha20
%global full_version 0.10.0
%global pkgname chacha20-0.10

Name:           rust-chacha20-0.10
Version:        0.10.0
Release:        %autorelease
Summary:        Rust crate "chacha20"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/stream-ciphers
#!RemoteAsset:  sha256:6f8d983286843e49675a4b7a2d174efe136dc93a18d69130dd18198a6c167601
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(cpufeatures-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}) = %{version}

%description
Additionally provides the ChaCha8, ChaCha12, XChaCha20, XChaCha12 and XChaCha8 stream ciphers, and also optional rand_core-compatible RNGs based on those ciphers.
Source code for takopackized Rust crate "chacha20"

%package     -n %{name}+cipher
Summary:        ChaCha20 stream cipher (RFC 8439) implemented in pure Rust using traits from the RustCrypto `cipher` crate, with optional architecture-specific hardware acceleration (AVX2, SSE2) - feature "cipher" and 3 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cipher-0.5/default) >= 0.5.0
Requires:       crate(cipher-0.5/stream-wrapper) >= 0.5.0
Provides:       crate(%{pkgname}/cipher) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/legacy) = %{version}
Provides:       crate(%{pkgname}/xchacha) = %{version}

%description -n %{name}+cipher
Additionally provides the ChaCha8, ChaCha12, XChaCha20, XChaCha12 and XChaCha8 stream ciphers, and also optional rand_core-compatible RNGs based on those ciphers.
This metapackage enables feature "cipher" for the Rust chacha20 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", "legacy", and "xchacha" features.

%package     -n %{name}+rng
Summary:        ChaCha20 stream cipher (RFC 8439) implemented in pure Rust using traits from the RustCrypto `cipher` crate, with optional architecture-specific hardware acceleration (AVX2, SSE2) - feature "rng"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-core-0.10) >= 0.10.0
Provides:       crate(%{pkgname}/rng) = %{version}

%description -n %{name}+rng
Additionally provides the ChaCha8, ChaCha12, XChaCha20, XChaCha12 and XChaCha8 stream ciphers, and also optional rand_core-compatible RNGs based on those ciphers.
This metapackage enables feature "rng" for the Rust chacha20 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        ChaCha20 stream cipher (RFC 8439) implemented in pure Rust using traits from the RustCrypto `cipher` crate, with optional architecture-specific hardware acceleration (AVX2, SSE2) - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zeroize-1) >= 1.8.1
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
Additionally provides the ChaCha8, ChaCha12, XChaCha20, XChaCha12 and XChaCha8 stream ciphers, and also optional rand_core-compatible RNGs based on those ciphers.
This metapackage enables feature "zeroize" for the Rust chacha20 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
