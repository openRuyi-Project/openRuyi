# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name simd_helpers
%global full_version 0.1.0
%global pkgname simd-helpers-0.1

Name:           rust-simd-helpers-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "simd_helpers"
License:        MIT
URL:            https://github.com/lu-zero/simd_helpers
#!RemoteAsset:  sha256:95890f873bec569a0362c235787f3aca6e1e887302ba4840839bcc6459c42da6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(quote-1/default) >= 1.0.2
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "simd_helpers"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
