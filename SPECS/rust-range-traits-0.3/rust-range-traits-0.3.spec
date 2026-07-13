# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name range-traits
%global full_version 0.3.2
%global pkgname range-traits-0.3

Name:           rust-range-traits-0.3
Version:        0.3.2
Release:        %autorelease
Summary:        Rust crate "range-traits"
License:        MIT OR Apache-2.0
URL:            https://github.com/timothee-haudebourg/range-traits
#!RemoteAsset:  sha256:d20581732dd76fa913c7dff1a2412b714afe3573e94d41c34719de73337cc8ab
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "range-traits"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
