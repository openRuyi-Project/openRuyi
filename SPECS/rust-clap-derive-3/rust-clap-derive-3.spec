# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name clap_derive
%global full_version 3.2.25
%global pkgname clap-derive-3

Name:           rust-clap-derive-3
Version:        3.2.25
Release:        %autorelease
Summary:        Rust crate "clap_derive"
License:        MIT OR Apache-2.0
URL:            https://github.com/clap-rs/clap/tree/master/clap_derive
#!RemoteAsset:  sha256:ae6371b8bdc8b7d3959e9cf7b22d4435ef3e79e138688421ec654acf8c81b008
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(heck-0.4/default) >= 0.4.0
Requires:       crate(proc-macro-error-1/default) >= 1.0.0
Requires:       crate(proc-macro2-1/default) >= 1.0.28
Requires:       crate(quote-1/default) >= 1.0.9
Requires:       crate(syn-1/default) >= 1.0.74
Requires:       crate(syn-1/full) >= 1.0.74

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/debug) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/deprecated) = %{version}
Provides:       crate(%{pkgname}/raw-deprecated) = %{version}
Provides:       crate(%{pkgname}/unstable-v4) = %{version}

%description
Source code for takopackized Rust crate "clap_derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
