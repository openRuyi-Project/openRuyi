# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ahash
%global full_version 0.8.12
%global pkgname ahash-0.8

Name:           rust-ahash-0.8
Version:        0.8.12
Release:        %autorelease
Summary:        Rust crate "ahash"
License:        MIT OR Apache-2.0
URL:            https://github.com/tkaitchuck/ahash
#!RemoteAsset:  sha256:5a15f179cd60c4584b8a8c596927aadc462e27f2ca70c04e0071964a73ba7a75
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1.0/default) >= 1.0.0
Requires:       crate(once-cell-1.0/alloc) >= 1.18.0
Requires:       crate(version-check-0.9/default) >= 0.9.4
Requires:       crate(zerocopy-0.8/simd) >= 0.8.24
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/nightly-arm-aes)
Provides:       crate(%{pkgname}/no-rng)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "ahash"

%package     -n %{name}+atomic-polyfill
Summary:        Non-cryptographic hash function using AES-NI for high performance - feature "atomic-polyfill"
Requires:       crate(%{pkgname})
Requires:       crate(once-cell-1.0/alloc) >= 1.18.0
Requires:       crate(once-cell-1.0/critical-section) >= 1.18.0
Requires:       crate(portable-atomic-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/atomic-polyfill)

%description -n %{name}+atomic-polyfill
This metapackage enables feature "atomic-polyfill" for the Rust ahash crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+const-random
Summary:        Non-cryptographic hash function using AES-NI for high performance - feature "const-random" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(const-random-0.1/default) >= 0.1.17
Provides:       crate(%{pkgname}/compile-time-rng)
Provides:       crate(%{pkgname}/const-random)

%description -n %{name}+const-random
This metapackage enables feature "const-random" for the Rust ahash crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "compile-time-rng" feature.

%package     -n %{name}+default
Summary:        Non-cryptographic hash function using AES-NI for high performance - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/runtime-rng)
Requires:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust ahash crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+getrandom
Summary:        Non-cryptographic hash function using AES-NI for high performance - feature "getrandom" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(getrandom-0.3/default) >= 0.3.1
Provides:       crate(%{pkgname}/getrandom)
Provides:       crate(%{pkgname}/runtime-rng)

%description -n %{name}+getrandom
This metapackage enables feature "getrandom" for the Rust ahash crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "runtime-rng" feature.

%package     -n %{name}+serde
Summary:        Non-cryptographic hash function using AES-NI for high performance - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.117
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust ahash crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
