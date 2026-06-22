# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name libadwaita-sys
%global full_version 0.9.1
%global pkgname libadwaita-sys-0.9

Name:           rust-libadwaita-sys-0.9
Version:        0.9.1
Release:        %autorelease
Summary:        Rust crate "libadwaita-sys"
License:        MIT
URL:            https://world.pages.gitlab.gnome.org/Rust/libadwaita-rs/
#!RemoteAsset:  sha256:aaee067051c5d3c058d050d167688b80b67de1950cfca77730549aa761fc5d7d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(gdk4-sys-0.11/default) >= 0.11.0
Requires:       crate(gio-sys-0.22/default) >= 0.22.0
Requires:       crate(glib-sys-0.22/default) >= 0.22.0
Requires:       crate(gobject-sys-0.22/default) >= 0.22.0
Requires:       crate(gtk4-sys-0.11/default) >= 0.11.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(pango-sys-0.22/default) >= 0.22.0
Requires:       crate(system-deps-7) >= 7.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/v1-1) = %{version}
Provides:       crate(%{pkgname}/v1-2) = %{version}
Provides:       crate(%{pkgname}/v1-3) = %{version}
Provides:       crate(%{pkgname}/v1-4) = %{version}
Provides:       crate(%{pkgname}/v1-5) = %{version}
Provides:       crate(%{pkgname}/v1-6) = %{version}
Provides:       crate(%{pkgname}/v1-7) = %{version}
Provides:       crate(%{pkgname}/v1-8) = %{version}
Provides:       crate(%{pkgname}/v1-9) = %{version}

%description
Source code for takopackized Rust crate "libadwaita-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
