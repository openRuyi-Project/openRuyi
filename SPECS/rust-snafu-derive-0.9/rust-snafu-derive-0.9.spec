# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name snafu-derive
%global full_version 0.9.2
%global pkgname snafu-derive-0.9

Name:           rust-snafu-derive-0.9
Version:        0.9.2
Release:        %autorelease
Summary:        Rust crate "snafu-derive"
License:        MIT OR Apache-2.0
URL:            https://github.com/shepmaster/snafu
#!RemoteAsset:  sha256:287f59010008f0d7cf5e3b03196d666c1acc46c8d3e9cf34c28a1a7157601e72
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(heck-0.4) >= 0.4.0
Requires:       crate(proc-macro2-1) >= 1.0.52
Requires:       crate(quote-1) >= 1.0.25
Requires:       crate(syn-2/clone-impls) >= 2.0.0
Requires:       crate(syn-2/derive) >= 2.0.0
Requires:       crate(syn-2/full) >= 2.0.0
Requires:       crate(syn-2/parsing) >= 2.0.0
Requires:       crate(syn-2/printing) >= 2.0.0
Requires:       crate(syn-2/proc-macro) >= 2.0.0
Requires:       crate(syn-2/visit-mut) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/unstable-provider-api) = %{version}

%description
Source code for takopackized Rust crate "snafu-derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
