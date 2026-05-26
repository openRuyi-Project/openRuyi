# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bytemuck
%global full_version 1.25.0
%global pkgname bytemuck-1.0

Name:           rust-bytemuck-1.0
Version:        1.25.0
Release:        %autorelease
Summary:        Rust crate "bytemuck"
License:        Zlib OR Apache-2.0 OR MIT
URL:            https://github.com/Lokathor/bytemuck
#!RemoteAsset:  sha256:c8efb64bd706a16a1bdde310ae86b351e4d21550d98d056f22f8a7f7a2183fec
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(bytemuck) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/aarch64-simd)
Provides:       crate(%{pkgname}/align-offset)
Provides:       crate(%{pkgname}/alloc-uninit)
Provides:       crate(%{pkgname}/avx512-simd)
Provides:       crate(%{pkgname}/const-zeroed)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/extern-crate-alloc)
Provides:       crate(%{pkgname}/extern-crate-std)
Provides:       crate(%{pkgname}/impl-core-error)
Provides:       crate(%{pkgname}/min-const-generics)
Provides:       crate(%{pkgname}/must-cast)
Provides:       crate(%{pkgname}/must-cast-extra)
Provides:       crate(%{pkgname}/nightly-docs)
Provides:       crate(%{pkgname}/nightly-float)
Provides:       crate(%{pkgname}/nightly-stdsimd)
Provides:       crate(%{pkgname}/pod-saturating)
Provides:       crate(%{pkgname}/track-caller)
Provides:       crate(%{pkgname}/transparentwrapper-extra)
Provides:       crate(%{pkgname}/unsound-ptr-pod-impl)
Provides:       crate(%{pkgname}/wasm-simd)
Provides:       crate(%{pkgname}/zeroable-atomics)
Provides:       crate(%{pkgname}/zeroable-maybe-uninit)
Provides:       crate(%{pkgname}/zeroable-unwind-fn)

%description
Source code for takopackized Rust crate "bytemuck"

%package     -n %{name}+bytemuck-derive
Summary:        Mucking around with piles of bytes - feature "bytemuck_derive" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(bytemuck-derive-1.0/default) >= 1.10.2
Provides:       crate(%{pkgname}/bytemuck-derive)
Provides:       crate(%{pkgname}/derive)

%description -n %{name}+bytemuck-derive
This metapackage enables feature "bytemuck_derive" for the Rust bytemuck crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "derive" feature.

%package     -n %{name}+latest-stable-rust
Summary:        Mucking around with piles of bytes - feature "latest_stable_rust"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/aarch64-simd)
Requires:       crate(%{pkgname}/align-offset)
Requires:       crate(%{pkgname}/alloc-uninit)
Requires:       crate(%{pkgname}/avx512-simd)
Requires:       crate(%{pkgname}/const-zeroed)
Requires:       crate(%{pkgname}/derive)
Requires:       crate(%{pkgname}/impl-core-error)
Requires:       crate(%{pkgname}/min-const-generics)
Requires:       crate(%{pkgname}/must-cast)
Requires:       crate(%{pkgname}/must-cast-extra)
Requires:       crate(%{pkgname}/pod-saturating)
Requires:       crate(%{pkgname}/track-caller)
Requires:       crate(%{pkgname}/transparentwrapper-extra)
Requires:       crate(%{pkgname}/wasm-simd)
Requires:       crate(%{pkgname}/zeroable-atomics)
Requires:       crate(%{pkgname}/zeroable-maybe-uninit)
Requires:       crate(%{pkgname}/zeroable-unwind-fn)
Provides:       crate(%{pkgname}/latest-stable-rust)

%description -n %{name}+latest-stable-rust
This metapackage enables feature "latest_stable_rust" for the Rust bytemuck crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustversion
Summary:        Mucking around with piles of bytes - feature "rustversion" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(rustversion-1.0/default) >= 1.0.22
Provides:       crate(%{pkgname}/nightly-portable-simd)
Provides:       crate(%{pkgname}/rustversion)

%description -n %{name}+rustversion
This metapackage enables feature "rustversion" for the Rust bytemuck crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "nightly_portable_simd" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
