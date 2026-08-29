# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wayland-csd-frame
%global full_version 0.3.0
%global pkgname wayland-csd-frame-0.3

Name:           rust-wayland-csd-frame-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "wayland-csd-frame"
License:        MIT
URL:            https://github.com/rust-windowing/wayland-csd-frame
#!RemoteAsset:  sha256:625c5029dbd43d25e6aa9615e88b829a5cad13b2819c4ae129fdbb7c31ab4c7e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.0.0
Requires:       crate(cursor-icon-1/default) >= 1.0.0
Requires:       crate(wayland-backend-0.3) >= 0.3.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "wayland-csd-frame"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
