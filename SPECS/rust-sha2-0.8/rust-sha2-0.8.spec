# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sha2
%global full_version 0.8.2
%global pkgname sha2-0.8

Name:           rust-sha2-0.8
Version:        0.8.2
Release:        %autorelease
Summary:        Rust crate "sha2"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/hashes
#!RemoteAsset:  sha256:a256f46ea78a0c0d9ff00077504903ac881a1dafdc20da66545699e7776b3e69
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(block-buffer-0.7/default) >= 0.7.0
Requires:       crate(digest-0.8/default) >= 0.8.0
Requires:       crate(fake-simd-0.1/default) >= 0.1.0
Requires:       crate(opaque-debug-0.2/default) >= 0.2.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/compress) = %{version}

%description
Source code for takopackized Rust crate "sha2"

%package     -n %{name}+asm-aarch64
Summary:        Pure Rust implementation of the SHA-2 hash function family including SHA-224, SHA-256, SHA-384, and SHA-512 - feature "asm-aarch64"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/asm) = %{version}
Requires:       crate(%{pkgname}/libc) = %{version}
Provides:       crate(%{pkgname}/asm-aarch64) = %{version}

%description -n %{name}+asm-aarch64
This metapackage enables feature "asm-aarch64" for the Rust sha2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libc
Summary:        Pure Rust implementation of the SHA-2 hash function family including SHA-224, SHA-256, SHA-384, and SHA-512 - feature "libc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libc-0.2/default) >= 0.2.68
Provides:       crate(%{pkgname}/libc) = %{version}

%description -n %{name}+libc
This metapackage enables feature "libc" for the Rust sha2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sha2-asm
Summary:        Pure Rust implementation of the SHA-2 hash function family including SHA-224, SHA-256, SHA-384, and SHA-512 - feature "sha2-asm" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sha2-asm-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/asm) = %{version}
Provides:       crate(%{pkgname}/sha2-asm) = %{version}

%description -n %{name}+sha2-asm
This metapackage enables feature "sha2-asm" for the Rust sha2 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "asm" feature.

%package     -n %{name}+std
Summary:        Pure Rust implementation of the SHA-2 hash function family including SHA-224, SHA-256, SHA-384, and SHA-512 - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(digest-0.8/std) >= 0.8.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust sha2 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
