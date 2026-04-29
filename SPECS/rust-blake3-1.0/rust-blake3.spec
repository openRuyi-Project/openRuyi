# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name blake3
%global full_version 1.8.4
%global pkgname blake3-1.0

Name:           rust-blake3-1.0
Version:        1.8.4
Release:        %autorelease
Summary:        Rust crate "blake3"
License:        CC0-1.0 OR Apache-2.0 OR Apache-2.0 WITH LLVM-exception
URL:            https://github.com/BLAKE3-team/BLAKE3
#!RemoteAsset:  sha256:4d2d5991425dfd0785aed03aedcf0b321d61975c9b5b3689c774a2610ae0b51e
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(arrayref-0.3/default) >= 0.3.9
Requires:       crate(arrayvec-0.7) >= 0.7.6
Requires:       crate(cc-1.0/default) >= 1.2.58
Requires:       crate(cfg-if-1.0/default) >= 1.0.4
Requires:       crate(constant-time-eq-0.4) >= 0.4.2
Requires:       crate(cpufeatures-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/neon)
Provides:       crate(%{pkgname}/no-avx2)
Provides:       crate(%{pkgname}/no-avx512)
Provides:       crate(%{pkgname}/no-neon)
Provides:       crate(%{pkgname}/no-sse2)
Provides:       crate(%{pkgname}/no-sse41)
Provides:       crate(%{pkgname}/prefer-intrinsics)
Provides:       crate(%{pkgname}/pure)
Provides:       crate(%{pkgname}/wasm32-simd)

%description
Source code for takopackized Rust crate "blake3"

%package     -n %{name}+digest
Summary:        BLAKE3 hash function - feature "digest" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(digest-0.11/default) >= 0.11.2
Requires:       crate(digest-0.11/mac) >= 0.11.2
Provides:       crate(%{pkgname}/digest)
Provides:       crate(%{pkgname}/traits-preview)

%description -n %{name}+digest
This metapackage enables feature "digest" for the Rust blake3 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "traits-preview" feature.

%package     -n %{name}+mmap
Summary:        BLAKE3 hash function - feature "mmap"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/std)
Requires:       crate(memmap2-0.9/default) >= 0.9.0
Provides:       crate(%{pkgname}/mmap)

%description -n %{name}+mmap
This metapackage enables feature "mmap" for the Rust blake3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rayon
Summary:        BLAKE3 hash function - feature "rayon"
Requires:       crate(%{pkgname})
Requires:       crate(rayon-core-1.0/default) >= 1.12.1
Provides:       crate(%{pkgname}/rayon)

%description -n %{name}+rayon
This metapackage enables feature "rayon" for the Rust blake3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        BLAKE3 hash function - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust blake3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        BLAKE3 hash function - feature "std" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(constant-time-eq-0.4/std) >= 0.4.2
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust blake3 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+zeroize
Summary:        BLAKE3 hash function - feature "zeroize"
Requires:       crate(%{pkgname})
Requires:       crate(arrayvec-0.7/zeroize) >= 0.7.6
Requires:       crate(zeroize-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/zeroize)

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust blake3 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
