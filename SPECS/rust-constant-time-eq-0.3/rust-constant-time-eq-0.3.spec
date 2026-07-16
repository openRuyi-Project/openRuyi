# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name constant_time_eq
%global full_version 0.3.1
%global pkgname constant-time-eq-0.3

Name:           rust-constant-time-eq-0.3
Version:        0.3.1
Release:        %autorelease
Summary:        Rust crate "constant_time_eq"
License:        CC0-1.0 OR MIT-0 OR Apache-2.0
URL:            https://github.com/cesarb/constant_time_eq
#!RemoteAsset:  sha256:7c74b8349d32d297c9134b8c88677813a227df8f779daa29bfc29c183fe3dca6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/count-instructions-test) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "constant_time_eq"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
