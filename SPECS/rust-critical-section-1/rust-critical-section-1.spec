# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name critical-section
%global full_version 1.2.0
%global pkgname critical-section-1

Name:           rust-critical-section-1
Version:        1.2.0
Release:        %autorelease
Summary:        Rust crate "critical-section"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-embedded/critical-section
#!RemoteAsset:  sha256:790eea4361631c5e7d22598ecd5723ff611904e3344ce8720784c93e3d83d40b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/restore-state-bool) = %{version}
Provides:       crate(%{pkgname}/restore-state-none) = %{version}
Provides:       crate(%{pkgname}/restore-state-u16) = %{version}
Provides:       crate(%{pkgname}/restore-state-u32) = %{version}
Provides:       crate(%{pkgname}/restore-state-u64) = %{version}
Provides:       crate(%{pkgname}/restore-state-u8) = %{version}
Provides:       crate(%{pkgname}/restore-state-usize) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "critical-section"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
