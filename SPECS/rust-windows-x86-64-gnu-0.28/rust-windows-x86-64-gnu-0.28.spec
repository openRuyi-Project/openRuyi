# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name windows_x86_64_gnu
%global full_version 0.28.0
%global pkgname windows-x86-64-gnu-0.28

Name:           rust-windows-x86-64-gnu-0.28
Version:        0.28.0
Release:        %autorelease
Summary:        Rust crate "windows_x86_64_gnu"
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/windows_x86_64_gnu
#!RemoteAsset:  sha256:bc31f409f565611535130cfe7ee8e6655d3fa99c1c61013981e491921b5ce954
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "windows_x86_64_gnu"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
