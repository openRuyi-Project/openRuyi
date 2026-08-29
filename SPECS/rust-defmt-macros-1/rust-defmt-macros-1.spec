# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name defmt-macros
%global full_version 1.1.0
%global pkgname defmt-macros-1

Name:           rust-defmt-macros-1
Version:        1.1.0
Release:        %autorelease
Summary:        Rust crate "defmt-macros"
License:        MIT OR Apache-2.0
URL:            https://github.com/knurling-rs/defmt
#!RemoteAsset:  sha256:f0a27770e9c8f719a79d8b638281f4d828f77d8fd61e0bd94451b9b85e576a0b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(defmt-parser-1/default) >= 1.0.0
Requires:       crate(proc-macro-error2-2/default) >= 2.0.0
Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.0
Requires:       crate(syn-2/extra-traits) >= 2.0.0
Requires:       crate(syn-2/full) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/unstable-test) = %{version}

%description
Source code for takopackized Rust crate "defmt-macros"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
