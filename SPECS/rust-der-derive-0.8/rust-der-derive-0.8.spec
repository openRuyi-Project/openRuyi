# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name der_derive
%global full_version 0.8.0
%global pkgname der-derive-0.8

Name:           rust-der-derive-0.8
Version:        0.8.0
Release:        %autorelease
Summary:        Rust crate "der_derive"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/formats/tree/master/der_derive
#!RemoteAsset:  sha256:59600e2c2d636fde9b65e99cc6445ac770c63d3628195ff39932b8d6d7409903
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
