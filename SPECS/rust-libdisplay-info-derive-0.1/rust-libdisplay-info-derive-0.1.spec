# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name libdisplay-info-derive
%global full_version 0.1.1
%global pkgname libdisplay-info-derive-0.1

Name:           rust-libdisplay-info-derive-0.1
Version:        0.1.1
Release:        %autorelease
Summary:        Rust crate "libdisplay-info-derive"
License:        MIT
URL:            https://github.com/Smithay/libdisplay-info-rs
#!RemoteAsset:  sha256:8dc2c710cf5819e91220a446d9e64acc6814386cc22c509c3f0df83c0b874a98
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
Source code for takopackized Rust crate "libdisplay-info-derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
