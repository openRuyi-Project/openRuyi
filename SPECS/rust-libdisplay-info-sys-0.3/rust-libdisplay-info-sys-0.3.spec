# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name libdisplay-info-sys
%global full_version 0.3.0
%global pkgname libdisplay-info-sys-0.3

Name:           rust-libdisplay-info-sys-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "libdisplay-info-sys"
License:        MIT
URL:            https://github.com/Smithay/libdisplay-info-rs
#!RemoteAsset:  sha256:26590d55b8819f9c6b0d95d9d12dc9edbfd1f2413e88814a33b631ac049bb51f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(semver-1) >= 1.0.24
Requires:       crate(system-deps-7) >= 7.0.3
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/auto) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/v0-1) = %{version}
Provides:       crate(%{pkgname}/v0-2) = %{version}
Provides:       crate(%{pkgname}/v0-3) = %{version}

%description
Source code for takopackized Rust crate "libdisplay-info-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
