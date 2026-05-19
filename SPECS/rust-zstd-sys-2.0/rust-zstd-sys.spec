# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zstd-sys
%global full_version 2.0.16+zstd.1.5.7
%global pkgname zstd-sys-2.0

Name:           rust-zstd-sys-2.0
Version:        2.0.16
Release:        %autorelease
Summary:        Rust crate "zstd-sys"
License:        MIT/Apache-2.0
URL:            https://github.com/gyscos/zstd-rs
#!RemoteAsset:  sha256:91e19ebc2adc8f83e43039e79776e3fda8ca919132d68a1fed6a5faca2683748
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1.0/default) >= 1.0.45
Requires:       crate(cc-1.0/parallel) >= 1.0.45
Requires:       crate(pkg-config-0.3/default) >= 0.3.28
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/debug)
Provides:       crate(%{pkgname}/experimental)
Provides:       crate(%{pkgname}/fat-lto)
Provides:       crate(%{pkgname}/legacy)
Provides:       crate(%{pkgname}/no-asm)
Provides:       crate(%{pkgname}/no-wasm-shim)
Provides:       crate(%{pkgname}/non-cargo)
Provides:       crate(%{pkgname}/pkg-config)
Provides:       crate(%{pkgname}/seekable)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/thin)
Provides:       crate(%{pkgname}/thin-lto)
Provides:       crate(%{pkgname}/zdict-builder)
Provides:       crate(%{pkgname}/zstdmt)

%description
Source code for takopackized Rust crate "zstd-sys"

%package     -n %{name}+bindgen
Summary:        Low-level bindings for the zstd compression library - feature "bindgen"
Requires:       crate(%{pkgname})
Requires:       crate(bindgen-0.72/runtime) >= 0.72.0
Provides:       crate(%{pkgname}/bindgen)

%description -n %{name}+bindgen
This metapackage enables feature "bindgen" for the Rust zstd-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Low-level bindings for the zstd compression library - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bindgen)
Requires:       crate(%{pkgname}/legacy)
Requires:       crate(%{pkgname}/zdict-builder)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust zstd-sys crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
