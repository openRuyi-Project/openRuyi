# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name system-configuration
%global full_version 0.5.1
%global pkgname system-configuration-0.5

Name:           rust-system-configuration-0.5
Version:        0.5.1
Release:        %autorelease
Summary:        Rust crate "system-configuration"
License:        MIT OR Apache-2.0
URL:            https://github.com/mullvad/system-configuration-rs
#!RemoteAsset:  sha256:ba3a3adc5c275d719af8cb4272ea1c4a6d668a777f37e115f6d11ddbc1c8e0e7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-1/default) >= 1.0.0
Requires:       crate(core-foundation-0.9/default) >= 0.9.0
Requires:       crate(system-configuration-sys-0.5/default) >= 0.5.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "system-configuration"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
