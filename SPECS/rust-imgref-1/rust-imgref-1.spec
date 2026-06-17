# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name imgref
%global full_version 1.12.2
%global pkgname imgref-1

Name:           rust-imgref-1
Version:        1.12.2
Release:        %autorelease
Summary:        Rust crate "imgref"
License:        CC0-1.0 OR Apache-2.0
URL:            https://lib.rs/crates/imgref
#!RemoteAsset:  sha256:89194689a993ab15268672e99e7b0e19da2da3268ac682e8f02d29d4d1434cd7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/deprecated) = %{version}

%description
Source code for takopackized Rust crate "imgref"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
