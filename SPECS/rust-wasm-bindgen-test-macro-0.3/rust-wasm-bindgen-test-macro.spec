# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wasm-bindgen-test-macro
%global full_version 0.3.55
%global pkgname wasm-bindgen-test-macro-0.3

Name:           rust-wasm-bindgen-test-macro-0.3
Version:        0.3.55
Release:        %autorelease
Summary:        Rust crate "wasm-bindgen-test-macro"
License:        MIT OR Apache-2.0
URL:            https://github.com/wasm-bindgen/wasm-bindgen
#!RemoteAsset:  sha256:085b2df989e1e6f9620c1311df6c996e83fe16f57792b272ce1e024ac16a90f1
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1.0/default) >= 1.0.0
Requires:       crate(quote-1.0/default) >= 1.0.0
Requires:       crate(syn-2.0/derive) >= 2.0.0
Requires:       crate(syn-2.0/parsing) >= 2.0.0
Requires:       crate(syn-2.0/printing) >= 2.0.0
Requires:       crate(syn-2.0/proc-macro) >= 2.0.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "wasm-bindgen-test-macro"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
