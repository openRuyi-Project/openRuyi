# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gio-win32-sys
%global full_version 0.22.0
%global pkgname gio-win32-sys-0.22

Name:           rust-gio-win32-sys-0.22
Version:        0.22.0
Release:        %autorelease
Summary:        Rust crate "gio-win32-sys"
License:        MIT
URL:            https://gtk-rs.org/
#!RemoteAsset:  sha256:d673cd130fa7b598cf3fa776265a8e4c02634f3283433d441b8fc6f9fe07f327
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(gio-sys-0.22/default) >= 0.22.0
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
Provides:       crate(%{pkgname}/v2-66) = %{version}
Provides:       crate(%{pkgname}/v2-78) = %{version}
Provides:       crate(%{pkgname}/v2-82) = %{version}
Provides:       crate(%{pkgname}/v2-84) = %{version}

%description
Source code for takopackized Rust crate "gio-win32-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
