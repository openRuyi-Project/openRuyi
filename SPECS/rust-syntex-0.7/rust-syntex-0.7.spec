# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name syntex
%global full_version 0.7.0
%global pkgname syntex-0.7

Name:           rust-syntex-0.7
Version:        0.7.0
Release:        %autorelease
Summary:        Rust crate "syntex"
License:        MIT OR Apache-2.0
URL:            https://github.com/erickt/rust-syntex
#!RemoteAsset:  sha256:76c050f0053387fc9cbf8fd8a792978f7170a9057217dc92606078b9647e88f5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(syntex-syntax-0.8/default) >= 0.8.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Patch2000:      2000-Use-compatible-versioned-dependencies.patch

%description
Source code for takopackized Rust crate "syntex"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
