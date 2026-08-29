# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name polling
%global full_version 2.8.0
%global pkgname polling-2

Name:           rust-polling-2
Version:        2.8.0
Release:        %autorelease
Summary:        Rust crate "polling"
License:        Apache-2.0 OR MIT
URL:            https://github.com/smol-rs/polling
#!RemoteAsset:  sha256:4b2d323e8ca7996b3e23126511a523f7e62924d93ecd5ae73b333815b0eb3dce
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(autocfg-1) >= 1.0.0
Requires:       crate(bitflags-1/default) >= 1.3.2
Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(concurrent-queue-2/default) >= 2.2.0
Requires:       crate(libc-0.2/default) >= 0.2.77
Requires:       crate(log-0.4/default) >= 0.4.11
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.9
Requires:       crate(windows-sys-0.48/default) >= 0.48.0
Requires:       crate(windows-sys-0.48/win32-foundation) >= 0.48.0
Requires:       crate(windows-sys-0.48/win32-networking-winsock) >= 0.48.0
Requires:       crate(windows-sys-0.48/win32-storage-filesystem) >= 0.48.0
Requires:       crate(windows-sys-0.48/win32-system-io) >= 0.48.0
Requires:       crate(windows-sys-0.48/win32-system-libraryloader) >= 0.48.0
Requires:       crate(windows-sys-0.48/win32-system-threading) >= 0.48.0
Requires:       crate(windows-sys-0.48/win32-system-windowsprogramming) >= 0.48.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "polling"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
