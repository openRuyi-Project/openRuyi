# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name js-sys
%global full_version 0.3.98
%global pkgname js-sys-0.3

Name:           rust-js-sys-0.3
Version:        0.3.98
Release:        %autorelease
Summary:        Rust crate "js-sys"
License:        MIT OR Apache-2.0
URL:            https://wasm-bindgen.github.io/wasm-bindgen/
#!RemoteAsset:  sha256:67df7112613f8bfd9150013a0314e196f4800d3201ae742489d999db2f979f08
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(once-cell-1) >= 1.12.0
Requires:       crate(wasm-bindgen-0.2) >= 0.2.121
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/unsafe-eval) = %{version}

%description
Source code for takopackized Rust crate "js-sys"

%package     -n %{name}+default
Summary:        Bindings for all JS global objects and functions in all JS environments like Node.js and browsers, built on `#[wasm_bindgen]` using the `wasm-bindgen` crate - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/unsafe-eval) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust js-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-core-03-stream
Summary:        Bindings for all JS global objects and functions in all JS environments like Node.js and browsers, built on `#[wasm_bindgen]` using the `wasm-bindgen` crate - feature "futures-core-03-stream"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-core-0.3) >= 0.3.8
Requires:       crate(futures-util-0.3/std) >= 0.3.31
Provides:       crate(%{pkgname}/futures-core-03-stream) = %{version}

%description -n %{name}+futures-core-03-stream
This metapackage enables feature "futures-core-03-stream" for the Rust js-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Bindings for all JS global objects and functions in all JS environments like Node.js and browsers, built on `#[wasm_bindgen]` using the `wasm-bindgen` crate - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-util-0.3/std) >= 0.3.31
Requires:       crate(wasm-bindgen-0.2/std) >= 0.2.121
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust js-sys crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
