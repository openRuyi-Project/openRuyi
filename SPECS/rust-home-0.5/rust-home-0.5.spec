# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name home
%global full_version 0.5.12
%global pkgname home-0.5

Name:           rust-home-0.5
Version:        0.5.12
Release:        %autorelease
Summary:        Rust crate "home"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/cargo
#!RemoteAsset:  sha256:cc627f471c528ff0c4a49e1d5e60450c8f6461dd6d10ba9dcd3a61d3dff7728d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(windows-sys-0.61/default) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-foundation) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-system-com) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-ui-shell) >= 0.61.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "home"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
