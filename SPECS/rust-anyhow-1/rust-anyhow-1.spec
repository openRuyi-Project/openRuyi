# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name anyhow
%global full_version 1.0.104
%global pkgname anyhow-1

Name:           rust-anyhow-1
Version:        1.0.104
Release:        %autorelease
Summary:        Rust crate "anyhow"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/anyhow
#!RemoteAsset:  sha256:330a5ed07fa54e4702c9d6c4174f74427fc0ef6e214bbd677ae50a5099946470
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/backtrace) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "anyhow"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
