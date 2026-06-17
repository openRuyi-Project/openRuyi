# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name openssl-src
%global full_version 300.6.0+3.6.2
%global pkgname openssl-src-300

Name:           rust-openssl-src-300
Version:        300.6.0
Release:        %autorelease
Summary:        Rust crate "openssl-src"
License:        MIT OR Apache-2.0
URL:            https://github.com/alexcrichton/openssl-src-rs
#!RemoteAsset:  sha256:a8e8cbfd3a4a8c8f089147fd7aaa33cf8c7450c4d09f8f80698a0cf093abeff4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1/default) >= 1.0.79
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/camellia) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/force-engine) = %{version}
Provides:       crate(%{pkgname}/idea) = %{version}
Provides:       crate(%{pkgname}/ktls) = %{version}
Provides:       crate(%{pkgname}/legacy) = %{version}
Provides:       crate(%{pkgname}/no-dso) = %{version}
Provides:       crate(%{pkgname}/seed) = %{version}
Provides:       crate(%{pkgname}/ssl3) = %{version}
Provides:       crate(%{pkgname}/weak-crypto) = %{version}

%description
Source code for takopackized Rust crate "openssl-src"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
