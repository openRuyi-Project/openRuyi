# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rhai_codegen
%global full_version 3.2.0
%global pkgname rhai-codegen-3

Name:           rust-rhai-codegen-3
Version:        3.2.0
Release:        %autorelease
Summary:        Rust crate "rhai_codegen"
License:        MIT OR Apache-2.0
URL:            https://rhai.rs/book/plugins/index.html
#!RemoteAsset:  sha256:3cd3a7535e50bf36857e7be7bec276d334e8c2dfa469c2201226fd01638ea5ca
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.0
Requires:       crate(syn-2/extra-traits) >= 2.0.0
Requires:       crate(syn-2/full) >= 2.0.0
Requires:       crate(syn-2/parsing) >= 2.0.0
Requires:       crate(syn-2/printing) >= 2.0.0
Requires:       crate(syn-2/proc-macro) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/metadata) = %{version}
Provides:       crate(%{pkgname}/sync) = %{version}

%description
Source code for takopackized Rust crate "rhai_codegen"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
