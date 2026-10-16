# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name terminal_size
%global full_version 0.2.6
%global pkgname terminal-size-0.2

Name:           rust-terminal-size-0.2
Version:        0.2.6
Release:        %autorelease
Summary:        Rust crate "terminal_size"
License:        MIT OR Apache-2.0
URL:            https://github.com/eminence/terminal-size
#!RemoteAsset:  sha256:8e6bf6f19e9f8ed8d4048dc22981458ebcf406d67e94cd422e5ecd73d63b3237
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rustix-0.37/default) >= 0.37.0
Requires:       crate(rustix-0.37/termios) >= 0.37.0
Requires:       crate(windows-sys-0.48/default) >= 0.48.0
Requires:       crate(windows-sys-0.48/win32-foundation) >= 0.48.0
Requires:       crate(windows-sys-0.48/win32-system-console) >= 0.48.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "terminal_size"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
