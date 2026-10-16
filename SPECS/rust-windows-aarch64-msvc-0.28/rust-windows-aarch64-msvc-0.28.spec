# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name windows_aarch64_msvc
%global full_version 0.28.0
%global pkgname windows-aarch64-msvc-0.28

Name:           rust-windows-aarch64-msvc-0.28
Version:        0.28.0
Release:        %autorelease
Summary:        Rust crate "windows_aarch64_msvc"
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/windows_aarch64_msvc
#!RemoteAsset:  sha256:52695a41e536859d5308cc613b4a022261a274390b25bd29dfff4bf08505f3c2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "windows_aarch64_msvc"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
