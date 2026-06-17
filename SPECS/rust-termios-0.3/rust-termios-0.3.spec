# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name termios
%global full_version 0.3.3
%global pkgname termios-0.3

Name:           rust-termios-0.3
Version:        0.3.3
Release:        %autorelease
Summary:        Rust crate "termios"
License:        MIT
URL:            https://github.com/dcuddeback/termios-rs
#!RemoteAsset:  sha256:411c5bf740737c7918b8b1fe232dca4dc9f8e754b8ad5e20966814001ed0ac6b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "termios"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
