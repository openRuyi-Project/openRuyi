# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name os_pipe
%global full_version 1.2.3
%global pkgname os-pipe-1

Name:           rust-os-pipe-1
Version:        1.2.3
Release:        %autorelease
Summary:        Rust crate "os_pipe"
License:        MIT
URL:            https://github.com/oconnor663/os_pipe.rs
#!RemoteAsset:  sha256:7d8fae84b431384b68627d0f9b3b1245fcf9f46f6c0e3dc902e9dce64edd1967
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.62
Requires:       crate(windows-sys-0.28/default) >= 0.28.0
Requires:       crate(windows-sys-0.28/win32-foundation) >= 0.28.0
Requires:       crate(windows-sys-0.28/win32-security) >= 0.28.0
Requires:       crate(windows-sys-0.28/win32-system-pipes) >= 0.28.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/io-safety) = %{version}

%description
Source code for takopackized Rust crate "os_pipe"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
