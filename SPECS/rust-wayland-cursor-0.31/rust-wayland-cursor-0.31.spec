# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wayland-cursor
%global full_version 0.31.14
%global pkgname wayland-cursor-0.31

Name:           rust-wayland-cursor-0.31
Version:        0.31.14
Release:        %autorelease
Summary:        Rust crate "wayland-cursor"
License:        MIT
URL:            https://github.com/smithay/wayland-rs
#!RemoteAsset:  sha256:4a52d18780be9b1314328a3de5f930b73d2200112e3849ca6cb11822793fb34d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rustix-1/default) >= 1.0.2
Requires:       crate(rustix-1/shm) >= 1.0.2
Requires:       crate(wayland-client-0.31/default) >= 0.31.14
Requires:       crate(xcursor-0.3/default) >= 0.3.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "wayland-cursor"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
