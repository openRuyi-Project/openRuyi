# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name derive_builder_macro
%global full_version 0.11.2
%global pkgname derive-builder-macro-0.11

Name:           rust-derive-builder-macro-0.11
Version:        0.11.2
Release:        %autorelease
Summary:        Rust crate "derive_builder_macro"
License:        MIT OR Apache-2.0
URL:            https://github.com/colin-kiegel/rust-derive-builder
#!RemoteAsset:  sha256:8f0314b72bed045f3a68671b3c86328386762c93f82d98c65c3cb5e5f573dd68
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(derive-builder-core-0.11/default) >= 0.11.2
Requires:       crate(syn-1/default) >= 1.0.91
Requires:       crate(syn-1/extra-traits) >= 1.0.91
Requires:       crate(syn-1/full) >= 1.0.91

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "derive_builder_macro"

%package     -n %{name}+clippy
Summary:        Rust macro to automatically implement the builder pattern for arbitrary structs - feature "clippy"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(derive-builder-core-0.11/clippy) >= 0.11.2
Provides:       crate(%{pkgname}/clippy) = %{version}

%description -n %{name}+clippy
This metapackage enables feature "clippy" for the Rust derive_builder_macro crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
