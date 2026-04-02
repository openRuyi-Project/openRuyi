# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name socket2
%global full_version 0.6.3
%global pkgname socket2-0.6

Name:           rust-socket2-0.6
Version:        0.6.3
Release:        %autorelease
Summary:        Rust crate "socket2"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/socket2
#!RemoteAsset:  sha256:3a766e1110788c36f4fa1c2b71b387a7815aa65f88ce0229841826633d93723e
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.184
Requires:       crate(windows-sys-0.61/default) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-foundation) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-networking-winsock) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-system-io) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-system-threading) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-system-windowsprogramming) >= 0.61.2
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/all)
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "socket2"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
