# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name keccak
%global full_version 0.1.6
%global pkgname keccak-0.1

Name:           rust-keccak-0.1
Version:        0.1.6
Release:        %autorelease
Summary:        Rust crate "keccak"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/sponges/tree/master/keccak
#!RemoteAsset:  sha256:cb26cec98cce3a3d96cbb7bced3c4b16e3d13f27ec56dbd62cbc8f39cfb9d653
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cpufeatures-0.2/default) >= 0.2.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/asm) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/no-unroll) = %{version}
Provides:       crate(%{pkgname}/simd) = %{version}

%description
Source code for takopackized Rust crate "keccak"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
