# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name async-trait
%global full_version 0.1.89
%global pkgname async-trait-0.1

Name:           rust-async-trait-0.1
Version:        0.1.89
Release:        %autorelease
Summary:        Rust crate "async-trait"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/async-trait
#!RemoteAsset:  sha256:9035ad2d096bed7955a320ee7e2230574d28fd3c3a0f186cbea1ff3c7eed5dbb
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.74
Requires:       crate(quote-1/default) >= 1.0.35
Requires:       crate(syn-2/clone-impls) >= 2.0.46
Requires:       crate(syn-2/full) >= 2.0.46
Requires:       crate(syn-2/parsing) >= 2.0.46
Requires:       crate(syn-2/printing) >= 2.0.46
Requires:       crate(syn-2/proc-macro) >= 2.0.46
Requires:       crate(syn-2/visit-mut) >= 2.0.46
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "async-trait"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
