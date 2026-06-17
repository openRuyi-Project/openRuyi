# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name vergen-lib
%global full_version 9.1.0
%global pkgname vergen-lib-9

Name:           rust-vergen-lib-9
Version:        9.1.0
Release:        %autorelease
Summary:        Rust crate "vergen-lib"
License:        MIT OR Apache-2.0
URL:            https://github.com/rustyhorde/vergen
#!RemoteAsset:  sha256:b34a29ba7e9c59e62f229ae1932fb1b8fb8a6fdcc99215a641913f5f5a59a569
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1/default) >= 1.0.100
Requires:       crate(derive-builder-0.20/default) >= 0.20.2
Requires:       crate(rustversion-1) >= 1.0.22
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/build) = %{version}
Provides:       crate(%{pkgname}/cargo) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/emit-and-set) = %{version}
Provides:       crate(%{pkgname}/git) = %{version}
Provides:       crate(%{pkgname}/rustc) = %{version}
Provides:       crate(%{pkgname}/si) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}

%description
Source code for takopackized Rust crate "vergen-lib"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
