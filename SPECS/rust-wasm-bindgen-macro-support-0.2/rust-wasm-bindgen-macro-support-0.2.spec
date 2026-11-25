# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wasm-bindgen-macro-support
%global full_version 0.2.128
%global pkgname wasm-bindgen-macro-support-0.2

Name:           rust-wasm-bindgen-macro-support-0.2
Version:        0.2.128
Release:        %autorelease
Summary:        Rust crate "wasm-bindgen-macro-support"
License:        MIT OR Apache-2.0
URL:            https://wasm-bindgen.github.io/wasm-bindgen/
#!RemoteAsset:  sha256:411e4887f0071ef2d2164a9d5fdf2d20efbef78fccd3a78b0c10a1dc5295e48a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bumpalo-3/default) >= 3.0.0
Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-3/default) >= 3.0.0
Requires:       crate(syn-3/extra-traits) >= 3.0.0
Requires:       crate(syn-3/full) >= 3.0.0
Requires:       crate(syn-3/visit) >= 3.0.0
Requires:       crate(syn-3/visit-mut) >= 3.0.0
Requires:       crate(wasm-bindgen-shared-0.2/default) >= 0.2.128

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/strict-macro) = %{version}

%description
Source code for takopackized Rust crate "wasm-bindgen-macro-support"

%package     -n %{name}+extra-traits
Summary:        Implementation APIs for the `#[wasm_bindgen]` attribute - feature "extra-traits"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(syn-3/extra-traits) >= 3.0.0
Requires:       crate(syn-3/full) >= 3.0.0
Requires:       crate(syn-3/visit) >= 3.0.0
Requires:       crate(syn-3/visit-mut) >= 3.0.0
Provides:       crate(%{pkgname}/extra-traits) = %{version}

%description -n %{name}+extra-traits
This metapackage enables feature "extra-traits" for the Rust wasm-bindgen-macro-support crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
