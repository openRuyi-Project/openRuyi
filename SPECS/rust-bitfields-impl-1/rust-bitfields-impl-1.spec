# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bitfields-impl
%global full_version 1.0.2
%global pkgname bitfields-impl-1

Name:           rust-bitfields-impl-1
Version:        1.0.2
Release:        %autorelease
Summary:        Rust crate "bitfields-impl"
License:        MIT
URL:            https://github.com/gregorygaines/bitfields-rs
#!RemoteAsset:  sha256:c09459e6af3016ea58af8332e31d5da117d33a621bad7019355eefccc4a567d4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.41
Requires:       crate(syn-2/default) >= 2.0.108
Requires:       crate(syn-2/extra-traits) >= 2.0.108
Requires:       crate(syn-2/full) >= 2.0.108
Requires:       crate(thiserror-2/default) >= 2.0.17

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Useful for low-level code (embedded or emulators).
Source code for takopackized Rust crate "bitfields-impl"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
