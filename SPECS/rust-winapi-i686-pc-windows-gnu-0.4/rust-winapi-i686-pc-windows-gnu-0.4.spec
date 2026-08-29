# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name winapi-i686-pc-windows-gnu
%global full_version 0.4.0
%global pkgname winapi-i686-pc-windows-gnu-0.4

Name:           rust-winapi-i686-pc-windows-gnu-0.4
Version:        0.4.0
Release:        %autorelease
Summary:        Rust crate "winapi-i686-pc-windows-gnu"
License:        MIT OR Apache-2.0
URL:            https://github.com/retep998/winapi-rs
#!RemoteAsset:  sha256:ac3b87c63620426dd9b991e5ce0329eff545bccbbb34f3be09ff6fb6ab51b7b6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Please don't use this crate directly, depend on winapi instead.
Source code for takopackized Rust crate "winapi-i686-pc-windows-gnu"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
