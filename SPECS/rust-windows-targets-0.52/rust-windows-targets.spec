# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global debug_package %{nil}
%global __debug_install_post %{nil}

%global crate_name windows-targets
%global full_version 0.52.6
%global pkgname windows-targets-0.52

Name:           rust-windows-targets-0.52
Version:        0.52.6
Release:        %autorelease
Summary:        Rust crate "windows-targets"
License:        MIT OR Apache-2.0
URL:            https://github.com/microsoft/windows-rs
#!RemoteAsset:  sha256:9b724f72796e036ab90c1021d4780d4d3d648aca59e491e6b98e725b84e99973
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(windows-aarch64-gnullvm-0.52/default) >= 0.52.6
Requires:       crate(windows-aarch64-msvc-0.52/default) >= 0.52.6
Requires:       crate(windows-i686-gnu-0.52/default) >= 0.52.6
Requires:       crate(windows-i686-gnullvm-0.52/default) >= 0.52.6
Requires:       crate(windows-i686-msvc-0.52/default) >= 0.52.6
Requires:       crate(windows-x86-64-gnu-0.52/default) >= 0.52.6
Requires:       crate(windows-x86-64-gnullvm-0.52/default) >= 0.52.6
Requires:       crate(windows-x86-64-msvc-0.52/default) >= 0.52.6
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "windows-targets"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
