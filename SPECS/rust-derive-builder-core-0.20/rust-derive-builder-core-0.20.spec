# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name derive_builder_core
%global full_version 0.20.2
%global pkgname derive-builder-core-0.20

Name:           rust-derive-builder-core-0.20
Version:        0.20.2
Release:        %autorelease
Summary:        Rust crate "derive_builder_core"
License:        MIT OR Apache-2.0
URL:            https://github.com/colin-kiegel/rust-derive-builder
#!RemoteAsset:  sha256:2d5bcf7b024d6835cfb3d473887cd966994907effbe9227e8c8219824d06c4e8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(darling-0.20/default) >= 0.20.10
Requires:       crate(proc-macro2-1/default) >= 1.0.37
Requires:       crate(quote-1/default) >= 1.0.35
Requires:       crate(syn-2/default) >= 2.0.15
Requires:       crate(syn-2/extra-traits) >= 2.0.15
Requires:       crate(syn-2/full) >= 2.0.15
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/clippy) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/lib-has-std) = %{version}

%description
Source code for takopackized Rust crate "derive_builder_core"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
