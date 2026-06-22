# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name knuffel-derive
%global full_version 3.2.0
%global pkgname knuffel-derive-3

Name:           rust-knuffel-derive-3
Version:        3.2.0
Release:        %autorelease
Summary:        Rust crate "knuffel-derive"
License:        MIT OR Apache-2.0
URL:            https://github.com/tailhook/knuffel
#!RemoteAsset:  sha256:91977f56c49cfb961e3d840e2e7c6e4a56bde7283898cf606861f1421348283d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(heck-0.4/default) >= 0.4.1
Requires:       crate(heck-0.4/unicode) >= 0.4.1
Requires:       crate(proc-macro-error-1/default) >= 1.0.4
Requires:       crate(proc-macro2-1/default) >= 1.0.32
Requires:       crate(quote-1/default) >= 1.0.10
Requires:       crate(syn-1/default) >= 1.0.81
Requires:       crate(syn-1/extra-traits) >= 1.0.81
Requires:       crate(syn-1/full) >= 1.0.81
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "knuffel-derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
