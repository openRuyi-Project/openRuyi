# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name darling_macro
%global full_version 0.20.11
%global pkgname darling-macro-0.20

Name:           rust-darling-macro-0.20
Version:        0.20.11
Release:        %autorelease
Summary:        Rust crate "darling_macro"
License:        MIT
URL:            https://github.com/TedDriggs/darling
#!RemoteAsset:  sha256:fc34b93ccb385b40dc71c6fceac4b2ad23662c7eeb248cf10d529b7e055b6ead
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(darling-core-0.20/default) >= 0.20.11
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
