# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name miow
%global full_version 0.6.1
%global pkgname miow-0.6

Name:           rust-miow-0.6
Version:        0.6.1
Release:        %autorelease
Summary:        Rust crate "miow"
License:        MIT OR Apache-2.0
URL:            https://github.com/yoshuawuyts/miow
#!RemoteAsset:  sha256:536bfad37a309d62069485248eeaba1e8d9853aaf951caaeaed0585a95346f08
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(windows-sys-0.60/default) >= 0.60.0
Requires:       crate(windows-sys-0.60/win32-foundation) >= 0.60.0
Requires:       crate(windows-sys-0.60/win32-networking-winsock) >= 0.60.0
Requires:       crate(windows-sys-0.60/win32-security) >= 0.60.0
Requires:       crate(windows-sys-0.60/win32-storage-filesystem) >= 0.60.0
Requires:       crate(windows-sys-0.60/win32-system-io) >= 0.60.0
Requires:       crate(windows-sys-0.60/win32-system-pipes) >= 0.60.0
Requires:       crate(windows-sys-0.60/win32-system-threading) >= 0.60.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "miow"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
