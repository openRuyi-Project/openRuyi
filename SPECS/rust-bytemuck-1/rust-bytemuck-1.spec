# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bytemuck
%global full_version 1.25.0
%global pkgname bytemuck-1

Name:           rust-bytemuck-1
Version:        1.25.0
Release:        %autorelease
Summary:        Rust crate "bytemuck"
License:        Zlib OR Apache-2.0 OR MIT
URL:            https://github.com/Lokathor/bytemuck
#!RemoteAsset:  sha256:c8efb64bd706a16a1bdde310ae86b351e4d21550d98d056f22f8a7f7a2183fec
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/aarch64-simd) = %{version}
Provides:       crate(%{pkgname}/align-offset) = %{version}
Provides:       crate(%{pkgname}/alloc-uninit) = %{version}
Provides:       crate(%{pkgname}/avx512-simd) = %{version}
Provides:       crate(%{pkgname}/const-zeroed) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/extern-crate-alloc) = %{version}
Provides:       crate(%{pkgname}/extern-crate-std) = %{version}
Provides:       crate(%{pkgname}/impl-core-error) = %{version}
Provides:       crate(%{pkgname}/min-const-generics) = %{version}
Provides:       crate(%{pkgname}/must-cast) = %{version}
Provides:       crate(%{pkgname}/must-cast-extra) = %{version}
Provides:       crate(%{pkgname}/nightly-docs) = %{version}
Provides:       crate(%{pkgname}/nightly-float) = %{version}
Provides:       crate(%{pkgname}/nightly-stdsimd) = %{version}
Provides:       crate(%{pkgname}/pod-saturating) = %{version}
Provides:       crate(%{pkgname}/track-caller) = %{version}
Provides:       crate(%{pkgname}/transparentwrapper-extra) = %{version}
Provides:       crate(%{pkgname}/unsound-ptr-pod-impl) = %{version}
Provides:       crate(%{pkgname}/wasm-simd) = %{version}
Provides:       crate(%{pkgname}/zeroable-atomics) = %{version}
Provides:       crate(%{pkgname}/zeroable-maybe-uninit) = %{version}
Provides:       crate(%{pkgname}/zeroable-unwind-fn) = %{version}

%description
Source code for takopackized Rust crate "bytemuck"

%package     -n %{name}+bytemuck-derive
Summary:        Mucking around with piles of bytes - feature "bytemuck_derive" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytemuck-derive-1/default) >= 1.10.2
Provides:       crate(%{pkgname}/bytemuck-derive) = %{version}
Provides:       crate(%{pkgname}/derive) = %{version}

%description -n %{name}+bytemuck-derive
This metapackage enables feature "bytemuck_derive" for the Rust bytemuck crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "derive" feature.

%package     -n %{name}+latest-stable-rust
Summary:        Mucking around with piles of bytes - feature "latest_stable_rust"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/aarch64-simd) = %{version}
Requires:       crate(%{pkgname}/align-offset) = %{version}
Requires:       crate(%{pkgname}/alloc-uninit) = %{version}
Requires:       crate(%{pkgname}/avx512-simd) = %{version}
Requires:       crate(%{pkgname}/const-zeroed) = %{version}
Requires:       crate(%{pkgname}/derive) = %{version}
Requires:       crate(%{pkgname}/impl-core-error) = %{version}
Requires:       crate(%{pkgname}/min-const-generics) = %{version}
Requires:       crate(%{pkgname}/must-cast) = %{version}
Requires:       crate(%{pkgname}/must-cast-extra) = %{version}
Requires:       crate(%{pkgname}/pod-saturating) = %{version}
Requires:       crate(%{pkgname}/track-caller) = %{version}
Requires:       crate(%{pkgname}/transparentwrapper-extra) = %{version}
Requires:       crate(%{pkgname}/wasm-simd) = %{version}
Requires:       crate(%{pkgname}/zeroable-atomics) = %{version}
Requires:       crate(%{pkgname}/zeroable-maybe-uninit) = %{version}
Requires:       crate(%{pkgname}/zeroable-unwind-fn) = %{version}
Provides:       crate(%{pkgname}/latest-stable-rust) = %{version}

%description -n %{name}+latest-stable-rust
This metapackage enables feature "latest_stable_rust" for the Rust bytemuck crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustversion
Summary:        Mucking around with piles of bytes - feature "rustversion" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustversion-1/default) >= 1.0.22
Provides:       crate(%{pkgname}/nightly-portable-simd) = %{version}
Provides:       crate(%{pkgname}/rustversion) = %{version}

%description -n %{name}+rustversion
This metapackage enables feature "rustversion" for the Rust bytemuck crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "nightly_portable_simd" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
