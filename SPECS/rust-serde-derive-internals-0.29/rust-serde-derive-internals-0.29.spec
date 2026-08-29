# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serde_derive_internals
%global full_version 0.29.1
%global pkgname serde-derive-internals-0.29

Name:           rust-serde-derive-internals-0.29
Version:        0.29.1
Release:        %autorelease
Summary:        Rust crate "serde_derive_internals"
License:        MIT OR Apache-2.0
URL:            https://serde.rs
#!RemoteAsset:  sha256:18d26a20a969b9e3fdf2fc2d9f21eda6c40e2de84c9408bb5d3b05d499aae711
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1) >= 1.0.74
Requires:       crate(quote-1) >= 1.0.35
Requires:       crate(syn-2/clone-impls) >= 2.0.46
Requires:       crate(syn-2/derive) >= 2.0.46
Requires:       crate(syn-2/parsing) >= 2.0.46
Requires:       crate(syn-2/printing) >= 2.0.46
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Unstable.
Source code for takopackized Rust crate "serde_derive_internals"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
