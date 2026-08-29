# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gobject-sys
%global full_version 0.22.6
%global pkgname gobject-sys-0.22

Name:           rust-gobject-sys-0.22
Version:        0.22.6
Release:        %autorelease
Summary:        Rust crate "gobject-sys"
License:        MIT
URL:            https://gtk-rs.org/
#!RemoteAsset:  sha256:22a861859b887a79cf461359c192c97a57d8fb0229dd291232e57aa11f6fa72c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(glib-sys-0.22/default) >= 0.22.0
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
