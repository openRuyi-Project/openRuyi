# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rand_hc
%global full_version 0.1.0
%global pkgname rand-hc-0.1

Name:           rust-rand-hc-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "rand_hc"
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rand_hc
#!RemoteAsset:  sha256:7b40677c7be09ae76218dc623efbf7b18e34bced3f38883af07bb75630a21bc4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rand-core-0.2) >= 0.2.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "rand_hc"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
