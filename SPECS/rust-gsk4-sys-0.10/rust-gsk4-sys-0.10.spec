# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gsk4-sys
%global full_version 0.10.3
%global pkgname gsk4-sys-0.10

Name:           rust-gsk4-sys-0.10
Version:        0.10.3
Release:        %autorelease
Summary:        Rust crate "gsk4-sys"
License:        MIT
URL:            https://gtk-rs.org/gtk4-rs
#!RemoteAsset:  sha256:7ce91472391146f482065f1041876d8f869057b195b95399414caa163d72f4f7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cairo-sys-rs-0.21/default) >= 0.21.0
Requires:       crate(gdk4-sys-0.10/default) >= 0.10.0
Requires:       crate(glib-sys-0.21/default) >= 0.21.0
Requires:       crate(glib-sys-0.21/v2-66) >= 0.21.0
Requires:       crate(gobject-sys-0.21/default) >= 0.21.0
Requires:       crate(gobject-sys-0.21/v2-66) >= 0.21.0
Requires:       crate(graphene-sys-0.21/default) >= 0.21.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(pango-sys-0.21/default) >= 0.21.0
Requires:       crate(pango-sys-0.21/v1-46) >= 0.21.0
Requires:       crate(system-deps-7) >= 7.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/broadway) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/v4-10) = %{version}
Provides:       crate(%{pkgname}/v4-14) = %{version}
Provides:       crate(%{pkgname}/v4-16) = %{version}
Provides:       crate(%{pkgname}/v4-18) = %{version}
Provides:       crate(%{pkgname}/v4-2) = %{version}
Provides:       crate(%{pkgname}/v4-20) = %{version}
Provides:       crate(%{pkgname}/v4-4) = %{version}
Provides:       crate(%{pkgname}/v4-6) = %{version}
Provides:       crate(%{pkgname}/vulkan) = %{version}

%description
Source code for takopackized Rust crate "gsk4-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
