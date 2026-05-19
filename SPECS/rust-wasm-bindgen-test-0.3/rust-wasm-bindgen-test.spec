# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wasm-bindgen-test
%global full_version 0.3.55
%global pkgname wasm-bindgen-test-0.3

Name:           rust-wasm-bindgen-test-0.3
Version:        0.3.55
Release:        %autorelease
Summary:        Rust crate "wasm-bindgen-test"
License:        MIT OR Apache-2.0
URL:            https://github.com/wasm-bindgen/wasm-bindgen
#!RemoteAsset:  sha256:bfc379bfb624eb59050b509c13e77b4eb53150c350db69628141abce842f2373
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(js-sys-0.3) >= 0.3.82
Requires:       crate(minicov-0.3/default) >= 0.3.0
Requires:       crate(wasm-bindgen-0.2) >= 0.2.105
Requires:       crate(wasm-bindgen-futures-0.4) >= 0.4.55
Requires:       crate(wasm-bindgen-test-macro-0.3/default) >= 0.3.55
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "wasm-bindgen-test"

%package     -n %{name}+gg-alloc
Summary:        Internal testing crate for wasm-bindgen - feature "gg-alloc"
Requires:       crate(%{pkgname})
Requires:       crate(gg-alloc-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/gg-alloc)

%description -n %{name}+gg-alloc
This metapackage enables feature "gg-alloc" for the Rust wasm-bindgen-test crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Internal testing crate for wasm-bindgen - feature "std" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(js-sys-0.3/std) >= 0.3.82
Requires:       crate(wasm-bindgen-0.2/std) >= 0.2.105
Requires:       crate(wasm-bindgen-futures-0.4/std) >= 0.4.55
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust wasm-bindgen-test crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
