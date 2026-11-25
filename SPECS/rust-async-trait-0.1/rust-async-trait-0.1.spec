# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name async-trait
%global full_version 0.1.92
%global pkgname async-trait-0.1

Name:           rust-async-trait-0.1
Version:        0.1.92
Release:        %autorelease
Summary:        Rust crate "async-trait"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/async-trait
#!RemoteAsset:  sha256:82f6aeea286b8eb4dd3431a1be1b59d290ace00f5bfd8e2a159bc2a05e2c1667
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.74
Requires:       crate(quote-1/default) >= 1.0.35
Requires:       crate(syn-3/clone-impls) >= 3.0.0
Requires:       crate(syn-3/full) >= 3.0.0
Requires:       crate(syn-3/parsing) >= 3.0.0
Requires:       crate(syn-3/printing) >= 3.0.0
Requires:       crate(syn-3/proc-macro) >= 3.0.0
Requires:       crate(syn-3/visit-mut) >= 3.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "async-trait"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
