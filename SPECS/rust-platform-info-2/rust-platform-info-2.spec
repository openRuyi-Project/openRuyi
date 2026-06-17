# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name platform-info
%global full_version 2.1.0
%global pkgname platform-info-2

Name:           rust-platform-info-2
Version:        2.1.0
Release:        %autorelease
Summary:        Rust crate "platform-info"
License:        MIT
URL:            https://github.com/uutils/platform-info
#!RemoteAsset:  sha256:9368d62437c8cbb7c31ee37fd8c08a7d390e09a3ff75698a674953f46705ffcb
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.154
Requires:       crate(windows-sys-0.59/default) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-foundation) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-storage-filesystem) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-system-libraryloader) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-system-systeminformation) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-system-systemservices) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-system-threading) >= 0.59.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "platform-info"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
