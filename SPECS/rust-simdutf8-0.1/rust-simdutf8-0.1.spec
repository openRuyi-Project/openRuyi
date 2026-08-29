# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name simdutf8
%global full_version 0.1.5
%global pkgname simdutf8-0.1

Name:           rust-simdutf8-0.1
Version:        0.1.5
Release:        %autorelease
Summary:        Rust crate "simdutf8"
License:        MIT OR Apache-2.0
URL:            https://github.com/rusticstuff/simdutf8
#!RemoteAsset:  sha256:e3a9fe34e3e7a50316060351f37187a3f546bce95496156754b601a5fa71b76e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/aarch64-neon) = %{version}
Provides:       crate(%{pkgname}/aarch64-neon-prefetch) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/hints) = %{version}
Provides:       crate(%{pkgname}/public-imp) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "simdutf8"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
