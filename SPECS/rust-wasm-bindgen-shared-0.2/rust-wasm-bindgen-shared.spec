# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global debug_package %{nil}
%global __debug_install_post %{nil}

%global crate_name wasm-bindgen-shared
%global full_version 0.2.118
%global pkgname wasm-bindgen-shared-0.2

Name:           rust-wasm-bindgen-shared-0.2
Version:        0.2.118
Release:        %autorelease
Summary:        Rust crate "wasm-bindgen-shared"
License:        MIT OR Apache-2.0
URL:            https://wasm-bindgen.github.io/wasm-bindgen/
#!RemoteAsset:  sha256:5fd04d9e306f1907bd13c6361b5c6bfc7b3b3c095ed3f8a9246390f8dbdee129
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(unicode-ident-1.0/default) >= 1.0.24
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "wasm-bindgen-shared"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
