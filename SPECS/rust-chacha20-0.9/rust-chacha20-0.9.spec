# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name chacha20
%global full_version 0.9.1
%global pkgname chacha20-0.9

Name:           rust-chacha20-0.9
Version:        0.9.1
Release:        %autorelease
Summary:        Rust crate "chacha20"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/stream-ciphers
#!RemoteAsset:  sha256:c3613f74bd2eac03dad61bd53dbe620703d4371614fe0bc3b9f04dd36fe4e818
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(cipher-0.4/default) >= 0.4.4
Requires:       crate(cpufeatures-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Additionally provides the ChaCha8, ChaCha12, XChaCha20, XChaCha12 and XChaCha8 stream ciphers, and also optional rand_core-compatible RNGs based on those ciphers.
Source code for takopackized Rust crate "chacha20"

%package     -n %{name}+std
Summary:        ChaCha20 stream cipher (RFC 8439) implemented in pure Rust using traits from the RustCrypto `cipher` crate, with optional architecture-specific hardware acceleration (AVX2, SSE2) - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cipher-0.4/std) >= 0.4.4
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
Additionally provides the ChaCha8, ChaCha12, XChaCha20, XChaCha12 and XChaCha8 stream ciphers, and also optional rand_core-compatible RNGs based on those ciphers.
This metapackage enables feature "std" for the Rust chacha20 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        ChaCha20 stream cipher (RFC 8439) implemented in pure Rust using traits from the RustCrypto `cipher` crate, with optional architecture-specific hardware acceleration (AVX2, SSE2) - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cipher-0.4/zeroize) >= 0.4.4
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
Additionally provides the ChaCha8, ChaCha12, XChaCha20, XChaCha12 and XChaCha8 stream ciphers, and also optional rand_core-compatible RNGs based on those ciphers.
This metapackage enables feature "zeroize" for the Rust chacha20 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
