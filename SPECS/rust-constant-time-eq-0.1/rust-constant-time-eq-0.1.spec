# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name constant_time_eq
%global full_version 0.1.5
%global pkgname constant-time-eq-0.1

Name:           rust-constant-time-eq-0.1
Version:        0.1.5
Release:        %autorelease
Summary:        Rust crate "constant_time_eq"
License:        CC0-1.0
URL:            https://github.com/cesarb/constant_time_eq
#!RemoteAsset:  sha256:245097e9a4535ee1e3e3931fcfcd55a796a44c643e8596ff6566d68f09b87bbc
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "constant_time_eq"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
