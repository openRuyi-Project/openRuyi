# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name system-configuration-sys
%global full_version 0.5.0
%global pkgname system-configuration-sys-0.5

Name:           rust-system-configuration-sys-0.5
Version:        0.5.0
Release:        %autorelease
Summary:        Rust crate "system-configuration-sys"
License:        MIT OR Apache-2.0
URL:            https://github.com/mullvad/system-configuration-rs
#!RemoteAsset:  sha256:a75fb188eb626b924683e3b95e3a48e63551fcfb51949de2f06a9d91dbee93c9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(core-foundation-sys-0.8/default) >= 0.8.0
Requires:       crate(libc-0.2/default) >= 0.2.49

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "system-configuration-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
