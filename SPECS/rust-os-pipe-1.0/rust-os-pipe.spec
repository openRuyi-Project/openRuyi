# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name os_pipe
%global full_version 1.2.2
%global pkgname os-pipe-1.0

Name:           rust-os-pipe-1.0
Version:        1.2.2
Release:        %autorelease
Summary:        Rust crate "os_pipe"
License:        MIT
URL:            https://github.com/oconnor663/os_pipe.rs
#!RemoteAsset:  sha256:db335f4760b14ead6290116f2427bf33a14d4f0617d49f78a246de10c1831224
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.186
Requires:       crate(windows-sys-0.59/default) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-foundation) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-security) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-system-pipes) >= 0.59.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/io-safety)

%description
Source code for takopackized Rust crate "os_pipe"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
