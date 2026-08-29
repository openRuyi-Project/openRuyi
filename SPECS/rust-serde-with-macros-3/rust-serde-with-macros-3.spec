# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serde_with_macros
%global full_version 3.20.0
%global pkgname serde-with-macros-3

Name:           rust-serde-with-macros-3
Version:        3.20.0
Release:        %autorelease
Summary:        Rust crate "serde_with_macros"
License:        MIT OR Apache-2.0
URL:            https://github.com/jonasbb/serde_with/
#!RemoteAsset:  sha256:b90c488738ecb4fb0262f41f43bc40efc5868d9fb744319ddf5f5317f417bfac
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(darling-0.23/default) >= 0.23.0
Requires:       crate(proc-macro2-1/default) >= 1.0.1
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.0
Requires:       crate(syn-2/extra-traits) >= 2.0.0
Requires:       crate(syn-2/full) >= 2.0.0
Requires:       crate(syn-2/parsing) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/schemars-0-8) = %{version}
Provides:       crate(%{pkgname}/schemars-0-9) = %{version}
Provides:       crate(%{pkgname}/schemars-1) = %{version}

%description
Source code for takopackized Rust crate "serde_with_macros"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
