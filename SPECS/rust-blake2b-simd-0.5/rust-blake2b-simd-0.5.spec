# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name blake2b_simd
%global full_version 0.5.11
%global pkgname blake2b-simd-0.5

Name:           rust-blake2b-simd-0.5
Version:        0.5.11
Release:        %autorelease
Summary:        Rust crate "blake2b_simd"
License:        MIT
URL:            https://github.com/oconnor663/blake2_simd
#!RemoteAsset:  sha256:afa748e348ad3be8263be728124b24a24f268266f6f5d58af9d75f6a40b5c587
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(arrayref-0.3/default) >= 0.3.5
Requires:       crate(arrayvec-0.5) >= 0.5.0
Requires:       crate(constant-time-eq-0.1/default) >= 0.1.3

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/uninline-portable) = %{version}

%description
Source code for takopackized Rust crate "blake2b_simd"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
