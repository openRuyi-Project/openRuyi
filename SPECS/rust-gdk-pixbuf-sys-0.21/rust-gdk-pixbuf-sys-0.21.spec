# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gdk-pixbuf-sys
%global full_version 0.21.5
%global pkgname gdk-pixbuf-sys-0.21

Name:           rust-gdk-pixbuf-sys-0.21
Version:        0.21.5
Release:        %autorelease
Summary:        Rust crate "gdk-pixbuf-sys"
License:        MIT
URL:            https://gtk-rs.org/
#!RemoteAsset:  sha256:bd95ad50b9a3d2551e25dd4f6892aff0b772fe5372d84514e9d0583af60a0ce7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(gio-sys-0.21/default) >= 0.21.0
Requires:       crate(glib-sys-0.21/default) >= 0.21.0
Requires:       crate(gobject-sys-0.21/default) >= 0.21.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(system-deps-7) >= 7.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/v2-40) = %{version}
Provides:       crate(%{pkgname}/v2-42) = %{version}
Provides:       crate(%{pkgname}/v2-44) = %{version}

%description
Source code for takopackized Rust crate "gdk-pixbuf-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
