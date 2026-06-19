# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cargo-platform
%global full_version 0.3.1
%global pkgname cargo-platform-0.3

Name:           rust-cargo-platform-0.3
Version:        0.3.1
Release:        %autorelease
Summary:        Rust crate "cargo-platform"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/cargo
#!RemoteAsset:  sha256:122ec45a44b270afd1402f351b782c676b173e3c3fb28d86ff7ebfb4d86a4ee4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(serde-1/default) >= 1.0.219
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "cargo-platform"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
