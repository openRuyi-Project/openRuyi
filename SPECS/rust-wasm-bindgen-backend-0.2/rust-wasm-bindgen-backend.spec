# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wasm-bindgen-backend
%global full_version 0.2.100
%global pkgname wasm-bindgen-backend-0.2

Name:           rust-wasm-bindgen-backend-0.2
Version:        0.2.100
Release:        %autorelease
Summary:        Rust crate "wasm-bindgen-backend"
License:        MIT OR Apache-2.0
URL:            https://rustwasm.github.io/wasm-bindgen/
#!RemoteAsset:  sha256:2f0a0651a5c2bc21487bde11ee802ccaf4c51935d0d3d42a6101f98161700bc6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bumpalo-3.0/default) >= 3.19.0
Requires:       crate(log-0.4/default) >= 0.4.27
Requires:       crate(proc-macro2-1.0/default) >= 1.0.95
Requires:       crate(quote-1.0/default) >= 1.0.40
Requires:       crate(syn-2.0/default) >= 2.0.104
Requires:       crate(syn-2.0/full) >= 2.0.104
Requires:       crate(wasm-bindgen-shared-0.2/default) >= 0.2.100
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "wasm-bindgen-backend"

%package     -n %{name}+extra-traits
Summary:        Backend code generation of the wasm-bindgen tool - feature "extra-traits"
Requires:       crate(%{pkgname})
Requires:       crate(syn-2.0/extra-traits) >= 2.0.104
Requires:       crate(syn-2.0/full) >= 2.0.104
Provides:       crate(%{pkgname}/extra-traits)

%description -n %{name}+extra-traits
This metapackage enables feature "extra-traits" for the Rust wasm-bindgen-backend crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
