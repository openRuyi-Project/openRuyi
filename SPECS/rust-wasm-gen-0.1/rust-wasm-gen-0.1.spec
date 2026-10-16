# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wasm-gen
%global full_version 0.1.4
%global pkgname wasm-gen-0.1

Name:           rust-wasm-gen-0.1
Version:        0.1.4
Release:        %autorelease
Summary:        Rust crate "wasm-gen"
License:        MIT
URL:            https://github.com/xtuc/wasm-gen
#!RemoteAsset:  sha256:b854b1461005a7b3365742310f7faa3cac3add809d66928c64a40c7e9e842ebb
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(byteorder-0.5) >= 0.5.0
Requires:       crate(leb128-0.2/default) >= 0.2.4

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "wasm-gen"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
