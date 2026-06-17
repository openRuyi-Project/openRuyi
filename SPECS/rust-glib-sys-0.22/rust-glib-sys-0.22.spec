# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name glib-sys
%global full_version 0.22.6
%global pkgname glib-sys-0.22

Name:           rust-glib-sys-0.22
Version:        0.22.6
Release:        %autorelease
Summary:        Rust crate "glib-sys"
License:        MIT
URL:            https://gtk-rs.org/
#!RemoteAsset:  sha256:5f7fbac234ed5bc2a28359b7bde8e1b9cdf1441cc2d7f068e4824672d7db9445
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
Provides:       crate(%{pkgname}/v2-88) = %{version}
Provides:       crate(%{pkgname}/v2-90) = %{version}

%description
Source code for takopackized Rust crate "glib-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
