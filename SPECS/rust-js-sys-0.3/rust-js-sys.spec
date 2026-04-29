# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global debug_package %{nil}
%global __debug_install_post %{nil}

%global crate_name js-sys
%global full_version 0.3.95
%global pkgname js-sys-0.3

Name:           rust-js-sys-0.3
Version:        0.3.95
Release:        %autorelease
Summary:        Rust crate "js-sys"
License:        MIT OR Apache-2.0
URL:            https://wasm-bindgen.github.io/wasm-bindgen/
#!RemoteAsset:  sha256:2964e92d1d9dc3364cae4d718d93f227e3abb088e747d92e0395bfdedf1c12ca
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(once-cell-1.0) >= 1.21.4
Requires:       crate(wasm-bindgen-0.2) >= 0.2.118
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/unsafe-eval)

%description
Source code for takopackized Rust crate "js-sys"

%package     -n %{name}+default
Summary:        Bindings for all JS global objects and functions in all JS environments like Node.js and browsers, built on `#[wasm_bindgen]` using the `wasm-bindgen` crate - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/std)
Requires:       crate(%{pkgname}/unsafe-eval)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust js-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures
Summary:        Bindings for all JS global objects and functions in all JS environments like Node.js and browsers, built on `#[wasm_bindgen]` using the `wasm-bindgen` crate - feature "futures"
Requires:       crate(%{pkgname})
Requires:       crate(cfg-if-1.0/default) >= 1.0.0
Requires:       crate(futures-util-0.3/std) >= 0.3.31
Provides:       crate(%{pkgname}/futures)

%description -n %{name}+futures
This metapackage enables feature "futures" for the Rust js-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-core-03-stream
Summary:        Bindings for all JS global objects and functions in all JS environments like Node.js and browsers, built on `#[wasm_bindgen]` using the `wasm-bindgen` crate - feature "futures-core-03-stream"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/futures)
Requires:       crate(futures-core-0.3) >= 0.3.8
Provides:       crate(%{pkgname}/futures-core-03-stream)

%description -n %{name}+futures-core-03-stream
This metapackage enables feature "futures-core-03-stream" for the Rust js-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Bindings for all JS global objects and functions in all JS environments like Node.js and browsers, built on `#[wasm_bindgen]` using the `wasm-bindgen` crate - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(wasm-bindgen-0.2/std) >= 0.2.118
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust js-sys crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
