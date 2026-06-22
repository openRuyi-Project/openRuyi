# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gtk4-sys
%global full_version 0.11.3
%global pkgname gtk4-sys-0.11

Name:           rust-gtk4-sys-0.11
Version:        0.11.3
Release:        %autorelease
Summary:        Rust crate "gtk4-sys"
License:        MIT
URL:            https://gtk-rs.org/gtk4-rs
#!RemoteAsset:  sha256:20ba8e695e2640455561274e65e45f0a151619e450746007667f4b23ceae4e1b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cairo-sys-rs-0.22/default) >= 0.22.0
Requires:       crate(gdk-pixbuf-sys-0.22/default) >= 0.22.0
Requires:       crate(gdk4-sys-0.11/default) >= 0.11.0
Requires:       crate(gio-sys-0.22/default) >= 0.22.0
Requires:       crate(gio-sys-0.22/v2-66) >= 0.22.0
Requires:       crate(glib-sys-0.22/default) >= 0.22.0
Requires:       crate(glib-sys-0.22/v2-66) >= 0.22.0
Requires:       crate(gobject-sys-0.22/default) >= 0.22.0
Requires:       crate(gobject-sys-0.22/v2-66) >= 0.22.0
Requires:       crate(graphene-sys-0.22/default) >= 0.22.0
Requires:       crate(gsk4-sys-0.11/default) >= 0.11.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(pango-sys-0.22/default) >= 0.22.0
Requires:       crate(pango-sys-0.22/v1-46) >= 0.22.0
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
Provides:       crate(%{pkgname}/v4-22) = %{version}
Provides:       crate(%{pkgname}/v4-24) = %{version}
Provides:       crate(%{pkgname}/v4-4) = %{version}
Provides:       crate(%{pkgname}/v4-6) = %{version}
Provides:       crate(%{pkgname}/v4-8) = %{version}

%description
Source code for takopackized Rust crate "gtk4-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
