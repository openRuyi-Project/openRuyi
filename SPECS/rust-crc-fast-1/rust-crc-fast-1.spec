# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name crc-fast
%global full_version 1.10.0
%global pkgname crc-fast-1

Name:           rust-crc-fast-1
Version:        1.10.0
Release:        %autorelease
Summary:        Rust crate "crc-fast"
License:        MIT OR Apache-2.0
URL:            https://github.com/awesomized/crc-fast-rust
#!RemoteAsset:  sha256:e75b2483e97a5a7da73ac68a05b629f9c53cff58d8ed1c77866079e18b00dba5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(spin-0.10/mutex) >= 0.10.0
Requires:       crate(spin-0.10/once) >= 0.10.0
Requires:       crate(spin-0.10/rwlock) >= 0.10.0
Requires:       crate(spin-0.10/spin-mutex) >= 0.10.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/ffi) = %{version}
Provides:       crate(%{pkgname}/optimize-crc32-auto) = %{version}
Provides:       crate(%{pkgname}/optimize-crc32-avx512-v4s3x3) = %{version}
Provides:       crate(%{pkgname}/optimize-crc32-avx512-vpclmulqdq-v3x2) = %{version}
Provides:       crate(%{pkgname}/optimize-crc32-neon-blended) = %{version}
Provides:       crate(%{pkgname}/optimize-crc32-neon-eor3-v9s3x2e-s3) = %{version}
Provides:       crate(%{pkgname}/optimize-crc32-neon-v12e-v1) = %{version}
Provides:       crate(%{pkgname}/optimize-crc32-neon-v3s4x2e-v2) = %{version}
Provides:       crate(%{pkgname}/optimize-crc32-sse-v4s3x3) = %{version}
Provides:       crate(%{pkgname}/panic-handler) = %{version}
Provides:       crate(%{pkgname}/vpclmulqdq) = %{version}

%description
Supplies a C-compatible shared library for use in other languages.
Source code for takopackized Rust crate "crc-fast"

%package     -n %{name}+cache
Summary:        World's fastest generic CRC16, CRC32, and CRC64 calculator using SIMD - feature "cache"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/hashbrown) = %{version}
Requires:       crate(%{pkgname}/spin) = %{version}
Provides:       crate(%{pkgname}/cache) = %{version}

%description -n %{name}+cache
Supplies a C-compatible shared library for use in other languages.
This metapackage enables feature "cache" for the Rust crc-fast crate, by
pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        World's fastest generic CRC16, CRC32, and CRC64 calculator using SIMD - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/ffi) = %{version}
Requires:       crate(%{pkgname}/panic-handler) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
Supplies a C-compatible shared library for use in other languages.
This metapackage enables feature "default" for the Rust crc-fast crate, by
pulling in any additional dependencies needed by that feature.

%package     -n %{name}+digest
Summary:        World's fastest generic CRC16, CRC32, and CRC64 calculator using SIMD - feature "digest" and 3 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(digest-0.10/alloc) >= 0.10.0
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/cli) = %{version}
Provides:       crate(%{pkgname}/digest) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+digest
Supplies a C-compatible shared library for use in other languages.
This metapackage enables feature "digest" for the Rust crc-fast crate, by
pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "alloc", "cli", and "std" features.

%package     -n %{name}+hashbrown
Summary:        World's fastest generic CRC16, CRC32, and CRC64 calculator using SIMD - feature "hashbrown"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hashbrown-0.16/default) >= 0.16.0
Provides:       crate(%{pkgname}/hashbrown) = %{version}

%description -n %{name}+hashbrown
Supplies a C-compatible shared library for use in other languages.
This metapackage enables feature "hashbrown" for the Rust crc-fast crate, by
pulling in any additional dependencies needed by that feature.

%package     -n %{name}+spin
Summary:        World's fastest generic CRC16, CRC32, and CRC64 calculator using SIMD - feature "spin"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(spin-0.10/mutex) >= 0.10.0
Requires:       crate(spin-0.10/once) >= 0.10.0
Requires:       crate(spin-0.10/rwlock) >= 0.10.0
Requires:       crate(spin-0.10/spin-mutex) >= 0.10.0
Provides:       crate(%{pkgname}/spin) = %{version}

%description -n %{name}+spin
Supplies a C-compatible shared library for use in other languages.
This metapackage enables feature "spin" for the Rust crc-fast crate, by
pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
