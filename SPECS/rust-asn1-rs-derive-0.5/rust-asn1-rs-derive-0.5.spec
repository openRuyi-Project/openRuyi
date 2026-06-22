# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name asn1-rs-derive
%global full_version 0.5.1
%global pkgname asn1-rs-derive-0.5

Name:           rust-asn1-rs-derive-0.5
Version:        0.5.1
Release:        %autorelease
Summary:        Rust crate "asn1-rs-derive"
License:        MIT OR Apache-2.0
URL:            https://github.com/rusticata/asn1-rs
#!RemoteAsset:  sha256:965c2d33e53cb6b267e148a4cb0760bc01f4904c1cd4bb4002a085bb016d1490
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.0
Requires:       crate(syn-2/full) >= 2.0.0
Requires:       crate(synstructure-0.13/default) >= 0.13.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "asn1-rs-derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
