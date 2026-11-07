# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name semver
%global full_version 0.6.0
%global pkgname semver-0.6

Name:           rust-semver-0.6
Version:        0.6.0
Release:        %autorelease
Summary:        Rust crate "semver"
License:        MIT OR Apache-2.0
URL:            https://docs.rs/crate/semver/
#!RemoteAsset:  sha256:7a3186ec9e65071a2095434b1f5bb24838d4e8e130f584c790f6033c79943537
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(semver-parser-0.7/default) >= 0.7.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/ci) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "semver"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
