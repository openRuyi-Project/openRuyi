# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name scopeguard
%global full_version 1.2.0
%global pkgname scopeguard-1

Name:           rust-scopeguard-1
Version:        1.2.0
Release:        %autorelease
Summary:        Rust crate "scopeguard"
License:        MIT OR Apache-2.0
URL:            https://github.com/bluss/scopeguard
#!RemoteAsset:  sha256:94143f37725109f92c262ed2cf5e59bce7498c01bcc1502d7b9afe439a4e9f49
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/use-std) = %{version}

%description
Defines the macros `defer!`, `defer_on_unwind!`, `defer_on_success!` as shorthands for guards with one of the implemented strategies.
Source code for takopackized Rust crate "scopeguard"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
