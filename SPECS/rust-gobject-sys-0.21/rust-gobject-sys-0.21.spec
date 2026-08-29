# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gobject-sys
%global full_version 0.21.5
%global pkgname gobject-sys-0.21

Name:           rust-gobject-sys-0.21
Version:        0.21.5
Release:        %autorelease
Summary:        Rust crate "gobject-sys"
License:        MIT
URL:            https://gtk-rs.org/
#!RemoteAsset:  sha256:2dca35da0d19a18f4575f3cb99fe1c9e029a2941af5662f326f738a21edaf294
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(glib-sys-0.21/default) >= 0.21.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(system-deps-7) >= 7.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/v2-58) = %{version}
Provides:       crate(%{pkgname}/v2-62) = %{version}
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
Source code for takopackized Rust crate "gobject-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
