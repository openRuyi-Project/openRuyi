# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gdk4-sys
%global full_version 0.10.3
%global pkgname gdk4-sys-0.10

Name:           rust-gdk4-sys-0.10
Version:        0.10.3
Release:        %autorelease
Summary:        Rust crate "gdk4-sys"
License:        MIT
URL:            https://gtk-rs.org/gtk4-rs
#!RemoteAsset:  sha256:a6d4e5b3ccf591826a4adcc83f5f57b4e59d1925cb4bf620b0d645f79498b034
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cairo-sys-rs-0.21/default) >= 0.21.0
Requires:       crate(gdk-pixbuf-sys-0.21/default) >= 0.21.0
Requires:       crate(gio-sys-0.21/default) >= 0.21.0
Requires:       crate(gio-sys-0.21/v2-66) >= 0.21.0
Requires:       crate(glib-sys-0.21/default) >= 0.21.0
Requires:       crate(glib-sys-0.21/v2-66) >= 0.21.0
Requires:       crate(gobject-sys-0.21/default) >= 0.21.0
Requires:       crate(gobject-sys-0.21/v2-66) >= 0.21.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(pango-sys-0.21/default) >= 0.21.0
Requires:       crate(pango-sys-0.21/v1-46) >= 0.21.0
Requires:       crate(pkg-config-0.3) >= 0.3.32
Requires:       crate(system-deps-7) >= 7.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/v4-10) = %{version}
Provides:       crate(%{pkgname}/v4-12) = %{version}
Provides:       crate(%{pkgname}/v4-14) = %{version}
Provides:       crate(%{pkgname}/v4-16) = %{version}
Provides:       crate(%{pkgname}/v4-18) = %{version}
Provides:       crate(%{pkgname}/v4-2) = %{version}
Provides:       crate(%{pkgname}/v4-20) = %{version}
Provides:       crate(%{pkgname}/v4-4) = %{version}
Provides:       crate(%{pkgname}/v4-6) = %{version}
Provides:       crate(%{pkgname}/v4-8) = %{version}

%description
Source code for takopackized Rust crate "gdk4-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
