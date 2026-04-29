# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
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
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rustix-1.0/default) >= 1.1.4
Requires:       crate(rustix-1.0/termios) >= 1.1.4
Requires:       crate(windows-sys-0.61/default) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-foundation) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-system-console) >= 0.61.2
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "terminal_size"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
