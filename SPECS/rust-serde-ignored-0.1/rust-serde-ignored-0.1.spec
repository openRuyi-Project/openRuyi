# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serde_ignored
%global full_version 0.1.14
%global pkgname serde-ignored-0.1

Name:           rust-serde-ignored-0.1
Version:        0.1.14
Release:        %autorelease
Summary:        Rust crate "serde_ignored"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/serde-ignored
#!RemoteAsset:  sha256:115dffd5f3853e06e746965a20dcbae6ee747ae30b543d91b0e089668bb07798
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(serde-1) >= 1.0.220
Requires:       crate(serde-core-1/alloc) >= 1.0.220
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "serde_ignored"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
