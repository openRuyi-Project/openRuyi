# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bitflags
%global full_version 0.9.1
%global pkgname bitflags-0.9

Name:           rust-bitflags-0.9
Version:        0.9.1
Release:        %autorelease
Summary:        Rust crate "bitflags"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang-nursery/bitflags
#!RemoteAsset:  sha256:4efd02e230a02e18f92fc2735f44597385ed02ad8f831e7c1c1156ee5e1ab3a5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/example-generated) = %{version}
Provides:       crate(%{pkgname}/unstable-testing) = %{version}

%description
Source code for takopackized Rust crate "bitflags"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
