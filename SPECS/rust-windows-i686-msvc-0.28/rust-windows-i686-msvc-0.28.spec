# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name windows_i686_msvc
%global full_version 0.28.0
%global pkgname windows-i686-msvc-0.28

Name:           rust-windows-i686-msvc-0.28
Version:        0.28.0
Release:        %autorelease
Summary:        Rust crate "windows_i686_msvc"
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/windows_i686_msvc
#!RemoteAsset:  sha256:51d5158a43cc43623c0729d1ad6647e62fa384a3d135fd15108d37c683461f64
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "windows_i686_msvc"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
