# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cargo_metadata
%global full_version 0.2.3
%global pkgname cargo-metadata-0.2

Name:           rust-cargo-metadata-0.2
Version:        0.2.3
Release:        %autorelease
Summary:        Rust crate "cargo_metadata"
License:        MIT
URL:            https://github.com/oli-obk/cargo_metadata
#!RemoteAsset:  sha256:be1057b8462184f634c3a208ee35b0f935cfd94b694b26deadccd98732088d7b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(serde-1/default) >= 1.0.2
Requires:       crate(serde-derive-1/default) >= 1.0.2
Requires:       crate(serde-json-1/default) >= 1.0.1

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "cargo_metadata"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
