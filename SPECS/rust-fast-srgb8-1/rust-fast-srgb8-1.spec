# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name fast-srgb8
%global full_version 1.0.0
%global pkgname fast-srgb8-1

Name:           rust-fast-srgb8-1
Version:        1.0.0
Release:        %autorelease
Summary:        Rust crate "fast-srgb8"
License:        MIT OR Apache-2.0 OR CC0-1.0
URL:            https://github.com/thomcc/fast-srgb8
#!RemoteAsset:  sha256:dd2e7510819d6fbf51a5545c8f922716ecfb14df168a3242f7d33e0239efe6a1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "fast-srgb8"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
