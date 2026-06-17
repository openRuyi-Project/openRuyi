# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wasm-bindgen-shared
%global full_version 0.2.121
%global pkgname wasm-bindgen-shared-0.2

Name:           rust-wasm-bindgen-shared-0.2
Version:        0.2.121
Release:        %autorelease
Summary:        Rust crate "wasm-bindgen-shared"
License:        MIT OR Apache-2.0
URL:            https://wasm-bindgen.github.io/wasm-bindgen/
#!RemoteAsset:  sha256:c4e0100b01e9f0d03189a92b96772a1fb998639d981193d7dbab487302513441
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(unicode-ident-1/default) >= 1.0.5
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "wasm-bindgen-shared"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
