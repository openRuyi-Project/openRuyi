# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name terminal_size
%global full_version 0.4.4
%global pkgname terminal-size-0.4

Name:           rust-terminal-size-0.4
Version:        0.4.4
Release:        %autorelease
Summary:        Rust crate "terminal_size"
License:        MIT OR Apache-2.0
URL:            https://github.com/eminence/terminal-size
#!RemoteAsset:  sha256:230a1b821ccbd75b185820a1f1ff7b14d21da1e442e22c0863ea5f08771a8874
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rustix-1/default) >= 1.0.1
Requires:       crate(rustix-1/termios) >= 1.0.1
Requires:       crate(windows-sys-0.59/default) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-foundation) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-system-console) >= 0.59.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "terminal_size"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
