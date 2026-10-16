# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name fd-lock
%global full_version 4.0.4
%global pkgname fd-lock-4

Name:           rust-fd-lock-4
Version:        4.0.4
Release:        %autorelease
Summary:        Rust crate "fd-lock"
License:        MIT OR Apache-2.0
URL:            https://github.com/yoshuawuyts/fd-lock
#!RemoteAsset:  sha256:0ce92ff622d6dadf7349484f42c93271a0d49b7cc4d466a936405bacbe10aa78
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(rustix-1/default) >= 1.0.0
Requires:       crate(rustix-1/fs) >= 1.0.0
Requires:       crate(windows-sys-0.52/default) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-foundation) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-storage-filesystem) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-system-io) >= 0.52.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "fd-lock"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
