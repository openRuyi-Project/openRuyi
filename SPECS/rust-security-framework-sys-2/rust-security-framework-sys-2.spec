# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name security-framework-sys
%global full_version 2.17.0
%global pkgname security-framework-sys-2

Name:           rust-security-framework-sys-2
Version:        2.17.0
Release:        %autorelease
Summary:        Rust crate "security-framework-sys"
License:        MIT OR Apache-2.0
URL:            https://lib.rs/crates/security-framework-sys
#!RemoteAsset:  sha256:6ce2691df843ecc5d231c0b14ece2acc3efb62c0a398c7e1d875f3983ce020e3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(core-foundation-sys-0.8/default) >= 0.8.7
Requires:       crate(libc-0.2/default) >= 0.2.150
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/macos-12) = %{version}
Provides:       crate(%{pkgname}/osx-10-10) = %{version}
Provides:       crate(%{pkgname}/osx-10-11) = %{version}
Provides:       crate(%{pkgname}/osx-10-12) = %{version}
Provides:       crate(%{pkgname}/osx-10-13) = %{version}
Provides:       crate(%{pkgname}/osx-10-14) = %{version}
Provides:       crate(%{pkgname}/osx-10-15) = %{version}
Provides:       crate(%{pkgname}/osx-10-9) = %{version}

%description
Source code for takopackized Rust crate "security-framework-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
