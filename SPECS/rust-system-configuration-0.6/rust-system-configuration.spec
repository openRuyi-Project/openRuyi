# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name system-configuration
%global full_version 0.6.1
%global pkgname system-configuration-0.6

Name:           rust-system-configuration-0.6
Version:        0.6.1
Release:        %autorelease
Summary:        Rust crate "system-configuration"
License:        MIT OR Apache-2.0
URL:            https://github.com/mullvad/system-configuration-rs
#!RemoteAsset:  sha256:3c879d448e9d986b661742763247d3693ed13609438cf3d006f51f5368a5ba6b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2.0/default) >= 2.9.1
Requires:       crate(core-foundation-0.9/default) >= 0.9.4
Requires:       crate(system-configuration-sys-0.6/default) >= 0.6.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "system-configuration"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
