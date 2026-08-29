# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name asn1-rs-impl
%global full_version 0.2.0
%global pkgname asn1-rs-impl-0.2

Name:           rust-asn1-rs-impl-0.2
Version:        0.2.0
Release:        %autorelease
Summary:        Rust crate "asn1-rs-impl"
License:        MIT OR Apache-2.0
URL:            https://github.com/rusticata/asn1-rs
#!RemoteAsset:  sha256:7b18050c2cd6fe86c3a76584ef5e0baf286d038cda203eb6223df2cc413565f7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "asn1-rs-impl"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
