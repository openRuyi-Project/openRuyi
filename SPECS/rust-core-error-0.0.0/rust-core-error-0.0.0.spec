# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name core-error
%global full_version 0.0.0
%global pkgname core-error-0.0.0

Name:           rust-core-error-0.0.0
Version:        0.0.0
Release:        %autorelease
Summary:        Rust crate "core-error"
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/core-error
#!RemoteAsset:  sha256:efcdb2972eb64230b4c50646d8498ff73f5128d196a90c7236eec4cbe8619b8f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(version-check-0.9) >= 0.9.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "core-error"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
