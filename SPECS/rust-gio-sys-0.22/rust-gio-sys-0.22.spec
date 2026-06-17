# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gio-sys
%global full_version 0.22.0
%global pkgname gio-sys-0.22

Name:           rust-gio-sys-0.22
Version:        0.22.0
Release:        %autorelease
Summary:        Rust crate "gio-sys"
License:        MIT
URL:            https://gtk-rs.org/
#!RemoteAsset:  sha256:64729ba2772c080448f9f966dba8f4456beeb100d8c28a865ef8a0f2ef4987e1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(glib-sys-0.22/default) >= 0.22.0
Requires:       crate(gobject-sys-0.22/default) >= 0.22.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(system-deps-7) >= 7.0.0
Requires:       crate(windows-sys-0.52/default) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-networking-winsock) >= 0.52.0
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

%description
Source code for takopackized Rust crate "gio-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
