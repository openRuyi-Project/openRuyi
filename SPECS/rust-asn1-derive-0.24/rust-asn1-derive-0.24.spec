# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name asn1_derive
%global full_version 0.24.1
%global pkgname asn1-derive-0.24

Name:           rust-asn1-derive-0.24
Version:        0.24.1
Release:        %autorelease
Summary:        Rust crate "asn1_derive"
License:        BSD-3-Clause
URL:            https://github.com/alex/rust-asn1
#!RemoteAsset:  sha256:909e307f1cc32bb8bccbd98f446e6d1bf03fa30f7b53a4337da7181ad30fa11a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.69
Requires:       crate(quote-1/default) >= 1.0.28
Requires:       crate(syn-2/default) >= 2.0.21
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "asn1_derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
