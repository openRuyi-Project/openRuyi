# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name asn1-rs-derive
%global full_version 0.6.0
%global pkgname asn1-rs-derive-0.6

Name:           rust-asn1-rs-derive-0.6
Version:        0.6.0
Release:        %autorelease
Summary:        Rust crate "asn1-rs-derive"
License:        MIT OR Apache-2.0
URL:            https://github.com/rusticata/asn1-rs
#!RemoteAsset:  sha256:3109e49b1e4909e9db6515a30c633684d68cdeaa252f215214cb4fa1a5bfee2c
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
