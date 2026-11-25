# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wasm-bindgen-macro
%global full_version 0.2.128
%global pkgname wasm-bindgen-macro-0.2

Name:           rust-wasm-bindgen-macro-0.2
Version:        0.2.128
Release:        %autorelease
Summary:        Rust crate "wasm-bindgen-macro"
License:        MIT OR Apache-2.0
URL:            https://wasm-bindgen.github.io/wasm-bindgen/
#!RemoteAsset:  sha256:a690d511e3c1a8b3a55e33511e3c2c00c78415cd23650f32b808627f5696b9ed
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(wasm-bindgen-macro-support-0.2/default) >= 0.2.128

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "wasm-bindgen-macro"

%package     -n %{name}+strict-macro
Summary:        Definition of the `#[wasm_bindgen]` attribute, an internal dependency - feature "strict-macro"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wasm-bindgen-macro-support-0.2/strict-macro) >= 0.2.128
Provides:       crate(%{pkgname}/strict-macro) = %{version}

%description -n %{name}+strict-macro
This metapackage enables feature "strict-macro" for the Rust wasm-bindgen-macro crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
