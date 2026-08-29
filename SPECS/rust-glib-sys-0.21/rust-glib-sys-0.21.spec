# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name glib-sys
%global full_version 0.21.5
%global pkgname glib-sys-0.21

Name:           rust-glib-sys-0.21
Version:        0.21.5
Release:        %autorelease
Summary:        Rust crate "glib-sys"
License:        MIT
URL:            https://gtk-rs.org/
#!RemoteAsset:  sha256:2d95e1a3a19ae464a7286e14af9a90683c64d70c02532d88d87ce95056af3e6c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(system-deps-7) >= 7.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/v2-58) = %{version}
Provides:       crate(%{pkgname}/v2-60) = %{version}
Provides:       crate(%{pkgname}/v2-62) = %{version}
Provides:       crate(%{pkgname}/v2-64) = %{version}
Provides:       crate(%{pkgname}/v2-66) = %{version}
Provides:       crate(%{pkgname}/v2-68) = %{version}
Provides:       crate(%{pkgname}/v2-70) = %{version}
Provides:       crate(%{pkgname}/v2-72) = %{version}
Provides:       crate(%{pkgname}/v2-74) = %{version}
Provides:       crate(%{pkgname}/v2-76) = %{version}
Provides:       crate(%{pkgname}/v2-78) = %{version}
Provides:       crate(%{pkgname}/v2-80) = %{version}
Provides:       crate(%{pkgname}/v2-82) = %{version}
Provides:       crate(%{pkgname}/v2-84) = %{version}
Provides:       crate(%{pkgname}/v2-86) = %{version}

%description
Source code for takopackized Rust crate "glib-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
