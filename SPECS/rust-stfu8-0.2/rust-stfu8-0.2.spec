# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name stfu8
%global full_version 0.2.7
%global pkgname stfu8-0.2

Name:           rust-stfu8-0.2
Version:        0.2.7
Release:        %autorelease
Summary:        Rust crate "stfu8"
License:        MIT OR Apache-2.0
URL:            https://github.com/vitiral/stfu8
#!RemoteAsset:  sha256:e51f1e89f093f99e7432c491c382b88a6860a5adbe6bf02574bf0a08efff1978
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/testing) = %{version}

%description
Source code for takopackized Rust crate "stfu8"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
