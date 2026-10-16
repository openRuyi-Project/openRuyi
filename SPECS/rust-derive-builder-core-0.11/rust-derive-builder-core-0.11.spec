# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name derive_builder_core
%global full_version 0.11.2
%global pkgname derive-builder-core-0.11

Name:           rust-derive-builder-core-0.11
Version:        0.11.2
Release:        %autorelease
Summary:        Rust crate "derive_builder_core"
License:        MIT OR Apache-2.0
URL:            https://github.com/colin-kiegel/rust-derive-builder
#!RemoteAsset:  sha256:1f91d4cfa921f1c05904dc3c57b4a32c38aed3340cce209f3a6fd1478babafc4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(darling-0.14/default) >= 0.14.0
Requires:       crate(proc-macro2-1/default) >= 1.0.37
Requires:       crate(quote-1/default) >= 1.0.18
Requires:       crate(syn-1/default) >= 1.0.91
Requires:       crate(syn-1/extra-traits) >= 1.0.91
Requires:       crate(syn-1/full) >= 1.0.91

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/clippy) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "derive_builder_core"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
