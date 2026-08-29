# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name if-addrs
%global full_version 0.13.4
%global pkgname if-addrs-0.13

Name:           rust-if-addrs-0.13
Version:        0.13.4
Release:        %autorelease
Summary:        Rust crate "if-addrs"
License:        MIT OR BSD-3-Clause
URL:            https://github.com/messense/if-addrs
#!RemoteAsset:  sha256:69b2eeee38fef3aa9b4cc5f1beea8a2444fc00e7377cafae396de3f5c2065e24
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(windows-sys-0.59/default) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-foundation) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-networking-winsock) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-networkmanagement-iphelper) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-networkmanagement-ndis) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-system-io) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-system-memory) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-system-threading) >= 0.59.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/link-local) = %{version}

%description
Source code for takopackized Rust crate "if-addrs"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
