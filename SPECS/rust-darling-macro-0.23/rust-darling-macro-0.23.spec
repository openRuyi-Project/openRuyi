# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name darling_macro
%global full_version 0.23.0
%global pkgname darling-macro-0.23

Name:           rust-darling-macro-0.23
Version:        0.23.0
Release:        %autorelease
Summary:        Rust crate "darling_macro"
License:        MIT
URL:            https://github.com/TedDriggs/darling
#!RemoteAsset:  sha256:ac3984ec7bd6cfa798e62b4a642426a5be0e68f9401cfc2a01e3fa9ea2fcdb8d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(darling-core-0.23/default) >= 0.23.0
Requires:       crate(quote-1/default) >= 1.0.18
Requires:       crate(syn-2/default) >= 2.0.15
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Use https://crates.io/crates/darling in your code.
Source code for takopackized Rust crate "darling_macro"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
