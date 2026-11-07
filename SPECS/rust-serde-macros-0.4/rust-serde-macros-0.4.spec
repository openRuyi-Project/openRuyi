# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serde_macros
%global full_version 0.4.4
%global pkgname serde-macros-0.4

Name:           rust-serde-macros-0.4
Version:        0.4.4
Release:        %autorelease
Summary:        Rust crate "serde_macros"
License:        MIT OR Apache-2.0
URL:            https://github.com/erickt/rust-serde
#!RemoteAsset:  sha256:11c58e2a43b650a5521b596cfefc6b3bc5196f7fb2c1b36ef6dbefcdeccd279c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(serde-codegen-0.4/nightly) >= 0.4.3

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Patch2000:      2000-Use-a-versioned-compatible-dependency.patch

%description
Source code for takopackized Rust crate "serde_macros"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
