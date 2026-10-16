# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rand_chacha
%global full_version 0.1.1
%global pkgname rand-chacha-0.1

Name:           rust-rand-chacha-0.1
Version:        0.1.1
Release:        %autorelease
Summary:        Rust crate "rand_chacha"
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rand_chacha
#!RemoteAsset:  sha256:556d3a1ca6600bfcbab7c7c91ccb085ac7fbbcd70e008a98742e7847f4f7bcef
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(autocfg-0.1) >= 0.1.0
Requires:       crate(rand-core-0.2) >= 0.2.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "rand_chacha"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
