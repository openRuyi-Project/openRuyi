# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rustc_version
%global full_version 0.2.3
%global pkgname rustc-version-0.2

Name:           rust-rustc-version-0.2
Version:        0.2.3
Release:        %autorelease
Summary:        Rust crate "rustc_version"
License:        MIT OR Apache-2.0
URL:            https://github.com/Kimundi/rustc-version-rs
#!RemoteAsset:  sha256:138e3e0acb6c9fb258b19b67cb8abd63c00679d2851805ea151465464fe9030a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(semver-0.9/default) >= 0.9.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "rustc_version"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
