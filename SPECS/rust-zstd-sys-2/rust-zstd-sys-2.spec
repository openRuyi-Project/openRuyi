# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zstd-sys
%global full_version 2.0.16+zstd.1.5.7
%global pkgname zstd-sys-2

Name:           rust-zstd-sys-2
Version:        2.0.16
Release:        %autorelease
Summary:        Rust crate "zstd-sys"
License:        MIT OR Apache-2.0
URL:            https://github.com/gyscos/zstd-rs
#!RemoteAsset:  sha256:91e19ebc2adc8f83e43039e79776e3fda8ca919132d68a1fed6a5faca2683748
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1) >= 1.0.45
Requires:       crate(cc-1/parallel) >= 1.0.45
Requires:       crate(pkg-config-0.3) >= 0.3.28
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/debug) = %{version}
Provides:       crate(%{pkgname}/experimental) = %{version}
Provides:       crate(%{pkgname}/fat-lto) = %{version}
Provides:       crate(%{pkgname}/legacy) = %{version}
Provides:       crate(%{pkgname}/no-asm) = %{version}
Provides:       crate(%{pkgname}/no-wasm-shim) = %{version}
Provides:       crate(%{pkgname}/non-cargo) = %{version}
Provides:       crate(%{pkgname}/pkg-config) = %{version}
Provides:       crate(%{pkgname}/seekable) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/thin) = %{version}
Provides:       crate(%{pkgname}/thin-lto) = %{version}
Provides:       crate(%{pkgname}/zdict-builder) = %{version}
Provides:       crate(%{pkgname}/zstdmt) = %{version}

%description
Source code for takopackized Rust crate "zstd-sys"

%package     -n %{name}+bindgen
Summary:        Low-level bindings for the zstd compression library - feature "bindgen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bindgen-0.72/runtime) >= 0.72.0
Provides:       crate(%{pkgname}/bindgen) = %{version}

%description -n %{name}+bindgen
This metapackage enables feature "bindgen" for the Rust zstd-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Low-level bindings for the zstd compression library - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bindgen) = %{version}
Requires:       crate(%{pkgname}/legacy) = %{version}
Requires:       crate(%{pkgname}/zdict-builder) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust zstd-sys crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
