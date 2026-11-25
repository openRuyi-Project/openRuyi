# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name der_derive
%global full_version 0.7.3
%global pkgname der-derive-0.7

Name:           rust-der-derive-0.7
Version:        0.7.3
Release:        %autorelease
Summary:        Rust crate "der_derive"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/formats/tree/master/der/derive
#!RemoteAsset:  sha256:8034092389675178f570469e6c3b0465d3d30b4505c294a6550db47f3c17ad18
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.0
Requires:       crate(syn-2/extra-traits) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "der_derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
