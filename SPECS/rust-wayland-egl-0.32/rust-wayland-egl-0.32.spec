# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wayland-egl
%global full_version 0.32.11
%global pkgname wayland-egl-0.32

Name:           rust-wayland-egl-0.32
Version:        0.32.11
Release:        %autorelease
Summary:        Rust crate "wayland-egl"
License:        MIT
URL:            https://github.com/smithay/wayland-rs
#!RemoteAsset:  sha256:9b97bdb7c49e5bd9b7562f38ff84f0dad47079fdc9e926f691a787f6dbc05451
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(wayland-backend-0.3/client-system) >= 0.3.15
Requires:       crate(wayland-backend-0.3/default) >= 0.3.15
Requires:       crate(wayland-sys-0.31/default) >= 0.31.11
Requires:       crate(wayland-sys-0.31/egl) >= 0.31.11
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "wayland-egl"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
