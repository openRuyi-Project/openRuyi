# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rand
%global full_version 0.6.5
%global pkgname rand-0.6

Name:           rust-rand-0.6
Version:        0.6.5
Release:        %autorelease
Summary:        Rust crate "rand"
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rand
#!RemoteAsset:  sha256:6d71dacdc3c88c1fde3885a3be3fbab9f35724e6ce99467f7d9c5026132184ca
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(autocfg-0.1) >= 0.1.0
Requires:       crate(libc-0.2) >= 0.2.0
Requires:       crate(rand-chacha-0.1/default) >= 0.1.0
Requires:       crate(rand-core-0.4/default) >= 0.4.0
Requires:       crate(rand-hc-0.1/default) >= 0.1.0
Requires:       crate(rand-isaac-0.1/default) >= 0.1.0
Requires:       crate(rand-jitter-0.1/default) >= 0.1.0
Requires:       crate(rand-pcg-0.1/default) >= 0.1.0
Requires:       crate(rand-xorshift-0.1/default) >= 0.1.0
Requires:       crate(winapi-0.3/default) >= 0.3.0
Requires:       crate(winapi-0.3/minwindef) >= 0.3.0
Requires:       crate(winapi-0.3/ntsecapi) >= 0.3.0
Requires:       crate(winapi-0.3/profileapi) >= 0.3.0
Requires:       crate(winapi-0.3/winnt) >= 0.3.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/i128-support) = %{version}

%description
Source code for takopackized Rust crate "rand"

%package     -n %{name}+alloc
Summary:        Random number generators and other randomness functionality - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-core-0.4/alloc) >= 0.4.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust rand crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+log
Summary:        Random number generators and other randomness functionality - feature "log"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/log) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust rand crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+packed-simd
Summary:        Random number generators and other randomness functionality - feature "packed_simd" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(packed-simd-0.3/default) >= 0.3.0
Requires:       crate(packed-simd-0.3/into-bits) >= 0.3.0
Provides:       crate(%{pkgname}/nightly) = %{version}
Provides:       crate(%{pkgname}/packed-simd) = %{version}
Provides:       crate(%{pkgname}/simd-support) = %{version}

%description -n %{name}+packed-simd
This metapackage enables feature "packed_simd" for the Rust rand crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "nightly", and "simd_support" features.

%package     -n %{name}+rand-os
Summary:        Random number generators and other randomness functionality - feature "rand_os"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-os-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/rand-os) = %{version}

%description -n %{name}+rand-os
This metapackage enables feature "rand_os" for the Rust rand crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde1
Summary:        Random number generators and other randomness functionality - feature "serde1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-core-0.4/serde1) >= 0.4.0
Requires:       crate(rand-isaac-0.1/serde1) >= 0.1.0
Requires:       crate(rand-xorshift-0.1/serde1) >= 0.1.0
Provides:       crate(%{pkgname}/serde1) = %{version}

%description -n %{name}+serde1
This metapackage enables feature "serde1" for the Rust rand crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Random number generators and other randomness functionality - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/rand-os) = %{version}
Requires:       crate(rand-core-0.4/std) >= 0.4.0
Requires:       crate(rand-jitter-0.1/std) >= 0.1.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust rand crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+stdweb
Summary:        Random number generators and other randomness functionality - feature "stdweb"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-os-0.1/stdweb) >= 0.1.0
Provides:       crate(%{pkgname}/stdweb) = %{version}

%description -n %{name}+stdweb
This metapackage enables feature "stdweb" for the Rust rand crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wasm-bindgen
Summary:        Random number generators and other randomness functionality - feature "wasm-bindgen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-os-0.1/wasm-bindgen) >= 0.1.0
Provides:       crate(%{pkgname}/wasm-bindgen) = %{version}

%description -n %{name}+wasm-bindgen
This metapackage enables feature "wasm-bindgen" for the Rust rand crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
