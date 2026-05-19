# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rust-stemmers
%global full_version 1.2.0
%global pkgname rust-stemmers-1.0

Name:           rust-rust-stemmers-1.0
Version:        1.2.0
Release:        %autorelease
Summary:        Rust crate "rust-stemmers"
License:        MIT/BSD-3-Clause
URL:            https://github.com/CurrySoftware/rust-stemmers
#!RemoteAsset:  sha256:e46a2036019fdb888131db7a4c847a1063a7493f971ed94ea82c67eada63ca54
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(serde-1.0/default) >= 1.0.228
Requires:       crate(serde-derive-1.0/default) >= 1.0.228
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "rust-stemmers"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
