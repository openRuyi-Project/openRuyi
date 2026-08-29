# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name nalgebra-macros
%global full_version 0.3.0
%global pkgname nalgebra-macros-0.3

Name:           rust-nalgebra-macros-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "nalgebra-macros"
License:        Apache-2.0
URL:            https://nalgebra.rs
#!RemoteAsset:  sha256:973e7178a678cfd059ccec50887658d482ce16b0aa9da3888ddeab5cd5eb4889
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.0
Requires:       crate(syn-2/full) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "nalgebra-macros"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
