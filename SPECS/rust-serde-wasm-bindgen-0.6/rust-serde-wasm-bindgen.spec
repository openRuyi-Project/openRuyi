# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serde-wasm-bindgen
%global full_version 0.6.5
%global pkgname serde-wasm-bindgen-0.6

Name:           rust-serde-wasm-bindgen-0.6
Version:        0.6.5
Release:        %autorelease
Summary:        Rust crate "serde-wasm-bindgen"
License:        MIT
URL:            https://github.com/RReverser/serde-wasm-bindgen
#!RemoteAsset:  sha256:8302e169f0eddcc139c70f139d19d6467353af16f9fce27e8c30158036a1e16b
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(js-sys-0.3/default) >= 0.3.82
Requires:       crate(serde-1.0/default) >= 1.0.228
Requires:       crate(serde-1.0/derive) >= 1.0.228
Requires:       crate(wasm-bindgen-0.2/default) >= 0.2.105
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "serde-wasm-bindgen"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
