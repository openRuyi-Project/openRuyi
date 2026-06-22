# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name prost-derive
%global full_version 0.12.6
%global pkgname prost-derive-0.12

Name:           rust-prost-derive-0.12
Version:        0.12.6
Release:        %autorelease
Summary:        Rust crate "prost-derive"
License:        Apache-2.0
URL:            https://github.com/tokio-rs/prost
#!RemoteAsset:  sha256:81bddcdb20abf9501610992b6759a4c888aef7d1a7247ef75e2404275ac24af1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1/default) >= 1.0.1
Requires:       crate(itertools-0.10/use-alloc) >= 0.10.0
Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.0
Requires:       crate(syn-2/extra-traits) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "prost-derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
